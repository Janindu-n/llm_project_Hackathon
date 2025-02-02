


Website (Wireframe): https://live-puma.10web.me/ 

# optimAIze


![optimAIze Logo](../optimAIze.png "OptimAIze Logo")

optimAIze is a plug-and-play AI platform designed to help businesses decompose their core services into specific, manageable subprocesses and recommend specialized, lightweight language models (LLMs) for each subtask. The system is ideal for small businesses looking for a cost-effective and privacy-preserving solution to automate operations like email marketing, contract drafting, analytical report generation, and more.

## Features

- **Task Decomposition:** Break down a business's main service into 3 distinct subprocesses using an advanced task analyzer.
- **Custom Model Mapping:** Automatically map each subtask to a specialized LLM optimized for that function.
- **Local Deployment:** Run all models locally on your Mac using CPU-based optimizations.
- **Modular Architecture:** Easily extend and customize the platform for additional business domains and more LLMs.

## Project Structure

```plaintext
optimAIze/
├── config/
│   └── model_config.json         # Configuration for task analyzer and specialized models
├── models/
│   ├── task_analyzer/            # Directory for downloaded task analyzer model
│   └── specialized/              # Directory for specialized subtask models
├── src/
│   ├── __init__.py
│   ├── decomposer.py             # Module for decomposing business services into subprocesses
│   ├── model_manager.py          # Module for downloading and managing models
│   └── utils.py                  # Utility functions (e.g., project structure creation, formatting)
├── main.py                       # Entry point for the application
└── requirements.txt              # Python dependencies
```

## Installation

### Prerequisites

- macOS with an Intel processor
- Python 3.10 (managed via pyenv recommended)
- Git

### Setup Steps

1. **Clone the Repository**  
   Clone or download the optimAIze repository to your local machine.

2. **Setup Python Environment**  
   Open your terminal and navigate to the project directory:
   ```bash
   cd optimAIze
   ```
   Create and activate a virtual environment:
   ```bash
   python -m venv llm_env
   source llm_env/bin/activate  # For zsh or bash on macOS
   ```

3. **Install Dependencies**  
   Install the required packages with:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Download the Latest Version of Transformers**  
   Since optimAIze uses the Microsoft Phi-2 model, install the latest version from GitHub:
   ```bash
   pip uninstall -y transformers
   pip install git+https://github.com/huggingface/transformers
   pip install einops
   ```

5. **Create the Necessary Project Structure**  
   If not already created, run the provided utility function to set up model directories:
   ```bash
   python -c "from src.utils import create_project_structure; create_project_structure()"
   ```

## Configuration

Adjust the configuration of the task analyzer and specialized models in the file:
`config/model_config.json`
```json
{
  "task_analyzer": {
    "model": "microsoft/phi-2",
    "max_length": 200,
    "temperature": 0.7,
    "do_sample": true
  },
  "specialized_models": {
    "process_analysis": {
      "model": "TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T",
      "description": "Process breakdown and analysis",
      "size": "1.1B"
    },
    "domain_specific": {
      "model": "facebook/opt-350m",
      "description": "Domain-specific task execution",
      "size": "350M"
    },
    "output_generation": {
      "model": "distilbert-base-uncased",
      "description": "Task-specific output generation",
      "size": "66M"
    }
  }
}
```
This JSON file maps the task analyzer and specialized models. Adjust models or parameters as necessary.

## Usage

Run the application by executing:

```bash
python main.py
```

Follow the on-screen prompts:
- **Company Name:** e.g., `OptimAIze`
- **Main Service:** e.g., `Marketing email generation`
- The system is currently configured to return 3 subprocess tasks along with recommendations for corresponding light-weight LLMs.

OptimAIze will analyze your input, break down the service into subprocesses, and display recommended models for each subtask, along with brief descriptions and model sizes.

## Troubleshooting

- **Model Loading Issues:**  
  If you encounter errors with model loading (such as key errors concerning Phi-2), ensure that:
  - You have installed the latest transformers from the GitHub repository.
  - The `einops` package is installed.
  - The configuration file (`config/model_config.json`) correctly specifies the models and includes `"trust_remote_code": true` where necessary.

- **NumPy Compatibility:**  
  If you see errors related to NumPy versions, downgrade to a compatible version by running:
  ```bash
  pip install numpy==1.24.3
  ```

## License

[MIT License](LICENSE)

## Contribution

Feel free to fork the repository and submit pull requests if you have improvements or additional features to contribute.

---

optimAIze is designed to simplify AI adoption for businesses by breaking down complex services into manageable, model-driven tasks. Enjoy optimizing your business operations with optimAIze!

---
Answer from Perplexity: pplx.ai/share
