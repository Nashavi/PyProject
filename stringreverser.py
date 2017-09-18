def stringreverser(x):
    lenx = len(x)
    reversed = []
    for i in range(1,lenx+1):
        reversed += x[-i]
    return print("The reversed string for %s is -  %s"%(x,''.join(reversed)))

stringreverser("my name is antony")