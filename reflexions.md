# Réflexions & Décisions — Nelson Portfolio AI

> Ce fichier documente ma manière de penser, les décisions architecturales importantes
> et les choix techniques pris durant le développement de ce projet.

---

## 1. Architecture générale

**Décision** : Séparer le code en modules spécialisés plutôt qu'un seul fichier monolithique. Chaque fichier a une responsabilité bien précise.

```
Client (Browser)
      ↓
Chainlit (UI + API)         → app.py
      ↓
Orchestrator (retry/queue)  → orchestrator.py
      ↓
Routing (smart selection)   → routing.py
      ↓
Providers (LLM factory)    → providers.py
      ↓
State (typage)              → state.py
```

---

## 2. Multi-provider : évolution des choix

### v1 — Ollama (local) + Groq (cloud)

**Décision initiale** : Utiliser Ollama en local et Groq en production.

**Problème rencontré** : Ollama nécessitait une installation (`brew install ollama`) + le téléchargement
d'un modèle (~4-5 Go) + un serveur tournant en permanence (`ollama serve`).

### v2 — LM Studio (local) + Groq (cloud)

**Pivot** : Remplacer Ollama par LM Studio, déjà installé sur ma machine.
LM Studio expose une API compatible OpenAI (`localhost:1234`), donc utilisation de `ChatOpenAI`.

**Problème réalisé** : L'architecture local/cloud n'a pas de sens pour un projet destiné à être
déployé en production. En prod, il n'y a pas de serveur local. Le fallback local → cloud
était un exercice artificiel (Donc unitil pour ce type de Projet), pas une architecture production-ready.

### v3 (actuelle) — Groq (principal) + Gemini (fallback)

**Décision finale** : Deux providers **cloud**, tous deux gratuits.
- **Groq** : `llama-3.3-70b-versatile` — ultra rapide grâce au hardware LPU, provider principal
- **Gemini** : `gemini-2.0-flash` — API gratuite Google, utilisé en fallback

**Pourquoi ce choix** : Si Groq tombe (rate limit, panne), le chatbot bascule automatiquement
sur Gemini sans interruption. Un utilisateur ne verra jamais d'erreur:
production-ready, pas un artifice local/cloud. Les deux providers sont gratuits, donc aucun coût.

**Variable `ENVIRONMENT` retirée** : Plus besoin de distinguer local/prod — le même code tourne
partout avec les mêmes providers cloud.

---

## 3. Routing simplifié

**v1** : Routing par environnement (`ENVIRONMENT=local` → LM Studio, `production` → Groq).

**v2** : Le routing sélectionne le provider dont la clé API est disponible.
Groq est prioritaire (plus rapide). Si sa clé manque, Gemini prend le relais.
Plus de variable d'environnement à gérer — la présence des clés API suffit.

---

## 4. Résilience : retry + fallback + concurrency

**Décision** : L'orchestrateur implémente 3 mécanismes de résilience.
- **Retry** : Chaque provider est réessayé `LLM_RETRIES` fois avant d'être abandonné
- **Fallback** : Si le provider principal échoue après tous les retries, on bascule sur l'autre provider
- **Semaphore** : `MAX_CONCURRENT_REQUESTS` limite les requêtes simultanées pour éviter la surcharge

**Pourquoi** : Les APIs LLM sont instables (rate limits, timeouts, pannes).
Un assistant portfolio doit rester disponible — un recruteur qui tombe sur une erreur ne reviendra pas.

**Évolution** : Le fallback est maintenant symétrique (Groq ↔ Gemini) au lieu de
unidirectionnel (local → cloud). Les deux chemins sont viables en production.

---

## 5. State management

**Décision** : Typer l'état avec `TypedDict` (LangChain pattern).

```python
class AgentState(TypedDict):
    messages: List[BaseMessage]
```

**Pourquoi** : Prépare l'intégration future de LangGraph (qui attend un `TypedDict` comme state).
Même sans LangGraph pour l'instant, le typage rend le code plus lisible et auto-documenté.
