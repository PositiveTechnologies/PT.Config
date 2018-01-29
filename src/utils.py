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
