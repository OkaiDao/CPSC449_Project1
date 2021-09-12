#!/usr/bin/env python3

# Example HTTP server
#
# See <https://docs.python.org/3/library/http.server.html> for details
#

import http.server
import socketserver
import redact

PORT = 8080


class ExampleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/operations':
            self.send_error(404)
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            payload = (
                f'<head><title>Redact</title><link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet"></head>'
                f'<body style="margin-top: 40px">'
                f'<div class="container">'
                f'<div id="view-10">'
                f'<div class="hero-unit">'
                f'<h1>Go here for Usage: <a href="https://foaas.com/" target="_blank">foaas.com</a></h1>'
                f'<p><em>-IJZ</em></p>'
                f'</div>'
                f'</div>'
                f'<p style="text-align: center"><a href="https://foaas.com/" target="_blank">foaas.com</a></p>'
                f'</div>'
                f'</body>'
            )
            self.wfile.write(payload.encode('utf-8'))
        else:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            data = redact.get_censored_json(self.path)
            payload = (
                f'<head><title>{self.path}</title><link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet"></head>'
                f'<body style="margin-top: 40px">'
                f'<div class="container">'
                f'<div id="view-10">'
                f'<div class="hero-unit">'
                f'<h1>{data["message"]}</h1>'
                f'<p><em>{data["subtitle"]}</em></p>'
                f'</div>'
                f'</div>'
                f'<p style="text-align: center"><a href="https://foaas.com/" target="_blank">foaas.com</a></p>'
                f'</div>'
                f'</body>'
            )
            self.wfile.write(payload.encode('utf-8'))


with socketserver.TCPServer(("", PORT), ExampleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
