"""Simple HTTP server for Cosmic Dodge game."""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

PORT = int(os.environ.get("PORT", 5000))
DIR = os.path.join(os.path.dirname(__file__), "static")

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(__file__), **kwargs)

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {args[0]} {args[1]} {args[2]}")

if __name__ == "__main__":
    httpd = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Server running on port {PORT}")
    httpd.serve_forever()
