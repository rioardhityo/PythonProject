x = 0
try:
    x = 1 / 0
except Exception, e:
    print e

print x + 1
