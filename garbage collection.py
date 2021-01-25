import gc

x= 1

print(x)

del x

print(gc.collect())