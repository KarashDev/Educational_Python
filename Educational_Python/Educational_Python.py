print ("Hello, World!")

x = 25
y = 15
print(x + y)

print()
print ("Hello", "World", "Hello", "World")

print('My name is "Ivan"')

print("How", "Are", "You", sep="***") 
print("How", "Are", "You", sep="\t")

print("How", "Are", "You", end="***") 
print("How", "Are", "You", end="\n")

intInString = str(x)
stringInInt = int("35")

#input_num = input()
#print("Your input:", input_num)

#input_num2 = input("Your second input: ")
#print(f"Second input was {input_num2}")

#print(int(input_num) + 25)
#print(str(input_num) + str(25))

var1, var2, var3 = 25, "hi", 125
#var4, var5, var6 = input(), input(), input()

print(var1, var2, var3, sep="---")
#print(var4, var5, var6, sep="---")

a, b = 11, 22
a, b = b, a
print(a, b)

print(2**3)
print(5//2) #2
print(5/2)  #2.5
print(5%2)
print(2 ** 2 ** 3)
print(3 + 4 * 5 ** 2 + 7) #110 (** => * => +-)
print(-123 // 10) #13

num = 25
num += 3
num *= 2
print(num) #56

numToRound = 5.252
print(round(numToRound))
print(round(numToRound, 2))
print(round(numToRound, 1))

q, w = 5, 10
e, r = 15, 20
print(q < w)
print(q < w and e < r)
print(q == w or e == r)
print(q != w) #true
print(not q == w) #true

print(type(q), type(intInString))

strX = "Hello, world!"
substrX1 = "world"
substrX2 = "123"
print(substrX1 in strX) #true
print(substrX2 in strX) #false 
print(substrX2 not in strX) #true

if "Hello" in strX:
    print("Yes, Hello")
elif "hello" in StrX:
    print("Yes, hello")
else: 
    print("No")


numberX = 220;
if numberX < 200:
    if numberX > 100:
        print("Number greater than 100 and less than 200")
    else:
        print("Number less than 100")
else:
    print("Number greater than 200")


stringX = "Hello!"
for char in stringX:
    print(char, end="")
