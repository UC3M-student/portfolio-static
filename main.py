from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/sitemap.xml")
def sitemap():
    return FileResponse("static/sitemap.xml", media_type="application/xml")

@app.get("/robots.txt")
def robots():
    return FileResponse("static/robots.txt", media_type="text/plain")
