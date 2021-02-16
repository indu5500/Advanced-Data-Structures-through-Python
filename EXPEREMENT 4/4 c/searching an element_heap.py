def search1():
  list1 = []
  num = int(input('Enter the list of numbers: '))
  for i in range (0,num):
    data=int(input())
    list1.insert(i,data)
  import heapq
  search=int(input("Enter the element to be searched:"))
  count=1
  for i in range(0,len(list1)):
      if(search==list1[i]):
          print("Element found at",i+1)
          count=0
          break
  if(not count==0):
    print("element not found")
search1()