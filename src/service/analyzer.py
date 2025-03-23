from recognizers.creditCardRecognizer import CreditCardRecognizer
from recognizers.locationRecognizer import LocationRecognizer
from recognizers.phoneNumberRecognizer import PhoneNumberRecognizer
from service.starpiiAnalyzer import StarPIIAnalyzer

class Analyzer:
    def __init__(self):
        self.starpii_analyzer = StarPIIAnalyzer()

    
    def analyze(self,text):
        results = self.starpii_analyzer.analyze(text)
        results.extend(LocationRecognizer.analyze(text))
        results.extend(PhoneNumberRecognizer.analyze(text))
        results.extend(CreditCardRecognizer.analyze(text))

        entity_wise_words = dict()
        for result in results:
            if result.entity_type in entity_wise_words:
                entity_wise_words[result.entity_type].append(text[result.start:result.end])
            else:
                entity_wise_words[result.entity_type] = [text[result.start:result.end]]

        return entity_wise_words
        

        