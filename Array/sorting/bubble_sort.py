# def sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
            
# arr=[4,5,3,2,1,9,3]
# print(sort(arr))



n = int(input("Enter the number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element {}: ".format(i + 1))))

for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    for x in arr:
        print(x)

print("Sorted:")
for x in arr:
    print(x)