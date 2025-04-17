import os

def view(handler ,filename):
     filename = os.path.join("template", filename)
     if os.path.isfile(filename):
            try:
                with open(filename, 'rb') as f:
                    content = f.read()
                handler.send_response(200)
                handler.send_header('Content-type', 'text/html')
                handler.end_headers()
                handler.wfile.write(content)
            except Exception as e:
                handler.send_error(500, f"Internal Server Error: {e}")
     else:
        handler.send_error(404, "Page Not Found")
