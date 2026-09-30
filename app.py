from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.request import urlopen
import threading

active = "BLUE"

class App(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.server.server_port == 8001:
            version = "BLUE - Version 1.0"
        else:
            version = "GREEN - Version 2.0"

        self.send_response(200)
        self.end_headers()
        self.wfile.write(version.encode())

def start(port):
    HTTPServer(("localhost", port), App).serve_forever()

threading.Thread(target=start, args=(8001,), daemon=True).start()
threading.Thread(target=start, args=(8002,), daemon=True).start()

print("Blue and Green environments started")

print("BLUE:", urlopen("http://localhost:8001").read().decode())
print("GREEN:", urlopen("http://localhost:8002").read().decode())

print("\nActive deployment:", active)

active = "GREEN"

print("Switching traffic to Green...")
print("Active deployment:", active)
print("Deployment Successful!")
