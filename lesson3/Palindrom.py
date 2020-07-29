def Palindrome(sir): 
    return sir == sir[::-1] 
  
  
sir = "minim"
inv = Palindrome(sir) 
  
if inv: 
    print("Cuvintul " + sir + " e palindrom") 
else: 
    print("Cuvintul " + sir + " nu e palindrom") 