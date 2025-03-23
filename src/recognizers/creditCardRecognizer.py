import re
from service.__init__ import *

class CreditCardRecognizer:

    @staticmethod
    def verify_using_luhn(credit_card_number):
        credit_card_number = credit_card_number.replace(" ","").replace("-","")
        reversed_number = credit_card_number[::-1]
        digits = [int(digit) for digit in reversed_number]
        check_sum = 0

        for index,number in enumerate(digits):
            if index%2 == 1:
                number *= 2
                if number > 9:
                    number -= 9
            check_sum += number

        return check_sum % 10 == 0



    @staticmethod
    def analyze(text):
        credit_card_regex = r'\b(?:\d[ -]*?){13,19}\b'
        credit_card_numbers = set(re.findall(credit_card_regex,text))
        valid_credit_card_numbers = [number for number in credit_card_numbers if CreditCardRecognizer.verify_using_luhn(number)]

        results = []
        for credit_card_number in valid_credit_card_numbers:
            for match in re.finditer(r'\b' + re.escape(credit_card_number) + r'\b', text):
                results.append({
                    "start": match.start(),
                    "end": match.end()
                })
        
        return ResultMapper.library_to_presidio(results=results,confidence_score=1.0,entity_type="CREDIT_CARD_NUMBER")