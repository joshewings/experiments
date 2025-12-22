from http.server import BaseHTTPRequestHandler, HTTPServer


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"""
<!doctype html>
<html lang=\"en\">
  <head>
    <meta charset=\"utf-8\" />
    <title>Hello World</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
  </body>
</html>
""")


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, HelloHandler)
    print("Serving on http://localhost:8000")
    httpd.serve_forever()
