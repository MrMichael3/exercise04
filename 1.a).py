def slice_tuple(tuple,begin,end):
    return tuple [begin:end]

t = (1,"python",2,"tuple",3,"string")
print(slice_tuple(t,0,3)) # prints: (1, 'python', 2)
print(slice_tuple(t,2,5)) # prints: (2, 'tuple', 3)
print(slice_tuple(t,-2,-1)) # prints: (3,)
print(slice_tuple(t,4,len(t))) # prints: (3, 'string')
