import uvicorn
import os
from embedding_server.server import app


def main():
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
    )


if __name__ == "__main__":
    main()
