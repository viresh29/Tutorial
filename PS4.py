# Range

print(range(5))

for i in range(5):
    print(i)

t = [6,651,4564,78952]

for p in enumerate(t):
    print(p)


for i, v in enumerate(t):
    print("i = {}, v = {}".format(i,v))


s = "show how to index into sequences".split()

print(s[0])

print(s[1:3])

w = "the quick brown fox jumps over the lazy dog".split()

print(w)

i = w.index('fox')
print(i)

print(w[i])

#w.index('unicorn')

x = w.count('the')
print(x)

