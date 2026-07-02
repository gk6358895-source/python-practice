'''s="rahul like python"
vowels="aeiou"
count=0
ans=""
for i in s:
    if i in vowels:
        count+=1
        ans+=i
print(ans,count)
'''

s="rahul$$$ like pyth235on"
vowels="aeiou"
c=0
v=0
n=0
sym=0
sp=0

for i in s:
    if i.isalpha():
        if i in vowels:
            v+=1
        else:
            c+=1 
    elif i.isdigit():
        n+=1
    elif i.isspace():
        sp+=1

    else:
        sym+=1

print("Vowels:", v)
print("Consonants:", c)
print("Digits:", n)
print("Spaces:", sp)
print("Special Characters:", sym)
