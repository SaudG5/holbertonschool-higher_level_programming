#!/usr/bin/python3
"""A simple API built with the http.server module of the standard library."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Handles GET requests and routes them to the matching endpoint."""

    def _send(self, status, content_type, body):
        """Send a response with the given status, content type and body."""
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def do_GET(self):
        """Respond to GET requests based on the requested path."""
        if self.path == "/":
            self._send(200, "text/plain", "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send(200, "application/json", json.dumps(data))
        elif self.path == "/status":
            self._send(200, "text/plain", "OK")
        elif self.path == "/info":
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self._send(200, "application/json", json.dumps(info))
        else:
            self._send(404, "text/plain", "Endpoint not found")


if __name__ == "__main__":
    server = HTTPServer(("", 8000), SimpleAPIHandler)
    print("Serving on http://localhost:8000")
    server.serve_forever()
