#!C:\Users\sylvain.therien\PycharmProjects\Pyramid_3\env3.5.2\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'waitress==0.9.0','console_scripts','waitress-serve'
__requires__ = 'waitress==0.9.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('waitress==0.9.0', 'console_scripts', 'waitress-serve')()
    )
