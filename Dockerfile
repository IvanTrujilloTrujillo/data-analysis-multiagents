FROM python:3.10-slim

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install

COPY . .

EXPOSE 8501

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Note: You need to provide your OpenAI API key when running the container
# Example: docker run -p 8501:8501 -e OPENAI_API_KEY=your-api-key data-analysis-chatbot

CMD ["pipenv", "run", "python", "app.py"]
