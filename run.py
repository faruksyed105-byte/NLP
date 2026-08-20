import argparse
import os
import sys
import threading
import time
import webbrowser
import uvicorn

# Ensure UTF-8 output in Windows consoles
if sys.platform == "win32":
    os.environ["PYTHONIOENCODING"] = "utf-8"
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass


def open_browser(url: str, delay: float = 1.5):
    """Open default browser after server startup."""
    time.sleep(delay)
    print(f"\n[LexiNLP] Opening browser at {url}...")
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"[LexiNLP] Note: Could not auto-open browser ({e}). Please open {url} manually.")


def parse_args():
    parser = argparse.ArgumentParser(description="LexiNLP - Legal Document NLP & Contract Intelligence Platform")
    parser.add_argument("--host", default=os.environ.get("HOST", "127.0.0.1"), help="Host to bind (default: 127.0.0.1 or localhost)")
    parser.add_argument("--port", "-p", type=int, default=int(os.environ.get("PORT", 8000)), help="Port to bind (default: 8000)")
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload on code changes")
    parser.add_argument("--no-browser", action="store_true", help="Do not automatically launch web browser")
    return parser.parse_args()


def main():
    args = parse_args()

    # Normalize host for uvicorn socket binding
    bind_host = "127.0.0.1" if args.host.lower() == "localhost" else args.host
    port = args.port

    localhost_url = f"http://localhost:{port}"
    ip_url = f"http://{bind_host}:{port}"
    browser_url = localhost_url if bind_host in ("127.0.0.1", "0.0.0.0") else ip_url

    print("=" * 68)
    print(" ⚖️  LexiNLP — Legal Document NLP & Contract Intelligence Platform")
    print("=" * 68)
    print(f"  • Local Web URL:      {localhost_url}")
    print(f"  • IP Web URL:         {ip_url}")
    print(f"  • Swagger API Docs:   {localhost_url}/docs")
    print(f"  • ReDoc Specs:        {localhost_url}/redoc")
    print(f"  • Health Check:       {localhost_url}/api/health")
    print("=" * 68)
    print(f"  Press Ctrl+C in terminal to stop server.\n")

    # Launch browser in a background thread if run directly
    if not args.no_browser:
        threading.Thread(target=open_browser, args=(browser_url,), daemon=True).start()

    # Start Uvicorn ASGI server
    uvicorn.run(
        "backend.app:app",
        host=bind_host,
        port=port,
        log_level="info",
        reload=args.reload
    )


if __name__ == "__main__":
    main()

