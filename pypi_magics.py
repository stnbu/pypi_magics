"""A collection of pypi-related magic commands (e.g. "%pip")
"""

from IPython.core.magic import Magics, magics_class, line_magic
from IPython.utils import py3compat
from IPython.core import page
from subprocess import Popen, PIPE
try:
    from pip.basecommand import Command
    from pip import commands
except ImportError:
    pass

PIP_COMMAND = 'pip'

def has_option(command_name, option):
    """Determines if the command_class has option. For example, "has_option('uninstall', '-y')"
    """
    for command_class in commands.__dict__.values():
        if hasattr(command_class, '__bases__') and Command in command_class.__bases__ and command_class.name == command_name:
            if command_class().cmd_opts.has_option(option):
                return True
    return False

@magics_class
class PyPiMagics(Magics):

    @line_magic
    def pip(self, line):
        """
        Passes all arguments on to "pip", printing stdout/stderr.

        Note that the '--yes' option is set for the "uninstall" command!
        """

        pip_command_line = [PIP_COMMAND] + line.split()
        for element in pip_command_line:
            if element == PIP_COMMAND or element.startswith('-'):
                continue
            else:
                command_name = element
                break
        else:
            command_name = None

        if command_name is not None and has_option(command_name, '-y'):
            pip_command_line.append('-y')

        try:
            p = Popen(pip_command_line, stdout=PIPE, stderr=PIPE, stdin=PIPE)
        except OSError as e:
            if e.errno == errno.ENOENT:
                print "pip not in path"
                return
            else:
                raise
        out, err = p.communicate()
        out = py3compat.bytes_to_str(out)
        err = py3compat.bytes_to_str(err)
        page.page(out)
        sys.stderr.write(err)
        sys.stderr.flush()

def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magics(PyPiMagics)
