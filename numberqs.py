# #reverse of a number

# def reverse(number):
#     reverse = 0
#     while number > 0:
#         digit = number % 10
#         reverse = reverse * 10 + digit
#         number = number // 10
#     return reverse
# print(reverse(12345))
        
# number is palindrome

# def palindrome(number):
#     original = number
#     reverse = 0
#     while number > 0:
#         digit =  number % 10
#         reverse = reverse * 10 + digit
#         number = number // 10
    
#     if reverse == original:
#         return "it is a palindrome"
#     else:
#         return "not a palindrome"

# print(palindrome(12321))


# count digits in a number

# def digit(number):
#     count = 0
#     while number > 0:
#         number = number // 10
#         count += 1
        
#     return count
# print(digit(12345))


# sum of digits

# def sumdigit(number):
#     sum = 0
#     while number > 0:
#         digit = number % 10
#         sum = sum + digit
#         number = number // 10
#     return sum
# print(sumdigit(123))


# product of digits

# def prodDigits(number):
#     prod = 1
    
#     while number > 0:
#         digit = number % 10
#         prod = prod * digit
#         number = number // 10
#     return prod
# print(prodDigits(1234))

# armstrong of a number  

# def armstrong(number):
#     original = number
#     arm = 0
#     while number > 0:
        
#         digit = number % 10
#         arm = arm + (digit ** 3)
#         number = number // 10
    
#     if arm == original:
#         return "it is an armstrong number"
#     else:
#         return "it is not an armstrong number"
# print(armstrong(1523))

# factorial of a number

# def factorial(number):
#     fact = 1
#     for i in range(1,number+1):
#         fact = fact * i
#     return fact

# print(factorial(3))
    
    
# multiplication table
# def table(number):
#     for i in range(1,11):
#         print( number * i )
# table(2)

    
# prime number

# def prime(number):
#     if number <=1 :
#         return "not a prime"
    
#     for i in range(2,int(number / 2)):
#         if number % 2 == 0:
#             return "not a prime"
#         else:
#             return "it is a prime"
# print(prime(7))


# check prime numbers till n

# def checkPrimeN(number):
#     prime = []
    
#     for i in range(2,number+1):
#         is_prime = True
#         for j in range(2,int(i**0.5)+1):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime.append(i)
#     return prime
# print(checkPrimeN(10))         


# perfect number
# def perfect(number):
#     sum = 0
#     for i in range(1,number):
#         if  number%i == 0:
#             sum+=i
    
#     if number == sum:
#         return "it is a perfect number"
#     else:
#         return "not a perfect number"    
# print(perfect(496))
    
# fibonacci  
# def fibonacci(number):
#     a,b = 0,1
#     for i in range(number):
#         print(a,end=" ")
#         a,b=b,a+b
# fibonacci(10)



# strong number

# def strong(number):
#     def factorial(n):
#         fact = 1
#         for i in range(1,n+1):
#             fact=fact*i
#         return fact
    
#     total = 0
#     temp = number
    
#     while temp > 0:
#         digit = temp % 10
#         total += factorial(digit)
#         temp = temp // 10
#     if total == number:
#         return "it is a strong number"
#     else:
#         return "not a strong number"
        
# print(strong(145)) 