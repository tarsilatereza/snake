# EXEMPLOS
n1 = input("type a number: ")
n2 = input("type other number: ")
s = n1 + n2
print("the sume is ", s)
#CONSOLE:
#> type a number:2
#> type other number3
#> the sume is  23

n1 = int(input("type a number: "))
n2 = int(input("type other number: "))
s = n1+ n2
print("the sume is ", s)
#CONSOLE
#> type a number: 2
#> type other number: 3
#> the sume is  5

print("the sume between {} and {} is {}".format(n1, n2, s))
#CONSOLE
#> the sume between 2 and 3 is 5

v = bool(input('type a value: '))
print(v)
#CONSOLE
#> type a value:
#> False

#> type a value: 9
#> True

a = input('type something: ')
print(a.isnumeric()) #isalpha/#isalnums
#CONSOLE
#type something: hi lorena
#False

#type something: 8
#True

