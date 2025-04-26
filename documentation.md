# AI-Powered Environment Protection Assistant

## Overview
The AI-Powered Environment Protection Assistant is a web-based application that provides information and guidance on environmental regulations and protection measures. It uses advanced AI technology to process and respond to queries about environmental laws, regulations, and best practices.

## Features
- Real-time chat interface for environmental queries
- Access to comprehensive environmental regulations
- Quick access to common environmental topics
- Dark/Light mode support
- Responsive design for all devices
- Secure API integration

## Technical Stack
- **Backend**: Python Flask
- **AI Framework**: LlamaIndex
- **Language Model**: Groq (llama3-70b-8192)
- **Embedding Model**: BAAI/bge-base-en-v1.5
- **Frontend**: HTML5, CSS3, JavaScript
- **UI Framework**: Bootstrap 5
- **Icons**: Font Awesome 6

## Project Structure
```
.
├── app.py                 # Main Flask application
├── templates/             # Frontend templates
│   └── index.html        # Main chat interface
├── data/                  # Environmental regulation documents
│   ├── punjab-bio-safety-rules-2014-pdf3.pdf
│   ├── PUNJAB_ENVIRONMENTAL_PROTECTION_RULES_2017.pdf
│   ├── Plastic Regulations-2023.pdf
│   ├── Gazette Notification regarding amendments to the Plastic Regulations, 2023.pdf
│   └── SMOG-Regulation_compressed.pdf
└── .venv/                 # Python virtual environment
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup
1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install flask llama-index-core llama-index-llms-groq llama-index-embeddings-huggingface
   ```
4. Set up environment variables:
   ```bash
   export GROQ_API_KEY="your_api_key_here"  # On Windows: set GROQ_API_KEY=your_api_key_here
   ```

## Usage

### Running the Application
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

### Using the Chat Interface
1. Type your environmental query in the input field
2. Press Enter or click the send button
3. View the AI-generated response
4. Use suggested questions for quick access to common topics
5. Toggle between dark and light mode using the theme button

## Available Topics
The assistant can provide information on:
- Plastic waste management regulations
- Air quality standards and smog regulations
- Biosafety rules and guidelines
- Environmental protection laws
- Delegation of powers for environmental approvals

## API Endpoints

### GET /
- Renders the main chat interface
- No parameters required

### POST /chat
- Handles chat messages
- Request body: `{"message": "your query here"}`
- Response: `{"response": "AI response here"}`

## Customization

### Adding New Documents
1. Place new PDF documents in the `data/` directory
2. Restart the Flask server to update the knowledge base

### Modifying the UI
- Edit `templates/index.html` for frontend changes
- CSS styles are included in the HTML file
- JavaScript functionality is included in the HTML file

## Security Considerations
- API keys should be stored securely
- Input validation is implemented
- Error handling is in place
- HTTPS should be used in production

## Performance Optimization
- Document indexing is done at startup
- Caching is implemented for faster responses
- Responsive design for optimal performance on all devices

## Troubleshooting

### Common Issues
1. **API Key Errors**
   - Ensure the GROQ_API_KEY is set correctly
   - Check for any typos in the API key

2. **Document Loading Issues**
   - Verify PDF files are not corrupted
   - Check file permissions
   - Ensure documents are in the correct directory

3. **Server Connection Issues**
   - Check if the Flask server is running
   - Verify port 5000 is not blocked
   - Check network connectivity

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
Alisha Tariq

## Acknowledgments
- LlamaIndex for the RAG framework
- Groq for the language model
- BAAI for the embedding model
- All contributors to the environmental regulation documents 