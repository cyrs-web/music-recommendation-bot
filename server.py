"""
Local Web Server for MelodyBot
Serves the web UI and automatically opens it in your default browser.
Requires NO external dependencies.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PORT = 5000

DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Silence routine GET requests for cleaner terminal output
        pass


def open_browser():
    """Wait briefly for server to bind, then open the browser."""
    time.sleep(0.8)
    url = f"http://localhost:{PORT}"
    print(f"\n🚀 Opening MelodyBot in your browser at: {url}")
    webbrowser.open(url)


def run_server():
    # Allow port reuse to avoid address already in use error
    socketserver.TCPServer.allow_reuse_address = True
    
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            print("=" * 60)
            print("        🎶 MelodyBot Web UI Server is Running 🎶")
            print("=" * 60)
            print(f"Server URL : http://localhost:{PORT}")
            print("Press Ctrl+C in this terminal to stop the server.")
            print("=" * 60)
            
            # Launch browser in a background thread
            threading.Thread(target=open_browser, daemon=True).start()
            
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 10048 or "Address already in use" in str(e):
            print(f"\n⚠️ Port {PORT} is busy, trying port {PORT + 1}...")
            # Try fallback port
            fallback_port = PORT + 1
            with socketserver.TCPServer(("", fallback_port), CustomHTTPRequestHandler) as httpd:
                print(f"Server URL : http://localhost:{fallback_port}")
                threading.Thread(target=lambda: webbrowser.open(f"http://localhost:{fallback_port}"), daemon=True).start()
                httpd.serve_forever()
        else:
            raise e
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    run_server()
