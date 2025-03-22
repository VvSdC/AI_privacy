from presidio_anonymizer import RecognizerResult

class ResultMapper:

    @staticmethod
    def library_to_presidio(results,entity_type,confidence_score):
        recognizer_results = [
            RecognizerResult(
                entity_type=entity_type,
                score=confidence_score,
                start=result['start'],
                end=result['end']
            ) for result in results
        ]
        return recognizer_results


    @staticmethod
    def model_to_presidio(results):
        recognizer_results = [
            RecognizerResult(
                entity_type=result['entity_group'],
                score=result['score'],
                start=result['start'],
                end=result['end']
            ) for result in results
        ] 
        return recognizer_results