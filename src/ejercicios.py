
def factorial (num):
    if num == 0:
        return 1
    elif num < 0:
        return -1
    else:
        resultado=1
        for i in range (1,num+1):
            resultado*= i 
        return resultado
  
def leapYear (year):
    if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
        return 1
    else:
        return -1

def daysInMonth (month, year):
    if month > 12 or month < 0 or year < 0:
        return -1
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2:
        if leapYear(year) == 1:
            return 29
        else: 
            return 28
    else:
        return 30

def dayOfWeek (day, month, year):
    a = int((14 - month) / 12)
    y = year - a
    m = month + 12 * a - 2
    d = (day + y + int(y/4) - int(y/100) + int(y/400) + int((31*m)/12)) % 7
    return int(d)

def myPower (num1, num2):
    if num2 < 0:
        return -1
    elif num2==0:
        return 1
    else:
        resultado= num1
        for i in range (1, num2):
            resultado *= num1
        return resultado

def numberOfNumbers (num):
    contador= 0
    if num < 0:
        return -1
    elif num == 0:
        return 1
    while num > 0:
        num= int(num / 10)
        contador += 1
    return contador

def isPrime (num):
    if num <= 0:
        return -1
    else:
        flag= True
        for i in range (2, num):
            if num % i == 0:
                flag= False
        if flag==True:
            return 1
        else: 
            return 0
        
def secondOrder (num1, num2, num3):
    resultado= (num2*num2) - 4 * (num1 * num3)
    if resultado == 0:
        return 1
    elif resultado > 0:
        return 2
    else:
        return 0
    
def numberDivisorPrime (num):
    contador= 0
    for i in range (1,num):
        if num % i == 0:
            contador += isPrime(i)
    return contador

def friend (num1, num2):
    if num1 < 0 or num2 < 0:
        return False 
    divisor= 0
    for i in range (1, num1+1):
        if num1 % i == 0:
            divisor += i
    if divisor - num1 == num2:
        return True
    else:
        return False
        