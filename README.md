# Blood Test Report Analyzer

A FastAPI-based application that uses AI agents to analyze blood test reports and provide comprehensive health insights, nutritional recommendations, and exercise plans.

## Features

- **PDF Blood Test Report Analysis**: Upload and analyze blood test reports in PDF format
- **AI-Powered Medical Insights**: Get detailed analysis of blood test results using AI agents
- **Nutritional Recommendations**: Receive personalized nutrition advice based on blood test results
- **Exercise Planning**: Get safe and effective exercise recommendations
- **Professional Medical Analysis**: Evidence-based recommendations from specialized AI agents

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (or other LLM provider)
- PDF blood test reports to analyze

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd blood-test-analyser-debug
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp env_example.txt .env
   
   # Edit .env and add your API keys
   # OPENAI_API_KEY=your_actual_openai_api_key
   ```

4. **Create necessary directories**
   ```bash
   mkdir -p data outputs
   ```

## Usage

### Running the Application

1. **Start the FastAPI server**
   ```bash
   python main.py
   ```

2. **Access the API**
   - API will be available at: `http://localhost:8000`
   - Interactive docs: `http://localhost:8000/docs`
   - Health check: `http://localhost:8000/`

### API Endpoints

#### POST `/analyze`
Analyze a blood test report PDF file.

**Parameters:**
- `file`: PDF file (required)
- `query`: Analysis query (optional, default: "Summarise my Blood Test Report")

**Example using curl:**
```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@path/to/your/blood_test.pdf" \
  -F "query=Analyze my blood test results and provide recommendations"
```

**Example using Python requests:**
```python
import requests

url = "http://localhost:8000/analyze"
files = {"file": open("blood_test.pdf", "rb")}
data = {"query": "Analyze my blood test results"}

response = requests.post(url, files=files, data=data)
print(response.json())
```

## Project Structure

```
blood-test-analyser-debug/
├── main.py              # FastAPI application entry point
├── agents.py            # AI agent definitions
├── task.py              # Task definitions for agents
├── tools.py             # Custom tools for PDF processing
├── requirements.txt     # Python dependencies
├── env_example.txt      # Environment variables template
├── README.md           # This file
├── data/               # Directory for uploaded PDF files
├── outputs/            # Directory for analysis outputs
└── .env               # Environment variables (create from env_example.txt)
```

## AI Agents

The application uses specialized AI agents:

1. **Doctor Agent**: Primary medical analysis and interpretation
2. **Verifier Agent**: Validates blood test report completeness
3. **Nutritionist Agent**: Provides nutritional recommendations
4. **Exercise Specialist Agent**: Creates exercise plans

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `SERPER_API_KEY`: Serper API key for web search (optional)

### LLM Configuration

The application supports multiple LLM providers. Currently configured for OpenAI, but can be extended to support:
- Google AI
- Anthropic Claude
- Local models

## Error Handling

The application includes comprehensive error handling for:
- Invalid file formats (only PDF supported)
- Missing API keys
- PDF processing errors
- Network connectivity issues

## Security Considerations

- Uploaded files are automatically cleaned up after processing
- API keys are stored in environment variables
- File validation prevents malicious uploads
- Temporary files use unique UUIDs to prevent conflicts

## Troubleshooting

### Common Issues

1. **"Error reading PDF file"**
   - Ensure the PDF is not corrupted
   - Check if the PDF contains text (not just images)
   - Verify file permissions

2. **"Error processing blood report"**
   - Check your API key is valid
   - Ensure internet connectivity
   - Verify the PDF is a blood test report

3. **Import errors**
   - Run `pip install -r requirements.txt`
   - Check Python version (3.8+ required)

### Debug Mode

To run in debug mode with more verbose output:
```bash
python main.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Disclaimer

This application is for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical decisions.
