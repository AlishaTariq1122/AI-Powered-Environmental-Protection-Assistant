from flask import Flask, render_template, request, jsonify
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq
import os

app = Flask(__name__)

# Initialize RAG system with better settings
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Groq(model="llama3-70b-8192", api_key="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")

# Load documents and create index with better settings
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(
    documents,
    show_progress=True
)

# Create a more sophisticated query engine
query_engine = index.as_query_engine(
    similarity_top_k=3,
    response_mode="tree_summarize",
    streaming=False
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    try:
        # Enhance the query with context about environmental protection
        enhanced_query = f"""
        You are an environmental protection assistant. Please provide detailed information from the documents about:
        {user_message}
        
        Include specific details, regulations, and relevant information. If the information is spread across multiple documents, 
        combine the information in a coherent way. Make sure to cite the specific document names when providing information.
        """
        
        response = query_engine.query(enhanced_query)
        return jsonify({'response': str(response)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 