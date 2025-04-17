from http.server import HTTPServer, BaseHTTPRequestHandler
import os
from routes import routes , not_found

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.route("GET")

    def do_POST(self):
        self.route("POST")

    def respond(self, content, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(content.encode())

    def route(self, method):
        path = self.path
        handler_func = routes.get((method, path), not_found)
        handler_func(self)



HOST = "0.0.0.0"
PORT = 8080
server = HTTPServer((HOST, PORT), SimpleHandler)
print(f"Serving on http://{HOST}:{PORT}")
server.serve_forever()
