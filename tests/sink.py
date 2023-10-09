import openai
import faiss

openai.api_key = "YOUR_KEY"
openai.api_base = "http://localhost:8080/v1"

embeddings = openai.Embedding.create(
    input="The food was delicious and the waiter...", model="all-MiniLM-L6-v2"
)

print(embeddings)

# make faiss available
index = faiss.IndexFlatL2(d)  # build the index, d=size of vectors
# here we assume xb contains a n-by-d numpy matrix of type float32
index.add(xb)  # add vectors to the index
print(index.ntotal)
