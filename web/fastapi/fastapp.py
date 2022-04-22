import html
import requests

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
k8s_svc_url = 'http://10.98.141.216:9999'

@app.get("/nginx", response_class=HTMLResponse)
def nginx():
    r = requests.get(k8s_svc_url, timeout=5)
    
    response = html.unescape(r.text)

    return response