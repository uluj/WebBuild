import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))  # Points to the same folder as the Python script

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://0.0.0.0:{PORT} (accessible locally and on the network)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Shutting down the server.")
            httpd.shutdown()

if __name__ == "__main__":
    run_server()
