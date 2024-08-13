#Name: Raine.B
#Course: CS1
#Instructor: Vasanta
#Date: 11/09/2021
#Purpose: Compares numbers and sorts lists

def compare_func(a, b):#function meant to compare the size of two numbers
    #to be implemented into partition function
    if a >= b:
        return True
    if a < b:
        return False

print(compare_func(5, 5))

def partition(the_list, p, r, compare_func):#creates a list with the last item becoming the middle value with values decreasing to the left

    i = p - 1
    j = p
    pivot = the_list[r]
    while j < r:
        if compare_func(the_list[j],pivot):
            i += 1

            (the_list[i], the_list[j]) = (the_list[j], the_list[i])     #swaps indices of j and i
        j = j + 1
    the_list[i+1], the_list[r] = the_list[r],the_list[i+1]

    return i + 1

rlist = [2, 4, 7, 12, 8, 9, 0, 1]

def quicksort(the_list, p, r, compare_func):    #sorts sublist and returns an index into the sublist, indicating where partition put the pivot item.
    # if len(the_list) == 2:
    #     return
    if p >= r:  #base case
        return

    q = partition(the_list, p, r, compare_func)
    # recursively calls quicksort
    quicksort(the_list, p, q-1, compare_func)
    quicksort(the_list, q+1, r, compare_func)


def sort(the_list, compare_func):   #makes a call to the quicksort function to sort the entire list
    return quicksort(the_list, 0, len(the_list)-1, compare_func)

sort(rlist, compare_func)

print(rlist)