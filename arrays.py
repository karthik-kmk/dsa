# 1)
arr = [10,20,70,40,50]
print(arr[2]) # accessing elements

# maximun value in an array
max_value = arr[0]
for num in arr:
    if num>max_value:
        max_value = num
print("maximun value is",max_value)


# sum of all elements
sum = 0
for i in arr:
    sum+=i
print("sum of the array is",sum)

# reverse an arry
reverse = arr[::-1]
print("reverse of the array is",reverse)

# linear search
target = 90
found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("element found at index",i)
        found = True
        break

if found == False:
    print("not found")



#smallest elements

array = [5,2,9,1,7]
min_value = array[0]

for num in array:
    if num<min_value:
        min_value = num
    
print("Minimum Elemenent is",min_value)

#count even and odd number
a = [2,5,7,8,10]

even = 0
odd = 0

for num in a:
    if num%2==0:
        even = even+1
    else:
        odd = odd+1
print("number of even numbers is ",even,"and number of odd numbers is ",odd)

#check if the array is sorted or not

b = [1,2,3,4,2]
flag = True
for i in range(len(b)-1):
    if b[i]>b[i+1]:
        flag = False
        break
    else:
        flag = True

if flag:
    print("Array is sorted")
else:
    print("Array not sorted")


#second largest
c = [10,20,23,14,12,21]

largest = c[i]
second = c[i+1]

for num in c:
    if num>largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("largest is ",largest)
print("second largest is ",second)


#remove duplicates
d = [1,2,2,3,4,5,5]
sorted_array = sorted(d)
unique= []

for i in range(len(d)):
   if i == 0 or sorted_array[i] != sorted_array[i-1]:
       unique.append(sorted_array[i])
    
print(unique)