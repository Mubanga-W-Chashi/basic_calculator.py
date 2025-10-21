# from usr_inp import usr_ipt
# from operations import add,sub,div,rmdr,pwr,flr_div
# name = input('Enter name: ')
# print('Hello ' + name + ' welcome to basic calculator')
# a , b = usr_ipt()

# # add(a,b)
# # sub(a,b)
# # div(a,b)
# # rmdr(a,b)
# # pwr(a,b)
# # flr_div(a,b)

from usr_inp import usr_inp
from operations import add,sub,div,multp,pwr,fl_div,remdr

name = input('Enter name: ').strip().title()
print(f'Hello {name}, Welcome to basic calculator! \n')

operation = input('Kindly choose and Operation from the options listed below: \n add \n sub \n div \n multp \n pwr \n fl_div \n remdr \n Your choice: ')
a , b = usr_inp()
feed = operation.lower()

#try adding the operators to the 'or' list
if feed in ('add','addition'):
    print(add(a,b))

elif feed in ('sub','subtract'):
    print(sub(a,b))

elif feed in ('pwr','power'):
    print(pwr(a,b))

elif feed in ('multp','multiplication','multiply'):
    print(multp(a,b))

elif feed in ('remdr','remainder'):
    print(remdr(a,b))

elif feed in ('flr_div','floor division'):
    print(fl_div(a,b))

elif feed in ('div','division'):
    print(div(a,b))
else:
    print('Invalid operation. Please try again. ')


# elif feed == 'div' or 'division':
#     print(div(a,b))

#print(feed)
#print(a)
# print(operation)

#     print('Error: wrong input format. Input a word value')
# if isinstance(operation,str) is not True: