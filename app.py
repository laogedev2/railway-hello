import os, time
from http.server import BaseHTTPRequestHandler, HTTPServer
START = time.time()
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        up = int(time.time() - START)
        body = ("<html><head><meta charset='utf-8'><title>Railway Hello</title></head>"
                "<body style='font-family:sans-serif;text-align:center;margin-top:15%'>"
                "<h1>🚂 Railway 试水服务在线</h1>"
                f"<p>uptime: {up}s · path: {self.path}</p>"
                "<p>deployed by LaoGeDev · trial run</p></body></html>").encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *a): pass
HTTPServer(("0.0.0.0", int(os.environ.get("PORT", "8080"))), H).serve_forever()
