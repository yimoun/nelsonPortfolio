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

## 2. Multi-provider : Groq + LM Studio (local)

**Décision** : Supporter deux providers LLM avec fallback automatique.

- **Groq** (cloud) : `llama-3.3-70b-versatile` — rapide, performant, utilisé en production
- **LM Studio** (local) : API OpenAI-compatible sur `localhost:1234` — utilisé en développement

**Pourquoi LM Studio en local et pas Ollama ?** : LM Studio était déjà installé sur la machine.
LM Studio expose une API compatible OpenAI (`localhost:1234`), donc on utilise `ChatOpenAI` de LangChain
comme client (ce n'est pas OpenAI le service, c'est juste le format d'API qui est le même).
Ollama aurait nécessité une installation supplémentaire et utilise son propre protocole (`ChatOllama`)...  **d'où la décision de Switcher.**

---

## 3. Routing par environnement (local vs production)

## 4. Résilience : retry + fallback + concurrency
**Décision** : L'orchestrateur implémente 3 mécanismes de résilience.
- **Retry** : Chaque provider est réessayé `LLM_RETRIES` fois avant d'être abandonné
- **Fallback** : Si le provider principal échoue, on bascule sur l'autre
- **Semaphore** : `MAX_CONCURRENT_REQUESTS` limite les requêtes simultanées pour éviter la surcharge

**Pourquoi** : Les APIs LLM sont instables (rate limits, timeouts, pannes).
Un assistant portfolio doit rester disponible — un recruteur qui tombe sur une erreur ne reviendra pas.


## 6. State management
**Décision** : Typer l'état avec `TypedDict` (LangChain pattern).

```python
class AgentState(TypedDict):
    messages: List[BaseMessage]
```

**Pourquoi** : Prépare l'intégration future de LangGraph (qui attend un `TypedDict` comme state).
Même sans LangGraph pour l'instant, le typage rend le code plus lisible et auto-documenté.
