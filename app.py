import streamlit as st
import os
from groq import Groq
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch Groq API Key
groq_api_key = os.environ['GROQ_API_KEY']

def main():
    # App Title and Description
    st.title("🤖 AI Assistant with Groq")
    st.markdown("A conversational chatbot powered by Groq and Langchain.")

    # Sidebar Configuration
    st.sidebar.header("🛠️ Configuration")
    selected_model = st.sidebar.selectbox(
        "Choose a Language Model:",
        ['mixtral-8x7b-32768', 'llama2-70b-4096'],
        help="Select the LLM to power the conversation."
    )
    memory_length = st.sidebar.slider(
        "Conversation Memory Length (messages):",
        min_value=1, 
        max_value=10, 
        value=5,
        help="Set the number of previous messages the chatbot will remember."
    )

    # Initialize Conversational Memory
    memory = ConversationBufferWindowMemory(k=memory_length)

    # User Input Section
    st.subheader("💬 Chat with the Assistant")
    user_query = st.text_area("Enter your question or message:", placeholder="Type here...")

    # Chat History Setup
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    else:
        # Load previous chat history into memory
        for message in st.session_state.chat_history:
            memory.save_context({'input': message['user']}, {'output': message['bot']})

    # Initialize Groq Chat Object and Conversation Chain
    groq_chat = ChatGroq(
        groq_api_key=groq_api_key,
        model_name=selected_model
    )
    conversation = ConversationChain(
        llm=groq_chat,
        memory=memory
    )

    # Generate Response and Display Chat
    if user_query:
        response = conversation(user_query)
        bot_reply = response['response']

        # Display Latest Bot Response Separately
        st.write("### Latest Response")
        st.success(bot_reply)

        # Save the exchange to session state
        st.session_state.chat_history.append({'user': user_query, 'bot': bot_reply})

        # Display Chat History
        st.subheader("📝 Chat History")
        for chat in st.session_state.chat_history:
            st.markdown(f"**You:** {chat['user']}")
            st.markdown(f"**Assistant:** {chat['bot']}")

if __name__ == "__main__":
    main()