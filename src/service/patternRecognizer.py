from presidio_analyzer import Pattern, PatternRecognizer


# UIN patterns
uin_patterns = [
    Pattern(name="PAN_NUMBER", regex=r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b", score=0.90),
    Pattern(name="AADHAAR_NUMBER", regex=r"\b\d{4}[- ]?\d{4}[- ]?\d{4}\b(?!\d)", score=0.90),
]
uin_recognizer = PatternRecognizer(patterns=uin_patterns, supported_entity="UIN")


# Credit card patterns
credit_card_patterns = [
    Pattern(
        name="CREDIT_CARD_NUMBER",
        regex=r"\b(?:4[0-9]{12}(?:[0-9]{3})?|(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|6(?:011|5[0-9]{2})[0-9]{12}|(?:2131|1800|35\d{3})\d{11})\b",
        score=0.90
    )
]
credit_card_recognizer = PatternRecognizer(patterns=credit_card_patterns, supported_entity="CREDIT_CARD")


# Phone number patterns
phone_number_patterns = [
    # 1️⃣ International phone number (Requires at least 9 digits)
    Pattern(
        name="INTL_PHONE_NUMBER",
        regex=r"\+?[1-9]\d{0,2}[-. ]?\(?\d{2,4}\)?[-. ]?\d{2,4}[-. ]?\d{4,9}",
        score=0.90,
    ),

    # 2️⃣ US phone number (10-digit format with optional country code)
    Pattern(
        name="US_PHONE_NUMBER",
        regex=r"\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}",
        score=0.85,
    ),

    # 3️⃣ India phone number (10-digit format, starting with 6, 7, 8, or 9)
    Pattern(
        name="IN_PHONE_NUMBER",
        regex=r"\b[6789]\d{9}\b",
        score=0.85,
    ),

    # 4️⃣ UK phone number (Starting with +44 or 0, ensuring at least 10 digits)
    Pattern(
        name="UK_PHONE_NUMBER",
        regex=r"\+?44[-. ]?\d{3,4}[-. ]?\d{6,7}|\(?0\d{3,4}\)?[-. ]?\d{6,7}",
        score=0.85,
    ),
]

phone_number_recognizer = PatternRecognizer(patterns=phone_number_patterns,supported_entity="PHONE_NUMBER")



# Url patterns
url_patterns = [
    Pattern(
        name="STANDARD_URL",
        regex=r"\b(?:https?:\/\/)?(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}(?:\/[^\s]*)?\/?\b",
        score=0.90,
    ),
    Pattern(
        name="URL_WITH_QUERY",
        regex=r"\b(?:https?:\/\/)?(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}(?:\/[^\s]*)?\?(?:[^\s]*)?\b",
        score=0.85,
    ),
    Pattern(
        name="IP_URL",
        regex=r"\b(?:https?:\/\/)?(?:\d{1,3}\.){3}\d{1,3}(?:\/[^\s]*)?\/?\b",
        score=0.85,
    ),
    Pattern(
        name="URL_WITH_PORT",
        regex=r"\b(?:https?:\/\/)?(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}:\d{2,5}(?:\/[^\s]*)?\/?\b",
        score=0.80,
    ),
    Pattern(
        name="SHORT_URL",
        regex=r"\b(?:https?:\/\/)?(?:www\.)?(?:bit\.ly|t\.co|goo\.gl|tinyurl\.com|ow\.ly|is\.gd|buff\.ly|shrtco\.de)\/[a-zA-Z0-9]+\b",
        score=0.75,
    ),
    Pattern(
        name="FILE_URL",
        regex=r"\bfile:\/\/\/?[^\s]+\b",
        score=0.70,
    )
]
url_recognizer = PatternRecognizer(patterns=url_patterns,supported_entity="URL")
