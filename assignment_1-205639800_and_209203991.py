
'----------------------------------------------------'
'question 1'

def XNor(first_bol,sec_bol) :
    if first_bol==sec_bol:
        return True
    return False

'----------------------------------------------------'
'question 2'

def MinFinder(user_value):
    minimum = user_value % 10
    while user_value != 0:
        if (user_value % 10 ) < minimum:
            minimum = user_value % 10
        user_value = int(user_value/10)
    return minimum

def RemoveMinDigit(Number):
    if Number < 0:
        print("bad input!!, the number you entered is not positive\n")
    if Number % 1 != 0:
        print("bad input!!, not a integer number\n")
        return
    min_num = MinFinder(Number)
    print('min is ' + str(min_num)+' \n')
    new_number = 0
    counter = 1
    while Number != 0:
            if Number % 10 != min_num:
                new_number = new_number + int((Number % 10 * counter))
                counter = counter * 10
            Number = int(Number / 10)
    return int(new_number)



x = input('please enter number:\n')
print(RemoveMinDigit(int(x)))
'----------------------------------------------------'
'question 3'



'----------------------------------------------------'
'question 4'
def CheckArithmeticSeries(Number) :
    if Number == 0:
        return  False
    Number = int(Number)
    dist = int((Number % 10))-int(((int(Number) / 10) % 10)) #(n+1)-(n)
    while int(Number) != 0:
        if int((Number % 10))-int(((int(Number) / 10) % 10)) == dist:
            Number =int(Number) / 10
        else:
            return False

    return True

x=input('enter number:\n ')
print('the answer is:'+ str(CheckArithmeticSeries(int(x))))
'----------------------------------------------------'
'----------------------------------------------------'
'----------------------------------------------------'
