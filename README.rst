IPython PyPi Magics
===================

A collection of pypi-related magic commands (e.g. "%pip")

To install, issue the following at the IPython prompt:

    %install_ext https://github.com/stnbu/pypi_magics/pypi_magics.py

After that, to load it:

    %load_ext pypi_magics

Hint: Place the above command in a *.ipy file in your profile's startup directory.

Commands
--------

%pip
    Passes all arguments on to "pip", printing stdout/stderr. Note that the '--yes' option is set for the "uninstall" command!
