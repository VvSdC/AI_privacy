import re
from geotext import GeoText
from service.__init__ import *

class LocationRecognizer:
    @staticmethod
    def analyze(text):
        places_identified = GeoText(text)
        locations = set(places_identified.cities + places_identified.countries)  # Remove duplicates

        results = []
        for location in locations:
            # Find starting and ending index of all occurrences of the location in the text
            for match in re.finditer(r'\b' + re.escape(location) + r'\b', text, re.IGNORECASE):
                results.append({
                    "start": match.start(),
                    "end": match.end()
                })

        return ResultMapper.library_to_presidio(results=results, confidence_score=1.0, entity_type="LOCATION")
