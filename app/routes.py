
# from utils import view
from urllib.parse import urlparse, parse_qs


def not_found(handler):
    handler.send_response(404)
    handler.send_header('Content-type', 'text/html')
    handler.end_headers()
    handler.wfile.write("<h1>404 - پیدا نشد</h1>")

def index(handler):
    handler.view(handler, "test.html")

def about(handler):
    handler.view( "about.html")
    
def test(handler):
    parsed = urlparse(handler.path)
    query_params = parse_qs(parsed.query)
    handler.view("test.html", {
        "query" : query_params['name'][0]
    })


routes = {
    ("GET", "/"): index,
    ("GET", "/about"): about,
    ("GET", "/test"): test,
}
