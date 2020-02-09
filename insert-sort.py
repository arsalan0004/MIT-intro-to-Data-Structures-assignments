

def insert_sort(x: list):
    for i in range(1,len(x)):
        key = x[i]
        k = i - 1 
        
        while((x[k] >= key) and (k > -1)):
            x[k+1] = x[k]
            k -= 1 
        x[k+1] = key
        
    return(x)
    
            
