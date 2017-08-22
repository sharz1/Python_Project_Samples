#Author: Sharlee Bryan
#Python version 3.6.2
#Sorting algorithm without using sort() or sorted() methods
#Efficiency factor insignificant for this exercise
#test with [67, 45, 2, 13, 1, 998] and [89, 23, 33, 45, 10, 12, 45, 45, 45]

def sortme(mylist):
    lowest = mylist[0]
    highest = mylist[0]
    sortedlist = []
    midlist = []
    if len(mylist)<2:
        return mylist
    else:
        for i in mylist:
            if i >= highest:
                highest = i
                sortedlist.append(i)
            elif i <= lowest:
                lowest = i
                sortedlist.insert(0,i)
            else:
                midlist.append(i)
        if len(midlist)==0:
            return sortedlist
        
        else:
            midlist += sortedlist
            return sortme(midlist)

test1 = [67, 45, 2, 13, 1, 998]
test2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]
test3 = [9]

print("Test1 = {}".format(test1))
print(sortme(test1))
print("Test2 = {}".format(test2))
print(sortme(test2))
print("Test3 = {}".format(test3))
print(sortme(test3))


                
