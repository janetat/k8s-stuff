import html
import requests

from fastapi import FastAPI

app = FastAPI()
k8s_svc_url = 'http://10.98.141.216:9999'

@app.get("/")
def index():
    r = requests.get(k8s_svc_url, timeout=5)
    
    response = html.unescape(r.text)

    return response