#!/usr/bin/env python3
"""
AI Commanding Heights Analysis - Local Web & API Server
Serves static consulting deck files and provides REST API endpoints for underlying datasets.
Zero external dependencies (uses standard Python library).
"""

import os
import sys
import json
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import urllib.parse

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
PORT = int(os.getenv("PORT", 8080))

class ConsultingDeckHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def log_message(self, format, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")

    def send_json_file(self, filepath: Path):
        if not filepath.exists():
            self.send_error(404, f"Dataset not found: {filepath.name}")
            return
        try:
            with open(filepath, "rb") as f:
                data = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(data)
        except Exception as e:
            self.send_error(500, f"Error reading dataset: {str(e)}")

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # REST API Endpoints
        api_routes = {
            "/api/metadata": "metadata.json",
            "/api/claims": "viral_claims_fact_check.json",
            "/api/surplus": "historical_tech_surplus.json",
            "/api/deflation": "token_price_vs_training_cost.json",
            "/api/capex": "capex_vs_ocf_projection.json",
            "/api/labor": "us_labor_whitecollar_pyramid.json",
            "/api/it-margins": "indian_it_outsourcing_margins.json",
            "/api/radar": "commanding_heights_radar.json"
        }

        if path in api_routes:
            self.send_json_file(DATA_DIR / api_routes[path])
            return

        super().do_GET()

def run_server():
    server_address = ("", PORT)
    try:
        httpd = ThreadingHTTPServer(server_address, ConsultingDeckHandler)
    except OSError:
        # Fallback to alternative port if 8080 is taken
        alt_port = 8088
        httpd = ThreadingHTTPServer(("", alt_port), ConsultingDeckHandler)
        print(f"Port {PORT} busy, fallback to http://localhost:{alt_port}")
        PORT_ACTUAL = alt_port
    else:
        PORT_ACTUAL = PORT

    print("=" * 60)
    print(" 🚀 AI Commanding Heights Strategic Analysis & Fact-Check")
    print(f" 🌐 Web Deck Server: http://localhost:{PORT_ACTUAL}")
    print(f" 📊 REST API Endpoints: http://localhost:{PORT_ACTUAL}/api/metadata")
    print("=" * 60)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer gracefully shut down.")

if __name__ == "__main__":
    run_server()
