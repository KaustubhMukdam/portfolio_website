#!/usr/bin/env python3
"""
Portfolio Website Startup Script
Starts both backend and frontend servers
"""

import subprocess
import sys
import time
import os
import signal
import threading
from pathlib import Path

def run_backend():
    """Start the Flask backend server"""
    backend_dir = Path(__file__).parent / "portfolio_backend"
    os.chdir(backend_dir)
    
    print("🚀 Starting Flask Backend Server...")
    print(f"📁 Backend Directory: {backend_dir}")
    print("🌐 Backend will be available at: http://localhost:5000")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "run.py"], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Backend server stopped")
    except Exception as e:
        print(f"❌ Error starting backend: {e}")

def run_frontend():
    """Start the frontend server"""
    frontend_dir = Path(__file__).parent / "portfolio_frontend"
    os.chdir(frontend_dir)
    
    print("🎨 Starting Frontend Server...")
    print(f"📁 Frontend Directory: {frontend_dir}")
    print("🌐 Frontend will be available at: http://localhost:3000")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "server.py"], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Frontend server stopped")
    except Exception as e:
        print(f"❌ Error starting frontend: {e}")

def main():
    print("🌟 Portfolio Website Startup")
    print("=" * 50)
    
    # Check if required directories exist
    backend_dir = Path("portfolio_backend")
    frontend_dir = Path("portfolio_frontend")
    
    if not backend_dir.exists():
        print("❌ Backend directory not found!")
        sys.exit(1)
    
    if not frontend_dir.exists():
        print("❌ Frontend directory not found!")
        sys.exit(1)
    
    print("✅ All directories found")
    print("🚀 Starting servers...")
    print("⏹️  Press Ctrl+C to stop all servers")
    print("=" * 50)
    
    # Start backend in a separate thread
    backend_thread = threading.Thread(target=run_backend, daemon=True)
    backend_thread.start()
    
    # Give backend time to start
    time.sleep(2)
    
    # Start frontend in main thread
    try:
        run_frontend()
    except KeyboardInterrupt:
        print("\n🛑 All servers stopped by user")
        sys.exit(0)

if __name__ == "__main__":
    main()
