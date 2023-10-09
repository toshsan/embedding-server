class TestCompat:
    def test_openaicompat(self):
        import openai

        openai.api_key = "YOUR_KEY"
        openai.api_base = "http://localhost:8080/v1"

        response = openai.Embedding.create(
            input="The food was delicious and the waiter...", model="all-MiniLM-L6-v2"
        )
        embeddings = response["data"][0]["embedding"]

        assert embeddings
