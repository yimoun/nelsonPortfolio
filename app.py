import chainlit as cl
from graph import agent
from langchain_core.messages import HumanMessage

# Chat Start
@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("state", {"messages": []})
    await cl.Message(
            content="👋 Hello! Je suis un assistant IA qui répond à toutes tes"
                    + " questions sur [Nelson Yimou](https://www.linkedin.com/in/nelson-yimou-02493621a/). "
                    + "Comment puis-je t'aider aujourd'hui ?").send()

# Handle Messages
@cl.on_message
async def on_message(msg: cl.Message):
    state = cl.user_session.get("state")
    state["messages"].append(HumanMessage(content=msg.content))

    final_state = await agent.ainvoke(state)

    ai_response = final_state["messages"][-1].content
    cl.user_session.set("state", final_state)
    await cl.Message(content=ai_response).send()

    print("cl.user_session:", cl.user_session.get("state"))

# Chat Stop
@cl.on_stop
def on_stop():
    print("L'utilisateur souhaite arrêter le chat")

# Chat End
@cl.on_chat_end
def on_chat_end():
    print("L'utilisateur a quitté la session")
