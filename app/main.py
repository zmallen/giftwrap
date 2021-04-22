from fastapi import FastAPI, Response, Request
import requests
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=10)

@app.get("/simple/{package}/", response_class=HTMLResponse)
async def pypi(package, request:Request, response:Response):
    url = 'https://pypi.org/simple/%s/' % package
    r = requests.get(url)
    if r.ok:
        dont_add_headers = [
            'Content-Length',
            'Content-Encoding'
        ]
        for header_key in r.headers.keys():
            if header_key not in dont_add_headers:
                response.headers[header_key] = r.headers[header_key]
        return r.text