from service.creditCardRecognizer import CreditCardRecognizer
from service.locationRecognizer import LocationRecognizer
from service.phoneNumberRecognizer import PhoneNumberRecognizer
from service.starpiiAnalyzer import StarPIIAnalyzer
from service.ipAddressRecognizer import IpAddressRecognizer

class Analyzer:
    def __init__(self):
        self.starpii_analyzer = StarPIIAnalyzer()

    
    def analyze(self,text):
        results = self.starpii_analyzer.analyze(text)
        results.extend(LocationRecognizer.analyze(text))
        results.extend(PhoneNumberRecognizer.analyze(text))
        results.extend(CreditCardRecognizer.analyze(text))
        results.extend(IpAddressRecognizer.analyze(text))
        return results

        