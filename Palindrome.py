name = 'racecar'
is_palindrome=True
i=0
j=len(name)-1
print(j)
while(i<=j):
    if name[i]==name[j]:
        i+=1
        j-=1
    else:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not")