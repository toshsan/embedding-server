import openai

openai.api_key = "YOUR_KEY"
openai.api_base = "http://localhost:8080/v1"

embeddings = openai.Embedding.create(
    input="The food was delicious and the waiter...", model="all-MiniLM-L6-v2"
)

print(embeddings)
