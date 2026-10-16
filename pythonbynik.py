list = [1,2,3,4,5]
print(list)
print(f'length of list : {len(list)}')
list.append('a')
print(list)
print(f'lenght of lisr :{len(list)}')

numbers = [111,2,5,8]
print(len(numbers ))
print(numbers)
numbers.append("34")
print(len(numbers))
print(numbers)
numbers.insert(0,'222')
print(len(numbers))
print(numbers)

given=[1,2,3,4,5,6]
for count in range(len(given)):
     print(given[count])

num =[]
for i in range(0,10):
    num.append(i)
    print(num)

count = 1 
while count <=10 :
    num.append(count)
    count+=1                  
print(num)  # indentation


my_list=[10,20,30,40,50,60,70,80,90,100]
for i in range (0,10):
    my_list[i]+=1
for i in range (10):
       print(my_list[i])


