from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer
import numpy as np
import openai
from sklearn.metrics.pairwise import cosine_similarity

# Set your OpenAI API key here
openai.api_key = "" # enter your api key

# Initialize Flask
app = Flask(__name__)

# Step 1: Crawl and Scrape Website Content
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    texts = [p.text for p in soup.find_all('p')]
    return texts

# Step 2: Convert Content to Embeddings
def create_embeddings(texts, model_name='sentence-transformers/all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(texts)
    return embeddings, texts

# Step 3: Query the Embedding Database Using Cosine Similarity
def query_embeddings(query, embeddings, texts, embedding_model):
    query_embedding = embedding_model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)
    sorted_indices = np.argsort(similarities[0])[::-1]  # Sort by highest similarity
    top_k = 5
    results = [texts[idx] for idx in sorted_indices[:top_k]]
    return results

# Step 4: Generate a Response using OpenAI API
def generate_response(context, query):
    prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Main Pipeline
def rag_pipeline(url, user_query):
    # Step 1: Scrape the website
    scraped_texts = scrape_website(url)

    # Step 2: Create embeddings
    embedding_model_name = 'sentence-transformers/all-MiniLM-L6-v2'
    embeddings, texts = create_embeddings(scraped_texts, embedding_model_name)

    # Step 3: Query the embeddings using cosine similarity
    embedding_model = SentenceTransformer(embedding_model_name)
    relevant_contexts = query_embeddings(user_query, np.array(embeddings), texts, embedding_model)
    context = "\n".join(relevant_contexts)

    # Step 4: Generate a response
    response = generate_response(context, user_query)

    return response

# Flask route for handling user query
@app.route('/ask', methods=['POST'])
def ask():
    website_url = request.form['website']
    user_query = request.form['query']

    # Run the RAG pipeline
    answer = rag_pipeline(website_url, user_query)
    
    return jsonify({"answer": answer})

# Flask route for serving the HTML page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
