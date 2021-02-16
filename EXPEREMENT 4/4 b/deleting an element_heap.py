def del1():
  list1 = []
  num = int(input('Enter the list of numbers: '))
  for i in range (0,num):
    data=int(input())
    list1.insert(i,data)
   import heapq
  print ("The popped and smallest element is : ",end="") 
  print (heapq.heappop(list1))
  list1.sort()
  # using heappop() to pop largest element 
  print ("The popped and largest element is : ",end="")
  list1.reverse()
  print (heapq.heappop(list1))
  list1.reverse()
  list1.sort()
  print(list1)
del1()