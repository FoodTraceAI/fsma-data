import sys
import os

# Get the absolute path to the "src" directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, BASE_DIR)

from menu_files.menu import menu_list

menu_list();
