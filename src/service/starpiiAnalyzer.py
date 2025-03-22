from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
from service.__init__ import *

class StarPIIAnalyzer:

    def __init__(self):
        self.model_path = r"../models/starpii"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModelForTokenClassification.from_pretrained(self.model_path)
        self.pipe = pipeline("token-classification", model=self.model, tokenizer=self.tokenizer, aggregation_strategy="simple")

    
    def analyze(self,text):
        starpii_results = self.pipe(text)
        results = ResultMapper.model_to_presidio(starpii_results)
        return results