# Comprehension du SQLAlchemy Data Layer

Chainlit doit gérer 3 choses fondamentales :

1️⃣ Conversations (threads)
2️⃣ Exécution (étapes d'exécution) des agents (steps)
3️⃣ Traces + UI + feedback (elements + feedbacks)

👉 Donc la DB est conçue comme un système de traçage d’exécution d’agent IA, pas juste un chat.
User
 └── Threads (conversation)
      ├── Steps (exécution IA)
      │     └── Steps enfants (raisonnement, tools, etc.)
      ├── Elements (UI / fichiers / outputs riches)
      └── Feedbacks (qualité / évaluation)

🔥 Ce que peut être un step :
    --> un prompt envoyé au LLM
    --> une réponse du LLM
    --> un appel à un tool (API, DB, function)
    --> une étape de raisonnement (chain-of-thought)
    -> une erreur
    --> un streaming en cours

Exemple reel de Steps pour un threads
    Step 1: User input
    Step 2: LLM thinking
    Step 3: Tool call (API météo)
    Step 4: Résultat tool
    Step 5: Réponse finale

🌳 Particularité clé : structure hiérarchique
    Step (parent)
    ├── Step (LLM thinking)
    ├── Step (tool call)
    └── Step (final answer)

Les Elements: 🎯 Rôle: Stocke les objets affichés dans l’interface

🧠 Exemples
    image générée
    fichier PDF
    graphique
    code snippet
    audio
    vidéo