Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def duplicate( a ):
    for i in a :
        if (a.count(i) > 1):
            print("element {} is repeated".format(i))

duplicate([1,2,3,4,5,3])
SyntaxError: invalid syntax
>>> 
