def Num_lit_cifre(str):
    nums = 0
    letter = 0
    other = 0
    for i in str :
        if i.isalpha():
            letter+=1
        elif i.isdigit():
            nums+=1
        else:
            other+=1
    return nums,letter,other

x = input("Introduceti un text: ")
print (Num_lit_cifre(x))
