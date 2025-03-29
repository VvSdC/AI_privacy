from presidio_analyzer import EntityRecognizer,RecognizerResult
from transformers import pipeline,AutoTokenizer,AutoModelForTokenClassification

class TransformerRecognizer(EntityRecognizer):
    
    def __init__(self,model_path,model_config):
        super().__init__(supported_entities=model_config["SUPPORTED_ENTITIES"],supported_language="en")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForTokenClassification.from_pretrained(model_path)
        self.pipe = pipeline("token-classification",model=self.model,tokenizer=self.tokenizer,aggregation_strategy="simple")
        self.label_mapper = model_config["MODEL_TO_PRESIDIO_MAPPING"]
        self.model_threshold_score = model_config["MODEL_THRESHOLD_SCORE"]

    def analyze(self,text,entities,nlp_artifacts=None):
        results = []
        analyzer_results = self.pipe(text)

        for result in analyzer_results:
            entity_type = result['entity_group']

            if entity_type in self.supported_entities and result['score'] >= self.model_threshold_score:
                results.append(RecognizerResult(
                    entity_type=self.label_mapper[entity_type],
                    score=result['score'],
                    start=result['start'],
                    end=result['end']
                ))
        
        return results