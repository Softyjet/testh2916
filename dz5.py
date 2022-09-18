import colorama
import inspect

print(inspect.ismodule(colorama))
print(inspect.getmodule(colorama))
for method in dir(colorama):
    print(method)
print(type(colorama))
for cursor in dir(colorama):
    print(method)
print(callable(cursor))
print(callable(colorama))
