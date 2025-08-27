# reverse a string

# def reverse(a):
#     return a[::-1]

# print(reverse("hello"))

# reverse of a string using loop

# def reverse(text):
#     reverse = ""
#     for char in text:
#         reverse = char+reverse
#     return reverse
# print(reverse("hello"))

# check if the string is a palindrome

# def palindrome(text):
#     reverse = ""
#     for char in text:
#         reverse = char+reverse
        
#     if reverse == text:
#         return "it is a palindrome"
#     else:
#         return "not a palindrome"
# print(palindrome("apspa"))


# vowels and consonants
# def alphabets(text):
#     vowels = 0
#     consonants = 0
    
#     for char in text:
#             if char in  "aeiouAEIOU":
#                 vowels = vowels + 1
#             else:
#                 consonants = consonants+1
#     return vowels,consonants
# print(alphabets("hello"))



# remove spaces using built in fnc
# def removeSpace(text):
#     return text.replace(" ","")
# print(removeSpace("hello world"))

# remove spaces using loop

# def removeSpace(text):
#     newTxt = ""
#     for char in text:
#         if char == " ":
#             newTxt += ""
#         else:
#             newTxt += char
#     return newTxt
# print(removeSpace("hello world"))


# built in 
# def capitaliseFirst(text):
#     captxt = text.title()
#     return captxt
# print(capitaliseFirst("hello world in this earth"))


# loop
# def cap(text):
#     words = text.split()
#     capi = []
    
#     for word in words:
#         capi.append(word.capitalize())
#     return " ".join(capi)
# print(cap("hello worls from thius eaerr"))


# def anagram(a,b):
#     a = a.lower().replace(" ","")
#     b = b.lower().replace(" ","")

#     if len(a) != len(b):
#         return False
    
#     return sorted(a) == sorted(b)

# print(anagram("listen","silent"))
# print(anagram("listen","silenasdt"))


# occurance of each charvater

# def countchars(text):
#     count = {}
    
#     for char in text:
#         if char in count:
#             count[char] = count[char]+1
#         else:
#             count[char] = 1
#     return count
# print(countchars("hello"))