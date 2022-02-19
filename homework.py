#1
hours = input("Enter Hours: ")
rate = input("Enter Rate: ") 
print("Pay: ", float(hours) * float(rate))

#2
Num = ""
Count = 0
Sum = 0
while Num != "done":
    Num = input("Enter a number: ")
    if not Num.isdigit() and Num != "done":
        print("Invalid input")
    elif Num != "done":
        Count += 1
        Sum += float(Num)
    else:
        print("Sum of numbers: ", Sum, "Count of numbers: ", Count, "Arithmetic average: ", Sum/Count)


#3
Letter = input("Enter a letter: ")
smallLetter = Letter.lower()
if smallLetter in "a, e, i, o, u":
    print("The letter is vowel")
elif smallLetter == "y":
    print("The letter is both vowel and consonant")
else:
    print("The letter is consonant") 

#4
letter = input("Enter a letter: ")
number = int(input("Enter a number: "))
if letter in "A, C, E, G" and number%2 != 0 or letter in "B, D, F, H" and number%2 == 0:
    print("black")
else:
    print("white")

#5
TempFar = float(input("Enter temperature: "))
print("TempC: ", (TempFar - 32)/1.8)




