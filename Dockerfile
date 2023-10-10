FROM python:3.11

ADD embedding_server/* /
ADD requirements.txt /

RUN python3 -m pip install -r requirements.txt
RUN python3 -c "import os; from sentence_transformers import SentenceTransformer; SentenceTransformer(os.getenv('MODEL', 'all-MiniLM-L6-v2'));"

EXPOSE 8000
ENTRYPOINT ["uvicorn", "server:app"]
