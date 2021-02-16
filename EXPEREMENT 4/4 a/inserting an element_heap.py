def insert1():
  list1 = []
  num = int(input('Enter the list of numbers: '))
  for i in range (0,num):
    data=int(input())
    list1.insert(i,data)
  import heapq
  print ("The created heap is : ",end="") 
  print (list1) 
  import heapq
  print ("The modified heap after push is : ",end="") 
  print (list1)
insert1()