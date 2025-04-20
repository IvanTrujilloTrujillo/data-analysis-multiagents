# Entry point to launch the Data Analysis Chatbot application

import os
import sys
import subprocess


def main() -> None:
    """
    Main entry point for running the Data Analysis Chatbot application.
    This script launches the Streamlit UI.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    streamlit_app_path = os.path.join(current_dir, "src", "ui", "streamlit_app.py")

    if not os.path.exists(streamlit_app_path):
        print(f"Error: Could not find the Streamlit app at {streamlit_app_path}")
        sys.exit(1)

    print("Starting Data Analysis Chatbot...")
    print("Loading Streamlit interface...")

    try:
        subprocess.run(["streamlit", "run", streamlit_app_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit app: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: Streamlit not found. Please make sure Streamlit is installed.")
        print("You can install it with: pip install streamlit")
        sys.exit(1)


if __name__ == "__main__":
    main()