'''
comparison operators in pthon
'''
# x=int(input("enter the first number: "))
# y=int(input("enter the second number: "))
# if x==y :
#     print(f'{x} and {y} are equal!')
# elif x>y :
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{x} is less than {y}')
# usage=float(input('enter your usage'))
# if usage <= 100:
#     print('your payment is 80 birr')
# elif usage >=100 and usage < 300:
#     print('your payment is 100 birr')
# elif usage >=300 and usage < 600:
#     print('your payment is 150 birr')
# elif usage >=600 and usage < 900:
#     print('your payment is 200 birr')
# else:
#     print('your payment is 300  birr')
'''salary tax'''
sallery=int(input('enter your salary: '))
if sallery<=600:
    print('there is no tax payment')
elif sallery > 600 and sallery <= 1500:
    net_sallery = sallery-((sallery*10)/100)
    print(net_sallery)
else:
    print(' you are in the list of high tax payers ')