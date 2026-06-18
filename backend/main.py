
from fastapi import FastAPI
app=FastAPI(title='HealthSync AI')

@app.get('/health')
def health():
    return {'ok':True}
