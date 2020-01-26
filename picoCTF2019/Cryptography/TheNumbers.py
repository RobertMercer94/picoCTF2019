letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
flag = ['empty']*24
for i in range (0,7):
    k = input('number: ')
    flag[i]= letters[k-1]
    print(flag[i])
i += 1
flag[i] = '{'
i +=1
while (i < 23):
    k = input('number: ')
    flag[i]= letters[k-1]
    print(flag[i])
    i += 1
flag[i]= '}'
str1= ''
flag = str1.join(flag)
print(flag)
