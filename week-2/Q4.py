Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def group(x,l):
        gl=[]
        g=[]
        i=0
        while i<len(x):
                if(len(gl)<l):
                        gl.append(x[i])
                        i=i+1
                else:
                        g.append(gl)
                        gl=[]
        g.append(gl)
        return g
print (group([1,3,2,2,9,7,2,4],3))
