def merge_sort(arr):
    sorted_arr = split(arr) 
    print(sorted_arr) 


def split(unsorted_arr: list) -> list: 
    #splits arrays into two 
    print(unsorted_arr)
    middle = len(unsorted_arr)//2
    left_side = unsorted_arr[0: middle]
    right_side = unsorted_arr[middle:]
    if len(unsorted_arr) > 1:
        proto_sort = (merge(split(left_side), split(right_side)))
        print("proto_sort = " + str(proto_sort))
        return(proto_sort)
        
    else:
        return(unsorted_arr)
        # you can return
        # return(unsorted_arr, rightSide)
        # then called them using indexing, something[0]
        # here return only 1 parameter so the second variable is null
    
    #split([5,4,3,2,1])


def merge(arr1, arr2) -> list:
    #compares two arrays and puts them together
    i = 0
    j = 0
    sorted_arr = []
    
    while(i < len(arr1) or j < len(arr2)):
        
        if(i == len(arr1)):
            for jj in range(j, len(arr2)):
                sorted_arr.append(arr2[jj])
                
            break
        if(j == len(arr2)):
            for ii in range(i, len(arr1) ):
                sorted_arr.append(arr1[ii])
            break
        if(arr1[i] <= arr2[j]):
            sorted_arr.append(arr1[i])
            i += 1
        elif(arr2[j] <= arr1[i]):
            sorted_arr.append(arr2[j])
            j += 1
    return(sorted_arr)

merge_sort([6,5,4,10,3,2,1,9,9])
       
        
                          
                    
                    
        
        

            
    
        
    
    


             