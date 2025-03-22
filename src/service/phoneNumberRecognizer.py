from service.__init__ import *
import phonenumbers
from phonenumbers import PhoneNumberMatcher
import re

class PhoneNumberRecognizer:

    @staticmethod
    def analyze(text):
        phone_numbers = set()
        for match in PhoneNumberMatcher(text,None):
            phone_numbers.add(match.raw_string)  

        # For numbers without country codes
        local_number_pattern = r'\b\d{10}\b'  
        for match in re.finditer(local_number_pattern, text):
            phone_numbers.add(match.group())
        
        results = []
        for phone_number in phone_numbers:
            escaped_number = re.escape(phone_number)
            escaped_number = escaped_number.replace(r'\ ', r'\s*')

            for match in re.finditer(escaped_number,text):
                results.append({
                    "start" : match.start(),
                    "end" : match.end()
                })
        
        return ResultMapper.library_to_presidio(results=results,confidence_score=1.0,entity_type="PHONE_NUMBER")
