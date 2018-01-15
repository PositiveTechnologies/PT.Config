from distutils.core import setup
from Cython.Build import cythonize
import os

setup(
        name='config',
        ext_modules=cythonize("*.py", exclude=['main.py', 'setup.py', 'build.py', 'lighttpd.py',
                                               ])
)

os.system('rm *.c')
