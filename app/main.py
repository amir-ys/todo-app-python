from http.server import HTTPServer, BaseHTTPRequestHandler
import os
from routes import routes , not_found
from urllib.parse import urlparse


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.route("GET")

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        self.body = self.rfile.read(content_length).decode('utf-8')
        self.route("POST")

    def respond(self, content, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(content.encode())

    def route(self, method):
        path = self.path
        parsed = urlparse(path)
        handler_func = routes.get((method, parsed.path), not_found)
        handler_func(self)
    
    def view(self, filename, context=None):
     filepath = os.path.join("template", filename)
     if os.path.isfile(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if context:
                for key, value in context.items():
                    content = content.replace(f"{{{{ {key} }}}}", str(value))

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            if isinstance(content, str):
                content = content.encode('utf-8')

            self.wfile.write(content)
        except Exception as e:
            self.send_error(500, f"Internal Server Error: {e}")
     else:
        self.send_error(404, "Page Not Found")



HOST = "0.0.0.0"
PORT = 8080
server = HTTPServer((HOST, PORT), SimpleHandler)
print(f"Serving on http://{HOST}:{PORT}")
server.serve_forever()
