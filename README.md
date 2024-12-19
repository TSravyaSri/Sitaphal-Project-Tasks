To describe the tasks in Sitafal (a framework or platform, if you mean something specific), here's an overview of how each task can be broken down in terms of their functionalities:

Task 1: Chat with PDF Using RAG Pipeline
In Sitafal, you would implement the Retrieval-Augmented Generation (RAG) pipeline for processing semi-structured data within PDFs. The functional flow can be as follows:

1. Data Ingestion
Process: Extract text from PDF files (e.g., tables, charts, and graphs). Break down the content into smaller chunks for easier access and relevance. Use a pre-trained embedding model to generate vector embeddings from these chunks. Store the embeddings in a vector database for efficient retrieval.
2. Query Handling
Process: When a user asks a question, their query is also converted into vector embeddings using the same model. A similarity search is conducted within the vector database to retrieve the most relevant chunks. These chunks are then passed to an LLM (Language Model) for response generation, augmented with the extracted data.
3. Comparison Queries
Process: For comparison-based queries, the system identifies the relevant fields or terms from multiple PDF files. It aggregates the data, compares it, and presents the results in a structured format (tabular or bullet points).
4. Response Generation
Process: Using the retrieved data and the user's query, the system generates a context-rich, factual response using the LLM, ensuring that the response is accurate and relevant.
Example PDF Data:

From page 2, extract unemployment information based on the degree type.
From page 6, extract tabular data.
Task 2: Chat with Website Using RAG Pipeline
The goal for the website RAG pipeline is similar: scrape, store, and generate responses based on the extracted content from websites.

1. Data Ingestion
Process: Use crawlers to scrape content from target websites (e.g., University pages like UChicago, Stanford). Extract relevant fields, metadata, and textual content. Segment this information into chunks and convert them into vector embeddings for efficient search and retrieval.
2. Query Handling
Process: Convert the user’s query into vector embeddings. Perform a similarity search in the vector database to retrieve the most relevant content from the scraped websites. Use the LLM to generate a response by augmenting it with the relevant context from the retrieved data.
3. Response Generation
Process: After retrieving the relevant information from the vector database, the system generates a response that is factually accurate and provides detailed context from the websites.
Example Websites:

UChicago: https://www.uchicago.edu/
Stanford: https://www.stanford.edu/
Washington: https://www.washington.edu/
UND: https://und.edu/
In Sitafal, you can implement these pipelines to efficiently process and query structured and unstructured data, enhancing user interactions by delivering context-aware, fact-based responses.
