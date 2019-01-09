import os
import sys
import pytest

version = sys.argv[1]
with open('version.py', 'w') as f:
    f.write("version = '%s'" % version)

os.chdir('../src')
os.system('xcopy /s /y "*.py" "../build"')
os.system('xcopy /s /y "config.spec" "../build"')
os.system('xcopy /s /y "inner_rules" "../build"')

os.chdir('../build')
os.system('pyinstaller "config.spec" -y --distpath="../build"')

os.system('xcopy /s /y "config" "../dist"')
os.chdir('../src')
os.system('rm version.py *.pyc')


err = pytest.main('-x ../tests/bvt')
if err:
    print('conf.exe build failed')
    os._exit(-1)

print('conf.exe built successful')
