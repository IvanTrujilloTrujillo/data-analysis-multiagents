"""Entry point to launch the Data Analysis Chatbot application."""

import os
import shutil
import subprocess
import sys


def main() -> None:
    """Main entry point for running the Data Analysis Chatbot application.

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
        streamlit_path = shutil.which("streamlit")
        if streamlit_path is None:
            print("Error: Streamlit not found. "
                  "Please make sure Streamlit is installed.")
            print("You can install it with: pip install streamlit")
            sys.exit(1)

        if not os.path.isfile(streamlit_path):
            print(f"Error: Invalid streamlit executable path: {streamlit_path}")
            sys.exit(1)

        subprocess.run(  # noqa: S603
            [streamlit_path, "run", streamlit_app_path],
            check=True,
            shell=False
        )
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit app: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
