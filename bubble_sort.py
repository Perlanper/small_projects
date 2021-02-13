import os

def bubble_sort(inpt):
    copy_arr = inpt
    for i in range(len(copy_arr)):
        for j in range(len(copy_arr)):
            if copy_arr[i] < copy_arr[j]:
                copy_arr = swap(copy_arr,i,j)
    return inpt

def swap(inpt_arr,j,i):
    temp = inpt_arr[i]
    inpt_arr[i] = inpt_arr[j]
    inpt_arr[j] = temp
    return inpt_arr


arr = [4,2,5,1,7,8,0]
print(arr)
sorted_arr = bubble_sort(arr)
print(sorted_arr)
os.system("PAUSE")