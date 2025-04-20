import os
from typing import List, Dict, Any, Optional
import pandas as pd
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI


load_dotenv()


class DataAnalysisBot:
    """
    A chatbot that can analyze CSV data and answer questions about it.
    """
    
    def __init__(self):
        """Initialize the chatbot with OpenAI model."""
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0,
        )
        self.conversation_history: List[Dict[str, Any]] = []
        self.current_dataframe: Optional[pd.DataFrame] = None
        self.dataframe_info: Optional[str] = None
    
    def load_csv(self, file_content, filename: str) -> str:
        """
        Load a CSV file into a pandas DataFrame.
        
        Args:
            file_content: The content of the CSV file
            filename: The name of the file
            
        Returns:
            A message about the loaded data
        """
        try:
            self.current_dataframe = pd.read_csv(file_content)
            
            # Generate information about the dataframe
            info_buffer = pd.io.StringIO()
            self.current_dataframe.info(buf=info_buffer)
            
            # Get basic statistics
            stats = self.current_dataframe.describe().to_string()
            
            # Create a comprehensive summary
            self.dataframe_info = (
                f"File '{filename}' loaded successfully.\n\n"
                f"Shape: {self.current_dataframe.shape[0]} rows, {self.current_dataframe.shape[1]} columns\n\n"
                f"Columns: {', '.join(self.current_dataframe.columns.tolist())}\n\n"
                f"Data Types:\n{self.current_dataframe.dtypes.to_string()}\n\n"
                f"Summary Statistics:\n{stats}"
            )
            
            # Add system message to conversation history
            self.conversation_history.append({
                "role": "system",
                "content": f"CSV file '{filename}' has been loaded. {self.current_dataframe.shape[0]} rows and {self.current_dataframe.shape[1]} columns."
            })
            
            return self.dataframe_info
            
        except Exception as e:
            error_message = f"Error loading CSV file: {str(e)}"
            self.conversation_history.append({
                "role": "system",
                "content": error_message
            })
            return error_message
    
    def chat(self, message: str) -> str:
        """
        Process a user message and return a response.
        
        Args:
            message: The user's message
            
        Returns:
            The chatbot's response
        """
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": message
        })
        
        # Prepare context for the LLM
        context = ""
        if self.current_dataframe is not None:
            # Add dataframe info to context
            context = f"The user has loaded a CSV file with the following information:\n{self.dataframe_info}\n\n"
            
            # For data-specific questions, add sample data
            if any(keyword in message.lower() for keyword in ["data", "csv", "file", "column", "row", "value", "analyze", "statistics"]):
                sample_data = self.current_dataframe.head(5).to_string()
                context += f"Here's a sample of the data (first 5 rows):\n{sample_data}\n\n"
        
        # Prepare messages for the LLM
        messages = [
            HumanMessage(content=f"{context}User question: {message}\n\nPlease provide a helpful response about the data.")
        ]
        
        # Get response from LLM
        response = self.llm.invoke(messages)
        
        # Add AI response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": response.content
        })
        
        return response.content
    
    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """
        Get the conversation history.
        
        Returns:
            The conversation history
        """
        # Filter out system messages for display
        return [msg for msg in self.conversation_history if msg["role"] in ["user", "assistant"]]