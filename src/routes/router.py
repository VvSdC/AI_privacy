from service.analyzer import Analyzer
from fastapi import FastAPI,Request,Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

# Creating an object of analyzer
analyzer = Analyzer()

@app.get('/text-analyze')
async def analyze_text(text: str):
    return analyzer.analyze(text)
