# Data Analysis Multi-Agents

A chatbot application that allows users to upload CSV files and chat with an AI to analyze the data.

## Features

- Upload and analyze CSV files
- Chat with an AI assistant about your data
- Get insights, statistics, and visualizations
- User-friendly Streamlit interface

## Architecture

The application consists of two main components:

1. **Backend**: A LangChain-based chatbot that can process and analyze CSV data
2. **Frontend**: A Streamlit UI for file upload and chat interaction

## Installation

### Prerequisites

- Python 3.10 or higher
- OpenAI API key

### Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd data-analysis-multiagents
   ```

2. Install dependencies using pipenv:
   ```
   pipenv install
   ```

3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

### Running Locally

1. Activate the virtual environment:
   ```
   pipenv shell
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open your browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

4. Upload a CSV file using the file uploader

5. Chat with the AI about your data:
   - Ask for summaries and statistics
   - Request specific analyses
   - Get insights about patterns and correlations

### Using Docker

1. Build the Docker image:
   ```
   docker build -t data-analysis-chatbot .
   ```

2. Run the container with your OpenAI API key:
   ```
   docker run -p 8501:8501 -e OPENAI_API_KEY=your_api_key_here data-analysis-chatbot
   ```

3. Open your browser and navigate to http://localhost:8501

4. Use the application as described above

## Example Questions

Once you've uploaded a CSV file, you can ask questions like:

- "Summarize this dataset"
- "What are the main statistics for column X?"
- "Are there any missing values?"
- "Show me the correlation between X and Y"
- "What insights can you provide about this data?"

## Development

### Project Structure

```
data-analysis-multiagents/
├── src/
│   ├── backend/
│   │   ├── __init__.py
│   │   └── main.py            # Backend chatbot implementation
│   ├── ui/
│   │   ├── __init__.py
│   │   └── streamlit_app.py   # Streamlit UI implementation
│   └── __init__.py
├── .dockerignore              # Files to exclude from Docker image
├── .gitignore                 # Files to exclude from Git
├── app.py                     # Main entry point
├── Dockerfile                 # Docker configuration
├── LICENSE
├── Pipfile                    # Dependencies
├── Pipfile.lock
├── pyproject.toml             # Project configuration including ruff
├── setup.py                   # Python package information
├── version.py                 # Python script with app version
└── README.md
```

### Code Quality

This project uses [ruff](https://github.com/charliermarsh/ruff) for linting and code quality checks. Ruff is a fast Python linter written in Rust that combines the functionality of multiple Python linters.

#### Running Ruff

To run ruff on the project:

```bash
# Install ruff if not already installed
pip install ruff

# Run format
ruff format

# Run linting with auto-fix
ruff check --fix
```

#### Ruff Configuration

The ruff configuration is defined in `pyproject.toml` and includes:

- PEP 8 style checking
- Import sorting
- Docstring validation (Google style)
- Security checks
- Type annotation checks
- And more

See the `pyproject.toml` file for the complete configuration.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
