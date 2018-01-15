from optparse import OptionParser, BadOptionError, AmbiguousOptionError
from utils import *
import os


class PassThroughOptionParser(OptionParser):
    """
    An unknown option pass-through implementation of OptionParser.

    When unknown arguments are encountered, skip it, until rargs is depleted.

    sys.exit(status) will still be called if a known argument is passed
    incorrectly (e.g. missing arguments or bad argument types, etc.)
    """
    def _process_args(self, largs, rargs, values):
        while rargs:
            try:
                OptionParser._process_args(self, largs, rargs, values)
            except (BadOptionError, AmbiguousOptionError):
                pass


parser = PassThroughOptionParser(usage="""usage: %prog [options] <"my config file">""")
parser.add_option("-v", "--version", dest="version", action="store_true", default=False, help="show program version")
parser.add_option("-r", "--report", dest="report", default=None, help="XML report filename",
                  metavar="<report.xml>")
parser.add_option("-P", "--pipe", dest="pipe", default=None, help="UI pipe name", metavar="<Pipe_N>")
parser.add_option("--user-rules", dest="user_rules", default=None, help="User rules filename")
parser.add_option("--preprocessing", dest="preprocessing", action="store_true", default=False, help="Preprocessing mode")
parser.add_option("--logs-dir", dest="logs_dir", default=None, help="Log path name")
parser.add_option("--temp-dir", dest="temp_dir", default=None, help="not supported")
parser.add_option("--result-protocol", help="not supported")


(options, args) = parser.parse_args()
options.json_version = '2.0'

if options.version:
    if is_frozen():
        import version
        v = version.version
    else:
        v = 'debug'
    print('PT.CONFIG %s' % v)
    os._exit(0)
