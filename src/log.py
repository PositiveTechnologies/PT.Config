from utils import *
import time
from datetime import datetime
import traceback
import sys
import os


class Log:
    def __init__(self, logs_dir):
        if logs_dir:
            self.HOMEDIR = logs_dir
        else:
            self.HOMEDIR = os.path.join(os.getenv('LOCALAPPDATA'), "PT.CONFIG\\logs")
        if not os.path.exists(self.HOMEDIR):
            os.makedirs(self.HOMEDIR)

        self.LOGNAME = os.path.join(self.HOMEDIR, "" + time.strftime("%Y-%m-%d") + ".log")

    def write(self, msg, err=False):
        if err:
            sys.stdout.write('{}\n'.format(msg))
            sys.stdout.flush()
        self.writeName(self.LOGNAME, msg)

    def writeName(self, name, msg):
        with open(name, 'a+b') as log:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            log.write(('{}: {}\n'.format(timestamp, msg)).encode())

    def exc(self):
        t, v, tb = sys.exc_info()
        if t == SystemExit:
            return

        tb = traceback.extract_tb(tb)
        stack_str = self.tb2str(tb)
        sep_line = '-' * 80 + '\n'
        exc_str = '{}{}\n\n"{}" exception, {}\n{}'.format(sep_line, stack_str, t.__name__, v, sep_line)
        self.write(exc_str, True)

    def tb2str(self, tb):
        ret = []
        for module, nline, function, line in tb:
            _, module = os.path.split(module)
            if module == '<string>':
                module = 'pt.config'
            s = '{}, line {}, "{}"'.format(module, nline, function)
            if line:
                s += ':\n    {}'.format(line)

            ret.append(s)

        ret = '\n'.join(ret)
        return ret
