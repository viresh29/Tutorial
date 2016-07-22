import sys
print(sys.getdefaultencoding())
import statistics as s
import numpy as np

x = [10,20,30,40]

print(np.median(x))
print(s.median(x))

print(max(x))
print(min(x))
print(sum(x))
print(len(x))

print(np.percentile(x,75) - np.percentile(x,25))

print(s.mean(x))




