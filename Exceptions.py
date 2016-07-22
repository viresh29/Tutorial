# Raise an exception to interrupt program
import sys

def convert(s):
    x = int(s)
    return x

print(convert("33"))


# exceptional function

def conv(s):
    try:
        x = int(s)
        print("conversion succedeed! x=", x)
    except ValueError:
        print("Conversion failed!")
        x = -1
    except TypeError:
        print("convesion failed!")
        x = -2
    return x

print(conv([1,2]))



def convert2(s):
    '''convert to an integer'''
    try:
        return int(s)
    except(ValueError,TypeError) as e:
        print("conversion error: {}".format(str(e)),file=sys.stderr)
        raise

print(convert2("Hello"))

from math import log

def string_log(s):
    v = convert2(s)
    return log(v)

print(string_log("ouch"))














