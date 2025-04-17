
from utils import view

def not_found(handler):
    handler.send_response(404)
    handler.send_header('Content-type', 'text/html')
    handler.end_headers()
    handler.wfile.write("<h1>404 - پیدا نشد</h1>")

def index(handler):
    view(handler, "test.html")

def about(handler):
    view(handler, "about.html")

routes = {
    ("GET", "/"): index,
    ("GET", "/about"): about,
}
