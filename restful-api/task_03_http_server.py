import http.server
import socketserver
import json

# Define the port number here
PORT = 8000  # You can change this to another port if needed

class MyRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Handle the root endpoint
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Handle the /data endpoint
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # Handle the /info endpoint
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))

        # Handle undefined endpoints with a 404 response
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found: Endpoint not found.")

# Ensure the PORT is defined before this point
if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
