number= int(input('How many terms ? :'))
n1,n2= 0,1
count= 0
if number<=0:
    print('Please enter possitive integer')
elif number==1:
    print('Fibonacci sequence upto',number,':')
    print(n1)
else:
    print('Fibonacci sequence:')
    while count<number:
        print(n1)
        nth=n1+n2
        #update values
        n1=n2
        n2=nth
        count+=1
