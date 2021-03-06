from math import *
'----------------------------------------------------'
'question 1'

def XNor(first_bol,sec_bol) :
    if first_bol==sec_bol:
        return True
    else:
        return False

'----------------------------------------------------'
'question 2'
def MinFinder(user_value):
    minimum = user_value % 10 #save the first number as minimum number
    while user_value != 0:
        if (user_value % 10 ) < minimum:# if true , save the new minimum number 
            minimum = user_value % 10 #save new number 
        user_value = user_value//10 # for check the next digit 
    return minimum

def RemoveMinDigit(Number):
    if Number < 0:
        print("bad input!!, the number you entered is not positive\n")
    if Number % 1 != 0:
        print("bad input!!, not a integer number\n")
        return
    min_num = MinFinder(Number) 
    new_number = 0
    counter = 1 #for save the position
    while Number != 0:
            if Number % 10 != min_num:
                new_number = new_number + int((Number % 10 * counter)) #add new digit 
                counter = counter * 10
            Number = Number // 10
    return int(new_number)




'----------------------------------------------------'
'question 3'

def SquareArea(α,γ,a,b,c,d):
    s = (a+b+c+d)*0.5 #half Scope
    α = radians(α) #degree to rad
    γ = radians(γ) #degree to rad
    return sqrt((s-a)*(s-b)*(s-c)*(s-d)-0.5*a*b*c*d*(1+cos(α+γ)))


'----------------------------------------------------'
'question 4'
def CheckArithmeticSeries(Number) :


    difference = Number % 10- (Number // 10) % 10 #(n+1)-(n)

    while int(Number) != 0:

        if int(Number) < 10:
            Number = int(Number) / 10
        elif int((Number % 10))-(Number// 10) % 10 == difference:
            Number= Number//10
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
'question 6'

def num_of_upper(string):

    counter = 0 # for count the capital letters in string
    for index in range(len(string)):
        if ord(string[index]) >= ord('A') and ord(string[index]) <= ord('Z'): #uf true its capital
            counter += 1 #count the letter 

    return counter

def num_of_lower(string):

    counter = 0 # for count the lower case letters in string
    for index in range(len(str(string))):
        if ord(string[index]) >= ord('a') and ord(string[index]) <= ord('z'): #if true its lower case letter in string
            counter += 1 #count the letter 

    return counter


def CalcUpperCalcLower(string):
    print('Number of Upper cases: '+ str(num_of_upper(string)))
    print('Number of Lower cases: '+ str(num_of_lower(string)))


'----------------------------------------------------'
'question 7'

def PerfectNumber(number):
    sum = 0 #Save the sum of all the divisors of the number

    for chk_num in range(1, number):
        if (number % chk_num) == 0:
            sum += chk_num
    if number == sum:
        return True
    return False
'----------------------------------------------------'
'question 8'
def IsPangrams(string):
    end_list = '\0'
    latter_diff = ord('a')-ord('A')# using for check other case
    latter_list = [] #for save the letters in the string , capital or lower and not capital and lower
    counter_list = 0 # for count the number of letter we save if we rich to 26 its pandrom
    for index in range(len(string)):
        lower = ord(string[index]) >= ord('a') and ord(string[index]) <= ord('z')# if true its lower-case letter
        capital = ord(string[index]) >= ord('A') and ord(string[index]) <= ord('Z')# if true its capital letter

        if lower:
            if value_in_list(string[index], latter_list) == False and value_in_list(chr(ord(string[index] )- latter_diff), latter_list) == False:
                    latter_list.insert(0, string[index])
                    counter_list += 1
        if capital:
            if value_in_list(string[index], latter_list) == False and value_in_list(chr(ord(string[index]) + latter_diff), latter_list) == False:
                    latter_list.insert(0, string[index])
                    counter_list += 1

    if counter_list == 26:
        return True

