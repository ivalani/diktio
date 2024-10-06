import http.server
import socketserver
import os

DIRECTORY = "/."
os.chdir(DIRECTORY)

# Define the port you want to serve on
PORT = 8080

# Create a handler for the requests
Handler = http.server.SimpleHTTPRequestHandler

# Set up the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving HTTP on port {PORT}")
    httpd.serve_forever()
