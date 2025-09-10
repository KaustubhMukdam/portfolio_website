#!/usr/bin/env python3
"""
Simple HTTP server to serve the portfolio frontend
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

# Configuration
PORT = 3000
HOST = '127.0.0.1'

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        # Handle preflight requests
        self.send_response(200)
        self.end_headers()

def main():
    # Change to the frontend directory
    frontend_dir = Path(__file__).parent
    os.chdir(frontend_dir)
    
    # Try to bind to the preferred port; if busy, increment until available
    port = PORT
    httpd = None
    socketserver.TCPServer.allow_reuse_address = True
    while port < PORT + 20:
        try:
            httpd = socketserver.TCPServer((HOST, port), CustomHTTPRequestHandler)
            break
        except OSError:
            port += 1
    
    if httpd is None:
        print("❌ Could not bind to any port in range.")
        sys.exit(1)
    
    print(f"🚀 Portfolio Frontend Server")
    print(f"📍 Serving at: http://{HOST}:{port}")
    print(f"📁 Directory: {frontend_dir}")
    print(f"🌐 Opening browser...")
    print(f"⏹️  Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Open browser
    try:
        webbrowser.open(f'http://{HOST}:{port}')
    except Exception:
        pass
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        sys.exit(0)

if __name__ == "__main__":
    main()
