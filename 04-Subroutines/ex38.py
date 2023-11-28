def f(palindrome):
    length =len(palindrome)
    if palindrome == palindrome[::-1]:
        
        return palindrome[::-1], True
    else:
        return palindrome[::-1], False
    
if __name__=="__main__":
    print(f("radar"))
    print(f("book"))


palindrome = "ABCDF"
print(palindrome[::-1])
