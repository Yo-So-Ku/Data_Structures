#create 2 list

list1 = [2,5,15,36,47,56,59,78,156,244,268]

list2 = [18,39,42,43,66,69,100]

#creating a merged list

mergelist = list1 + list2

#sorting the merged list

for i in range(17):

    for i in range(17):

        if mergelist[i] > mergelist[i + 1]:
            
            placeholder = mergelist[i]

            mergelist[i] = mergelist[i + 1]

            mergelist[i + 1] = placeholder