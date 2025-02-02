import os
import torch

def create_project_structure():
    directories = [
        'models/task_analyzer',
        'models/specialized',
        'config'
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def get_device():
    return "cuda" if torch.cuda.is_available() else "cpu"

def format_model_recommendation(tasks, config):
    recommendations = []
    specialized_models = config["specialized_models"]
    model_types = list(specialized_models.keys())
    
    for i, task in enumerate(tasks):
        model_type = model_types[i % len(model_types)]
        model_info = specialized_models[model_type]
        recommendations.append({
            "task": task,
            "recommended_model": model_info["model"],
            "model_size": model_info["size"],
            "description": model_info["description"]
        })
    return recommendations
