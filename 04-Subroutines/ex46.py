''' Define the function f(x,y), which returns the sum of numbers in the range <x,y> that are
completely divisible by 2 and 3 and not divisible by 4. Sample result:
'''
def f(x,y):
  i = x 
  y = y + 1
  sum = 0
  while i<y:
    if i%2==0 and i%3 ==0 and i%4!=0: 
        print(i, end=" ")
        sum += i
    i +=1
  print(" ")  
  print(sum)

if __name__=="__main__":
    f(1,20)
    f(10,30)