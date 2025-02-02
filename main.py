from src.decomposer import TaskDecomposer
from src.utils import create_project_structure, format_model_recommendation
import json

def main():
    # Create necessary directories
    create_project_structure()
    
    # Initialize decomposer
    decomposer = TaskDecomposer()
    
    # Get user input
    company_name = input("Enter company name: ")
    service = input("Enter main service: ")
    max_models = 3  # Hardcoded as specified
    
    # Analyze and get tasks
    tasks = decomposer.analyze_business(company_name, service, max_models)
    
    # Load config for recommendations
    with open('config/model_config.json', 'r') as f:
        config = json.load(f)
    
    # Get model recommendations
    recommendations = format_model_recommendation(tasks, config)
    
    # Display results
    print("\nTask Analysis and Model Recommendations:")
    print("-" * 50)
    for rec in recommendations:
        print(f"\nTask: {rec['task']}")
        print(f"Recommended Model: {rec['recommended_model']}")
        print(f"Model Size: {rec['model_size']}")
        print(f"Description: {rec['description']}")

if __name__ == "__main__":
    main()
