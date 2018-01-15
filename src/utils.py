import sys
import os
import wmi
import linecache


def write_file(fname, s, mode=''):
    f = open(fname, 'w' + mode, encoding='utf-8')
    f.write(s)
    f.close()


def append_file(fname, s, mode=''):
    f = open(fname, 'a' + mode, encoding='utf-8')
    f.write(s)
    f.close()


def is_frozen():
    return getattr(sys, 'frozen', False)


def getappdir():
    if is_frozen():
        application_path = os.path.dirname(sys.executable)
        prod = os.path.join(application_path, '../php')
        dev = os.path.join(application_path, '../dist')
        return prod if os.path.exists(prod) else dev
    application_path = os.path.dirname(__file__)
    return os.path.join(application_path, '../dist')


def check_disk_free_space(path):
    c = wmi.WMI()
    drive, _ = os.path.splitdrive(path)
    wql = "Select * From Win32_logicaldisk WHERE Caption=\"%s\"" % drive
    if int(c.query(wql)[0].FreeSpace) < 30e3:
        sys.exit("<error>Not enough free disk space</error>")


def file_line(fname, lineno):
    try:
        return linecache.getline(fname, lineno).strip()
    except UnicodeDecodeError:
        with open(fname, 'r') as f:
            lines = f.readlines()
        return lines[lineno - 1].strip()
