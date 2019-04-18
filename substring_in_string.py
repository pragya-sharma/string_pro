'''
Aim: In this challenge, the user enters a string and a substring.
     You have to print the number of times that the substring
     occurs in the given string.
'''
     
s = input("enter string")
sub = input("enter substring of str")
if sub in s:
    print("subsrting is ",s.count(sub),"times in string")
    
