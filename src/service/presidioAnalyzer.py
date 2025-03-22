from presidio_analyzer import AnalyzerEngine # type: ignore
from presidio_analyzer.nlp_engine import NlpEngineProvider # type: ignore

class PresidioAnalyzer:
    def __init__(self,entities_to_ignore=["NRP"]):
        self.presidio_config = configuration = {
            "nlp_engine_name": "spacy",
            "models": [
                {"lang_code": "en", "model_name": "en_core_web_lg"},
            ],
        }
        self.nlp_engine_provider = NlpEngineProvider(nlp_configuration=self.presidio_config)
        self.nlp_engine = self.nlp_engine_provider.create_engine()
        self.analyzer = AnalyzerEngine(
            nlp_engine=self.nlp_engine, 
            supported_languages=["en"], 
            default_score_threshold=0.75
        )
        self.entities_to_ignore = entities_to_ignore


    def analyze(self, text):
        analyzer_results = self.analyzer.analyze(text=text, language="en")
        filtered_results = [result for result in analyzer_results if result.entity_type not in self.entities_to_ignore]
        return filtered_results
