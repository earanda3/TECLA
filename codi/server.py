#!/usr/bin/env python3
import http.server
import socketserver
import sys

PORT = 8080

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        pass  # silencia els logs de cada request

socketserver.TCPServer.allow_reuse_address = True

def start_server(port):
    try:
        with socketserver.TCPServer(("127.0.0.1", port), MyHTTPRequestHandler) as httpd:
            print(f"✓ Servidor TECLA al port {port}")
            print(f"  Obre: http://127.0.0.1:{port}/tecla.html")
            print("  Ctrl+C per aturar\n")
            httpd.serve_forever()
    except OSError as e:
        if e.errno in (48, 98, 10048):  # macOS=48, Linux=98, Windows=10048
            print(f"Port {port} ocupat, provant {port + 1}…")
            start_server(port + 1)
        else:
            raise

if __name__ == "__main__":
    try:
        start_server(PORT)
    except KeyboardInterrupt:
        print("\nServidor aturat.")
        sys.exit(0)
