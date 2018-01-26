import subprocess
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'PT.Config'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))


def check(flist, relpath=''):
    for ref in flist:
        fname = os.path.realpath(os.path.join('../dist', relpath, ref))
        assert os.path.exists(fname)


def test_simple_example():
    out, _ = subprocess.Popen(
        '..\\dist\\conf.exe -P nopipe {}'.format(os.path.join(os.path.dirname(__file__), 'apache.conf')),
        stdout=subprocess.PIPE).communicate()
    assert out.find(b'ServerTokens Full') != -1


def test_ply():
    out, _ = subprocess.Popen(
        '..\\dist\\conf.exe -P nopipe {}'.format(os.path.join(os.path.dirname(__file__), 'lighttpd.conf')),
        stdout=subprocess.PIPE).communicate()
    assert out.find(b'server.dir-listing = "enable"') != -1


def test_exe_refs():
    r = [
        '_ctypes.cp35-win_amd64.pyd',
        '_hashlib.cp35-win_amd64.pyd',
        '_elementtree.cp35-win_amd64.pyd ',
        '_lzma.cp35-win_amd64.pyd ',
        '_socket.cp35-win_amd64.pyd',
        '_ssl.cp35-win_amd64.pyd',
        '_bz2.cp35-win_amd64.pyd',
        'conf.exe',
        'conf.exe.manifest',
        'pyexpat.cp35-win_amd64.pyd',
        'python35.dll',
        'pythoncom35.dll',
        'pywintypes35.dll',
        'select.cp35-win_amd64.pyd',
        'unicodedata.cp35-win_amd64.pyd',
        'win32api.cp35-win_amd64.pyd',
        'inner_rules',
        'base_library.zip',
    ]
    check(r)
