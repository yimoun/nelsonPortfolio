import chainlit as cl
from state import AgentState
from langchain_core.messages import HumanMessage, AIMessage

# Chat Start
@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("state", {"messages": []})
    await cl.Message(
            content="👋 Hello! Je suis l'assistant IA qui répond à tes questions réponds à toutes tes"
                    + "questions sur Nelson Yimou. Comment puis-je t'aider aujourd'hui ?").send()

# Handle Messages
@cl.on_message
async def on_message(msg: cl.Message):
    state: AgentState = cl.user_session.get("state")
    state["messages"].append(HumanMessage(content=msg.content))

    ai_msg = cl.Message(content="")
    await ai_msg.send()

    content = ""
    # async for chunk in limited_stream(state["messages"]):
    #     content += chunk.content
    #     await ai_msg.stream_token(chunk.content)

    state["messages"].append(AIMessage(content=content))
    cl.user_session.set("state", state)
    await ai_msg.update()

# Chat Stop
@cl.on_stop
def on_stop():
    print("L'utilisateur souhaite arrêter le chat")

# Chat End
@cl.on_chat_end
def on_chat_end():
    print("L'utilisateur a quitté la session")