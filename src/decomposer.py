from .model_manager import ModelManager
import torch

class TaskDecomposer:
    def __init__(self):
        self.model_manager = ModelManager()
        self.analyzer, self.tokenizer = self.model_manager.load_task_analyzer()
        
    def analyze_business(self, company_name, service, max_models=3):
        prompt = self._create_analysis_prompt(company_name, service)
        
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True)
        
        # Add generation configuration
        outputs = self.analyzer.generate(
            inputs["input_ids"],
            max_length=200,
            do_sample=True,  # Enable sampling
            temperature=0.7,
            pad_token_id=self.tokenizer.eos_token_id,
            attention_mask=inputs["attention_mask"],  # Add attention mask
        )
        
        analysis = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return self._parse_tasks(analysis, max_models)

    


    def _create_analysis_prompt(self, company_name, service):
        return f"""
        Company: {company_name}
        Main Service: {service}
        
        Analyze and break down the main service into essential sub-processes. 
        Format: Process: [process name] - Description: [brief description]
        """
    
    def _parse_tasks(self, analysis, max_models):
        # Simple parsing logic - can be enhanced based on needs
        tasks = []
        lines = analysis.split('\n')
        for line in lines:
            if line.strip().startswith('Process:'):
                task = line.split('-')[0].replace('Process:', '').strip()
                tasks.append(task)
                if len(tasks) >= max_models:
                    break
        return tasks
