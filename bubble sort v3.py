items = [23, 41, 11, 17, 34, 56]
n= len(items)-1
swapped = True


while swapped and n > 0: # External Loop
    swapped = False   # breaks loop if swapped assigned to false  
    for index in range(0, n):
        if (items[index] > items[index+1]):  # if statement for item 0 to 1
            temp = items[index] # defining temp as index
            items[index] = items[index+1]  # item 0 has been assigned to item 1
            items[index+1] = temp  # item 1 becomes item 0

            swapped = True


    n = n - 1

        
        
    

print(items)
        
