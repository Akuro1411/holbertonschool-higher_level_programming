from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import socket
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(data.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200, "OK")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            data = json.dumps({"version": "1.0", "description": "A simple API built with http.server"})
            self.wfile.write(data.encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

try:
    httpd = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()
except KeyboardInterrupt:
    print("The server was stopped")
    httpd.socket.close()
