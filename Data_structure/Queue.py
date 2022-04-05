#initialization of queue
queue=[]

#adding elements to queue
queue.append('Ram')
queue.append('Shyam')
queue.append('Hari')

#printing the content of queue
print(queue)

#removing the content from queue
print(queue.pop(1))

#user input element on queue
new_queue=[]
if len(new_queue)==100:
    print("full")
else:
    new_queue.append(input("enter the element "))

print("the element of queue is:",new_queue)
