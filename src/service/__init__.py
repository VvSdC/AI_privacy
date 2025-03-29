from presidio_analyzer import AnalyzerEngine,RecognizerRegistry
from presidio_analyzer.nlp_engine import NlpEngineProvider
from service.transformerRecognizer import TransformerRecognizer
from service.patternRecognizer import *
from config.starpii import STARPII_CONFIG
from config.ner import MULTILINGUAL_CONFIG

# Starpii 
starpii_model_path = r'../models/starpii'
starpii_recognizer = TransformerRecognizer(model_path=starpii_model_path,model_config=STARPII_CONFIG)

# Multilingual 
multilingual_model_path = r'../models/multilingual'
multilingual_recognizer = TransformerRecognizer(model_path=multilingual_model_path,model_config=MULTILINGUAL_CONFIG)

# Registry
registry = RecognizerRegistry()
registry.add_recognizer(starpii_recognizer)
registry.add_recognizer(multilingual_recognizer)
registry.add_recognizer(uin_recognizer)
registry.add_recognizer(credit_card_recognizer)
registry.add_recognizer(phone_number_recognizer)

# Presidio configuration
presidio_analyzer = AnalyzerEngine(registry=registry)