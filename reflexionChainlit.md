
# Initialize LLM (langchain_ollama, ou tout autre)
# Define Agent state
# LangGraph node 
# Build LangGraph

# Chat Session Start
# Handle Messages
# Chat stop
# Chat End

#  Separated streaming function
# on_chat_resume
    # autehtification: firts with CHAINLIT_AUTH_SECRET, second with Password Auth (or mix with OAuth, Header)
    # Data persistance
    choosed : # SQLAlchemy Data Layer #
        After installing PostgreSQL you need to do 3 things:
            1. Create User 'admin' with password 'admin'
            2. Create new database 'my_chainlit_db'
            3. Grant all permission of 'my_chainlit_db' to user 'admin'
    Next we have to launch this installation: pip install asyncpg SQLAlchemy aiohttp greenlet

    # @cl.data_layer with the conninfo=DATABASEURL

# Deploy Chainlit with FastAPI and/or with Ngrok
# Customization: 
    -->Logo and FavIcon
    -->Chainlit Theme / CSS / Remote Watermark

# Les Starters
    --> Personnaliser un message d'acceuil pour chaque Starter

# Diplay elements: Images and PDF / Videos & Audio / Draw Bar Pie Scatter Charts / 

[ Client (Browser) ]
        ↓
[ Chainlit (UI + API) ]
        ↓
[ LangGraph (Agent Engine) ]
        ↓
[ Tools / LLM / Services ]
        ↓
[ Data Layer (PostgreSQL + Storage) ]













# Des commits
1.  on_chat_start & on_message_handle & on_stop & on_chat_end & stream_llm_response
2. chat_resume. 
