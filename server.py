#!/usr/bin/env python3
"""
ElderAssist Local Web Server
Lightweight, accessible HTTP server with proper MIME types and CORS support.
Runs on http://localhost:8000
"""

import http.server
import socketserver
import os
import sys
import webbrowser

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class ElderHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and caching headers suitable for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def guess_type(self, path):
        # Ensure correct MIME types for modern JS modules, CSS, and SVG
        base_type = super().guess_type(path)
        if path.endswith('.js'):
            return 'application/javascript; charset=utf-8'
        elif path.endswith('.css'):
            return 'text/css; charset=utf-8'
        elif path.endswith('.html'):
            return 'text/html; charset=utf-8'
        elif path.endswith('.json'):
            return 'application/json; charset=utf-8'
        elif path.endswith('.sql'):
            return 'text/plain; charset=utf-8'
        return base_type

def run_server():
    os.chdir(DIRECTORY)
    # Allow port reuse immediately
    socketserver.TCPServer.allow_reuse_address = True
    
    try:
        with socketserver.TCPServer(("", PORT), ElderHandler) as httpd:
            url = f"http://localhost:{PORT}"
            print("=" * 65)
            print(f"  ElderAssist Web Application is running at:")
            print(f"  --> {url}")
            print(f"  Serving files from: {DIRECTORY}")
            print(f"  Press Ctrl+C to stop the server.")
            print("=" * 65)
            
            # Check if launched with --open flag
            if "--open" in sys.argv:
                webbrowser.open(url)

            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[ElderAssist] Server stopped gracefully.")
    except OSError as e:
        if e.errno == 10048 or "Address already in use" in str(e):
            print(f"[ElderAssist] Port {PORT} is busy. Trying port 8080...")
            with socketserver.TCPServer(("", 8080), ElderHandler) as httpd:
                print(f"  --> http://localhost:8080")
                httpd.serve_forever()
        else:
            raise e

if __name__ == '__main__':
    run_server()
