from fastapi import FastAPI, Response, Request
import requests
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=10)

paranoid = False

class OctetStreamResponse(Response):
    media_type = "application/octet-stream"

#localhost:8000/packages/virtualenvwrapper-0.1.0.tar.gz/
@app.get("/packages/{package}/", response_class=OctetStreamResponse)
async def serve_package(package, response:Response):
    package_path = 'app/packages/virtualenvwrapper-0.1.0.tar.gz'
    data = None
    import ipdb; ipdb.set_trace()
    with open(package_path, 'rb') as fd:
        data = fd.read()
    return Response(
        data,
        media_type="application/octet-stream"
    )

@app.get("/simple/{package}/", response_class=HTMLResponse)
async def pypi(package, request:Request, response:Response):
#    if not paranoid:
#        return 'http://localhost:8000/packages/virtualenvwrapper-0.1.0.tar.gz/'
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

@app.get("/api/v1/dependencies?gems={gems}", response_class=HTMLResponse)
async def rubygems(gems, request:Request, response:Response):
    return 'ok'
