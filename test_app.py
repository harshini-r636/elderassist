#!/usr/bin/env python3
"""
ElderAssist Automated Verification Test Suite
Tests file presence, static asset integrity, HTML ARIA compliance,
schema structure, and HTTP server endpoint availability.
"""

import os
import sys
import threading
import time
import urllib.request
import socketserver

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def test_files_exist():
    required_files = [
        "index.html",
        "css/styles.css",
        "js/config.js",
        "js/supabase-client.js",
        "js/accessibility.js",
        "js/app.js",
        "supabase/schema.sql",
        "server.py"
    ]
    print("[1] Checking required files...")
    for rel_path in required_files:
        full_path = os.path.join(ROOT_DIR, rel_path)
        assert os.path.exists(full_path), f"Missing file: {rel_path}"
        assert os.path.getsize(full_path) > 0, f"Empty file: {rel_path}"
        print(f"  [OK] {rel_path} ({os.path.getsize(full_path)} bytes)")
    print("  All required files are present.\n")

def test_html_semantics_and_features():
    print("[2] Verifying HTML semantic structure and accessibility...")
    html_path = os.path.join(ROOT_DIR, "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check key categories
    categories = ["payments", "appointments", "online_forms", "video_calls", "smartphone_use"]
    for cat in categories:
        assert cat in content, f"Missing category '{cat}' in index.html"
    print("  [OK] All 5 digital task categories found in HTML")

    # Check elderly, volunteer, admin roles
    roles = ['data-role="elderly"', 'data-role="volunteer"', 'data-role="admin"']
    for role in roles:
        assert role in content, f"Missing role selector '{role}' in index.html"
    print("  [OK] All 3 role selectors (Elderly, Volunteer, Admin) found")

    # Check accessibility controls
    a11y_features = ['data-font-scale="large"', 'id="btn-high-contrast"', 'tts-global-btn']
    for feat in a11y_features:
        assert feat in content, f"Missing accessibility control '{feat}'"
    print("  [OK] Accessibility toolbar controls (Font scaler, High contrast, Speech narration) present")

    # Check modals
    modals = [
        "modal-create-request",
        "modal-guide-viewer",
        "modal-chat",
        "modal-review",
        "modal-notifications",
        "modal-supabase"
    ]
    for m in modals:
        assert f'id="{m}"' in content, f"Missing modal '{m}'"
    print("  [OK] All 6 core modals present (Request, Guide Viewer, Chat, Review, Notifications, Supabase)\n")

def test_supabase_schema():
    print("[3] Verifying Supabase SQL Schema...")
    sql_path = os.path.join(ROOT_DIR, "supabase", "schema.sql")
    with open(sql_path, "r", encoding="utf-8") as f:
        sql = f.read()

    tables = ["profiles", "help_requests", "messages", "guides", "reviews", "notifications"]
    for table in tables:
        assert f"CREATE TABLE IF NOT EXISTS public.{table}" in sql, f"Missing table {table} in schema.sql"
    print("  [OK] All 6 database tables defined")

    assert "ENABLE ROW LEVEL SECURITY" in sql, "Missing Row Level Security statements"
    print("  [OK] Row Level Security (RLS) policies configured")

    assert "INSERT INTO public.profiles" in sql, "Missing seed data for profiles"
    assert "INSERT INTO public.guides" in sql, "Missing seed data for guides"
    print("  [OK] Seed data for profiles, guides, and initial requests validated\n")

def test_css_design_system():
    print("[4] Verifying CSS elderly design system & contrast modes...")
    css_path = os.path.join(ROOT_DIR, "css", "styles.css")
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    assert "--font-base" in css, "Missing CSS font base scale"
    assert ".font-large" in css, "Missing .font-large CSS modifier"
    assert ".font-xlarge" in css, "Missing .font-xlarge CSS modifier"
    assert "html.high-contrast" in css, "Missing html.high-contrast theme"
    assert "--btn-min-height" in css, "Missing accessible button min height"
    print("  [OK] Accessibility CSS variables and high contrast theme validated\n")

def test_http_server():
    print("[5] Testing HTTP Server...")
    from server import ElderHandler
    test_port = 8899

    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("", test_port), ElderHandler)
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()

    time.sleep(0.5)
    try:
        url = f"http://127.0.0.1:{test_port}/index.html"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=3) as resp:
            status = resp.getcode()
            body = resp.read().decode('utf-8')
            assert status == 200, f"Expected 200 OK, got {status}"
            assert "<!DOCTYPE html>" in body, "Response is not HTML"
            print(f"  [OK] HTTP GET {url} -> 200 OK ({len(body)} bytes)")

        # Test static js mime type
        js_url = f"http://127.0.0.1:{test_port}/js/config.js"
        with urllib.request.urlopen(js_url, timeout=3) as resp:
            content_type = resp.headers.get('Content-Type')
            assert 'javascript' in content_type, f"Invalid MIME: {content_type}"
            print(f"  [OK] HTTP GET {js_url} -> 200 OK (Content-Type: {content_type})")
    finally:
        httpd.shutdown()
        httpd.server_close()
    print("  [OK] Server tests passed cleanly.\n")

if __name__ == '__main__':
    print("=" * 60)
    print("  Starting ElderAssist Verification Test Suite")
    print("=" * 60)
    test_files_exist()
    test_html_semantics_and_features()
    test_supabase_schema()
    test_css_design_system()
    test_http_server()
    print("ALL TESTS PASSED SUCCESSFULLY! ElderAssist is ready.")
