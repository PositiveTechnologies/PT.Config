import os
import sys
import pytest

version = sys.argv[1]
with open('version.py', 'w') as f:
    f.write("version = '%s'" % version)

os.chdir('../src')
os.system('xcopy /s /y "main.py" "../build"')
os.system('xcopy /s /y "lighttpd.py" "../build"')
os.system('xcopy /s /y "config.spec" "../build"')
os.system('xcopy /s /y "inner_rules" "../build"')

os.system("{} setup.py build --build-lib=../dist --build-temp=../build".format(sys.executable))

os.chdir('../build')
os.system('{} ../PyInstaller-3.2/pyinstaller.py "config.spec" -y --distpath="../build"'.format(sys.executable))

os.system('xcopy /s /y "config" "../dist"')
os.chdir('../src')
os.system('rm version.py *.pyc')


err = pytest.main('-x ../tests/bvt')
if err:
    print('conf.exe build failed')
    os._exit(-1)

print('conf.exe built successful')
