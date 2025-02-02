import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import json
import os

class ModelManager:
    def __init__(self):
        self.config = self._load_config()
        self.models = {}
        self.tokenizers = {}
        
    def _load_config(self):
        with open('config/model_config.json', 'r') as f:
            return json.load(f)
    
def load_task_analyzer(self):
    model_name = self.config["task_analyzer"]["model"]
    if "task_analyzer" not in self.models:
        # Change to float32 for CPU compatibility
        self.models["task_analyzer"] = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float32,  # Changed from float16
            low_cpu_mem_usage=True
        )
        self.tokenizers["task_analyzer"] = AutoTokenizer.from_pretrained(model_name)
    
    return self.models["task_analyzer"], self.tokenizers["task_analyzer"]

    def load_specialized_model(self, task_type):
        if task_type not in self.models:
            model_info = self.config["specialized_models"][task_type]
            self.models[task_type] = AutoModelForCausalLM.from_pretrained(
                model_info["model"],
                torch_dtype=torch.float16,
                low_cpu_mem_usage=True
            )
            self.tokenizers[task_type] = AutoTokenizer.from_pretrained(model_info["model"])
        
        return self.models[task_type], self.tokenizers[task_type]
