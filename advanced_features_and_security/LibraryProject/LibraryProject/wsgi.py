"""
WSGI config for LibraryProject project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""
import os
import sys 
from pathlib import Path 

# Add the project directory to the Python path
BASE_DIR = Path(__file__).resolve().parent.parent # Gets to the LibraryProject folder
sys.path.insert(0, str(BASE_DIR)) # <-- Add this line
# Alternatively, if BASE_DIR gets too high, try:
# sys.path.insert(0, str(Path(__file__).resolve().parent)) # This gets the parent of wsgi.py (i.e., LibraryProject folder itself)


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

application = get_wsgi_application()