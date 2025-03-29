from presidio_analyzer import Pattern, PatternRecognizer

patterns = [
    Pattern(name="PAN_NUMBER", regex=r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b", score=0.90),
    Pattern(name="AADHAAR_NUMBER", regex=r"\b\d{4}[- ]?\d{4}[- ]?\d{4}\b(?!\d)", score=0.90),
    Pattern(
        name="CREDIT_CARD_NUMBER",
        regex=r"\b(?:4[0-9]{12}(?:[0-9]{3})?|(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|6(?:011|5[0-9]{2})[0-9]{12}|(?:2131|1800|35\d{3})\d{11})\b",
        score=0.90
    ),
]

uin_recognizer = PatternRecognizer(patterns=patterns[0:2], supported_entity="UIN")
credit_card_recognizer = PatternRecognizer(patterns=[patterns[2]], supported_entity="CREDIT_CARD")
