"""Keypress - A Module for detectin a single keypress."""


try:
    import msvcrt

    def getkey():
        """wait for a keypress and return a single character string."""
        return msvcrt.getch()

except ImportError:

    import sys
    import tty
    import termios

    def getkey():
        """wait for a keypress and return a single character string."""

        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcgetattr(fd,termios.TCSADRAIN,original_attributes)
        return ch

# if either of the unix=specific tty or termios are not found,
# we allow the ImportError to propagate from here.
