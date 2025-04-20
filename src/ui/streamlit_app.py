# Streamlit app for the Data Analysis Chatbot

import os
import streamlit as st
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.backend.main import DataAnalysisBot


st.set_page_config(
    page_title="Data Analysis Chatbot",
    page_icon="📊",
    layout="wide",
)


if "bot" not in st.session_state:
    st.session_state.bot = DataAnalysisBot()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "dataframe" not in st.session_state:
    st.session_state.dataframe = None
if "file_info" not in st.session_state:
    st.session_state.file_info = None


def handle_file_upload() -> None:
    """Handle file upload and process it with the bot."""
    uploaded_file = st.session_state.uploaded_file
    if uploaded_file is not None:
        file_content = uploaded_file.getvalue()

        file_info = st.session_state.bot.load_csv(uploaded_file, uploaded_file.name)

        st.session_state.file_info = file_info
        st.session_state.dataframe = st.session_state.bot.current_dataframe

        st.session_state.messages.append({"role": "system", "content": f"CSV file '{uploaded_file.name}' has been loaded."})


def handle_chat_input() -> None:
    """Handle user input and send it to the bot."""
    user_message = st.session_state.user_input
    if user_message:
        st.session_state.messages.append({"role": "user", "content": user_message})

        bot_response = st.session_state.bot.chat(user_message)

        st.session_state.messages.append({"role": "assistant", "content": bot_response})


def main() -> None:
    """Main function to run the Streamlit app."""
    st.title("Data Analysis Chatbot")
    st.markdown("""
    Upload a CSV file and chat with the AI to analyze your data.
    """)

    col1, col2 = st.columns([2, 3])

    # Left column: File upload and data preview
    with col1:
        st.subheader("Upload Data")
        st.file_uploader(
            "Upload a CSV file", 
            type=["csv"], 
            key="uploaded_file",
            on_change=handle_file_upload
        )

        if st.session_state.file_info:
            with st.expander("File Information", expanded=True):
                st.text(st.session_state.file_info)

        if st.session_state.dataframe is not None:
            st.subheader("Data Preview")
            st.dataframe(st.session_state.dataframe.head(10), use_container_width=True)

    # Right column: Chat interface
    with col2:
        st.subheader("Chat with the AI")

        chat_container = st.container(height=500)
        with chat_container:
            for message in st.session_state.messages:
                if message["role"] == "user":
                    st.chat_message("user").write(message["content"])
                elif message["role"] == "assistant":
                    st.chat_message("assistant").write(message["content"])
                elif message["role"] == "system":
                    st.chat_message("system").write(message["content"])

        st.chat_input(
            "Ask a question about your data...",
            key="user_input",
            on_submit=handle_chat_input,
            disabled=st.session_state.dataframe is None
        )

        if st.session_state.dataframe is None:
            st.info("Please upload a CSV file to start chatting.")
        else:
            st.markdown("""
            **Example questions you can ask:**
            - Summarize this dataset
            - What are the main statistics for column X?
            - Are there any missing values?
            - Show me the correlation between X and Y
            - What insights can you provide about this data?
            """)


if __name__ == "__main__":
    main()
