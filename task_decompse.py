from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class EmailTaskDecomposer:
    def __init__(self):
        self.task_analyzer = AutoModelForCausalLM.from_pretrained("microsoft/phi-2")
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2")
        
        # Define specialized models for each subtask
        self.specialized_models = {
            "subject_lines": {
                "model": "TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T",
                "description": "Optimized for short, engaging subject lines",
                "size": "1.1B parameters"
            },
            "email_body": {
                "model": "facebook/opt-350m",
                "description": "Specialized for email body content",
                "size": "350M parameters"
            },
            "call_to_action": {
                "model": "distilbert-base-uncased",
                "description": "Focused on conversion-oriented text",
                "size": "66M parameters"
            }
        }
