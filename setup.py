from setuptools import setup, find_packages

VERSION = "0.2.0"
DESCRIPTION = "Embedding Server"
LONG_DESCRIPTION = "Drop in replacement for OpenAI's embedding API. Can be used with official OpenAPI libraries"

# Setting up
setup(
    name="embedding_server",
    version=VERSION,
    author="Tosh San",
    author_email="santosh@sahoo.xyz",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["fastapi", "sentence-transformers", "uvicorn"],
    keywords=["python", "embeddings", "fastapi", "openai", "pytorch", "transformers"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    package_data={'embedding-server': ['bin/server']},
    scripts=['embedding_server/bin/server']
)
