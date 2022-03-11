#assignment7: write a password generator of total length 15 using , 
#6:digit 3 :lowercase letters, 3: uppercase letters,
# 3 :special characters(#,$,&,!,@)

import random
password_length=15

sam1='abcdefghijklmnopqrstuvwxyz'
sam2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sam3='123456789'
sam4='#$&!@'
password=""

p1= "".join(random.sample(sam1,3))
p2= "".join(random.sample(sam2,3))
p3= "".join(random.sample(sam3,6))
p4= "".join(random.sample(sam4,3))

for index in range(password_length):
	password= p1+p2+p3+p4
	
print("password generated: {}".format(password))
