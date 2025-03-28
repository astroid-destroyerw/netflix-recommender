import sys
import os

# Add your project directory to the Python path
path = '/home/mohit19/netflixrecommender'
if path not in sys.path:
    sys.path.append(path)

from app import app as application 