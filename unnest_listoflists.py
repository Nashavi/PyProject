def flatten(listolists,out = []):
    
    for i in range(len(listolists)):
        
        if type(listolists[i]) == type([]):
            flatten(listolists[i],out)
        else:
            out.append(listolists[i])
    
    return out
    
    
lister = [[[[4,5,6],3],2],21,2,[2,5,7,[23,4,[6]]]]
flatten(lister)
