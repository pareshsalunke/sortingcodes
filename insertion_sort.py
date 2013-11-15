def insertion_sort(list):  
  for index in range(1,len(list)):
    value = list[index]
    i = index-1  
    while(i>=0): 
       if (value < list[i]):
         list[i+1]=list[i]
         list[i] = value
       i = i - 1
  print list       
      
      
def main():
  list = [8,4,3,6,1,2]
  insertion_sort(list)
   
if __name__ == '__main__':
  main()
  
