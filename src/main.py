# from service.presidioAnalyzer import PresidioAnalyzer
# from service.locationRecognizer import LocationRecognizer
# from service.creditCardRecognizer import CreditCardRecognizer
from service.starpiiAnalyzer import StarPIIAnalyzer

dummy_text = """
John's contact number in the US is +1 (415) 555-2671, while his UK number is +44 7911 123456.
For India, reach out at +91-9876543210 or 98765 43210.

Some random IP addresses: 
- IPv4: 192.168.1.1, 10.0.0.1, 255.255.255.255, 172.16.32.5
- Invalid IPv4: 999.999.999.999, 300.300.300.300
- IPv6: 2001:0db8:85a3:0000:0000:8a2e:0370:7334, ::1, fe80::1ff:fe23:4567:890a
- Invalid IPv6: 12345::6789, 2001:db8:::1

Locations mentioned:
- New York, USA
- London, United Kingdom
- Bangalore, India
- San Francisco, California
- Sydney, Australia
- Fake Location: Atlantis, Moon Base Alpha and London and also loNdon


Credit Card Numbers:
- Visa 4111 1111 1111 1111
- MasterCard 5500-0000-0000-0004
- Discover  6011 0000 0000 0004
- AMEX 3714 496353 98431
- NO spaces  4111111111111111  6011000000000004
- 4111 1111 1111 1111

"""

# presidio_analyzer = PresidioAnalyzer()
# print(presidio_analyzer.analyze(dummy_text))
# results = CreditCardRecognizer.analyze(dummy_text)

analyzer = StarPIIAnalyzer()
results = analyzer.analyze(dummy_text)

for result in results:
    print(f"{dummy_text[result.start:result.end]} -> {result.entity_type}")