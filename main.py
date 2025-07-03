from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

# Verificación de Google Search Console
@app.get("/google512f505ee54497af.html")
def google_verification():
    return FileResponse("google512f505ee54497af.html")

# Sitemap
@app.get("/sitemap.xml")
def sitemap():
    return FileResponse("static/sitemap.xml", media_type="application/xml")

# Robots.txt
@app.get("/robots.txt")
def robots():
    return FileResponse("static/robots.txt", media_type="text/plain")
