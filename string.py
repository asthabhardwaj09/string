## here we can use triple inverted columa insented of escape sequence (new line)
# and also we can use triple inverted column if we want more than one inverted columa in a same statement  

a= "my name is astha bhardwaj. \"currently\"\n i m pursuing my gradution from btech with data science"
print(a)
print(type(a))
b="""ravita is my friend and 
i want to be with her everytime"""
print(b)
print(type(b))
c= """ansikha love salman very much but "she" cannot "exprees" her feeling to "ravita" """
print(c)
print(type(c))

### we can see we have used in line 17 single inverted columa in a same statement it will not cause any error because
##  we used double inverted columa for first and last statement

## vice versa for line 17 

d="ravita also 'love' suhani but she do not want to tell her feelings to astha"
print(d)
print(type(d))
e='''princess also "love" prince but 
she do not want to tell her feelings to astha'''
print(e)
print(type(e))

###  here all the above code is string
### anything write inside a double or single inverted columa than it is a string

# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])

print("lets start for loop\n")

for character in a:
    print(character)
    
## form line 31 to 36 we cannot use this index becuase it will take a time also we must know about total index
###if we do not know an we cross than it will throw an error
## therefor we use for loop