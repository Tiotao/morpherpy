#!C:\Users\Yiwen\Documents\Coding\morpherpy\env\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'gunicorn==17.5','console_scripts','gunicorn_paster'
__requires__ = 'gunicorn==17.5'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('gunicorn==17.5', 'console_scripts', 'gunicorn_paster')()
    )
