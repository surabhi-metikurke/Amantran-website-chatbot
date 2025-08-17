import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))  # Fix ImportError

from app import create_app  # Import after fixing path

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
