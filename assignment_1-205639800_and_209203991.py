
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




'----------------------------------------------------'
'question 3'



'----------------------------------------------------'
'question 4'
def CheckArithmeticSeries(Number) :

    Number = int(Number)
    dist = int((Number % 10))-int(((int(Number) / 10) % 10)) #(n+1)-(n)

    while int(Number) != 0:

        if int(Number) < 10:
            Number = int(Number) / 10
        elif int((Number % 10))-int(int(Number/ 10) % 10) == dist:
            Number= int(Number)/10
        else:
            return False
    return True



'----------------------------------------------------'
'question 5'


def CanBeTriangle(num1,num2,num3):
    try:
        if float(num1) < 0 or float(num2) < 0 or float(num3) < 0:
            return False
        if float(num1) + float(num2) <float(num3):
            return False
        if float(num1) + float(num3) <float(num2):
            return False
        if float(num3) + float(num2) <float(num1):
            return False
        return True
    except:
        print('bad input!!\n')

'----------------------------------------------------'
'----------------------------------------------------'
