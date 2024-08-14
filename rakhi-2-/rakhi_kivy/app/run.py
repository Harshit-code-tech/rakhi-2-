# run.py
import os
import sys

# Ensure the current directory is set to the project's root directory
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, '..', '..')
sys.path.insert(0, project_root)

from rakhi_kivy.app.main2 import MyDailyCompanionApp2

if __name__ == '__main__':
    MyDailyCompanionApp2().run()
