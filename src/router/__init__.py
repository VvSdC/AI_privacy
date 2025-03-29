from fastapi import FastAPI,Request,Response # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from service.__init__ import presidio_analyzer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)


@app.get('/text-analyze')
async def analyze_text(text: str):
    analyzer_results = presidio_analyzer.analyze(text,language="en")
    results = []
    for result in analyzer_results:
        entity = [text[result.start:result.end],result.entity_type]
        results.append(entity)
    return results