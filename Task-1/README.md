# Task 1: Chat with PDF Using RAG Pipeline

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that enables users to interact with semi-structured data from PDF files. It processes PDF files, extracts data, converts the content into vector embeddings, and allows the system to answer user queries and comparisons based on the retrieved information.

## Overview

The goal of this task is to allow users to upload PDF files and interact with the data they contain. The system extracts relevant information, stores it as embeddings in a vector database, and uses a pre-trained Large Language Model (LLM) to generate responses based on the user’s query. This includes handling specific queries like retrieving detailed data from specific sections of the PDF or comparing data from different files.

---

## Functional Requirements

### 1. Data Ingestion
- **Input**: PDF files containing semi-structured data.
- **Process**:
  - Extract text and relevant structured information from PDF files.
  - Segment data into logical chunks for better granularity.
  - Convert chunks into vector embeddings using a pre-trained embedding model.
  - Store embeddings in a vector database for efficient similarity-based retrieval.

### 2. Query Handling
- **Input**: User's natural language question.
- **Process**:
  - Convert the user's query into vector embeddings using the same embedding model.
  - Perform a similarity search in the vector database to retrieve the most relevant chunks.
  - Pass the retrieved chunks to the LLM along with a prompt or agentic context to generate a detailed response.

### 3. Comparison Queries
- **Input**: User's query asking for a comparison.
- **Process**:
  - Identify and extract the relevant terms or fields to compare across multiple PDF files.
  - Retrieve the corresponding chunks from the vector database.
  - Process and aggregate data for comparison.
  - Generate a structured response (e.g., tabular or bullet-point format).

### 4. Response Generation
- **Input**: Relevant information retrieved from the vector database and the user query.
- **Process**:
  - Use the LLM with retrieval-augmented prompts to produce responses with exact values and context.
  - Ensure factuality by incorporating retrieved data directly into the response.

---

## Example Data

The following PDF file is used for testing and data extraction:

- **[Example PDF: Tables, Charts, and Graphs with Examples](https://www.hunter.cuny.edu/dolciani/pdf_files/workshop-materials/mmcpresentations/tables-charts-and-graphs-with-examples-from.pdf)**

---

## Specific Tasks to be Performed

1. **From page 2**:
   - Extract the unemployment information based on the type of degree input.

2. **From page 6**:
   - Extract and display tabular data for user queries.

---
