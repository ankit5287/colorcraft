import os
import sys

# Vercel -> /var/task/api/index.py
# Root -> /var/task/
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

from colorcraft_project.wsgi import application

# Vercel looks for 'app' variable
app = application
