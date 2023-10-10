import logging
import time
from typing import Optional
from sentence_transformers import SentenceTransformer
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, Field
import os

MODEL_NAME = os.getenv("MODEL", "all-MiniLM-L6-v2")
AUTH = f"Bearer {os.getenv('KEY', 'YOUR_KEY')}"

model = SentenceTransformer(MODEL_NAME)
app = FastAPI()
logger = logging.getLogger(__name__)


class EmbeddingBody(BaseModel):
    input: str = Field(description="Your text string goes here")
    model: str | None = Field(
        default=None, title="model name. not in use", max_length=300
    )


@app.post(
    "/v1/embeddings",
)
async def root(body: EmbeddingBody, Authorization: Optional[str] = Header(None)):
    if AUTH != Authorization:
        raise HTTPException(
            status_code=401,
            detail="Authroization: Bearer YOUR_KEY must be provided",
        )

    sentences = [body.input]
    start = time.time()

    embeddings = model.encode(sentences)
    logger.info("%s took %f", body.input, time.time() - start)

    return {
        "data": [
            {
                "embedding": embeddings[0].tolist(),
                "index": 0,
                "object": "embedding",
            }
        ],
        "model": MODEL_NAME,
        "object": "list",
        "usage": {"prompt_tokens": 0, "total_tokens": 0},
    }
