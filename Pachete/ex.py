# Opening a file 
f = open("test.txt") 
Count = 0
Content = f.read() 
CoList = Content.split("\n") 
  
for i in CoList: 
    if i: 
        Count += 1
          
print("Numarul de linii din fisier") 
print(Count) 