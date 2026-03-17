#Aufgabe 1 ###################################################################################
user_name = input("What is your name: ")
user_age = input("How old are you: ")
print("Hallo, ich heiße ", user_name, "und ich bin ", user_age, "Jahre alt")

#Aufgabe 2######################################################################################

m = int(input("Geben Sie eine Nummer m > 0: "))
n = int(input("Geben Sie eine Nummer n > 0: "))
whole_number = m//n
remainder = m%n

print("Der ganze Teil von der Division ist", whole_number, "und der Rest ist ", remainder)

#Aufgabe 3 #######################################################################################

pi = 3.14159
x_1 = 3
x_2 = 3.14
x_3 = 22/7
x_4 = 333/106

approximation = abs(pi - x_1)/pi 
error_prozent = approximation * 100
print(f"Pi kann durch {x_1} approximiert werden mit einem relativen Fehler von {approximation:.4f}. Das entspricht {error_prozent:.2f}%")

approximation = abs(pi - x_2)/pi
error_prozent = approximation * 100
print(f"Pi kann durch {x_2} approximiert werden mit einem relativen Fehler von {approximation:.4f}. Das entspricht {error_prozent:.2f}%")


approximation = abs(pi - x_3)/pi
error_prozent = approximation * 100
print(f"Pi kann durch {x_3:.4f} approximiert werden mit einem relativen Fehler von {approximation:.4f}. Das entspricht {error_prozent:.2f}%")


approximation = abs(pi - x_4)/pi
error_prozent = approximation * 100
print(f"Pi kann durch {x_4:.5f} approximiert werden mit einem relativen Fehler von {approximation:.4f}. Das entspricht {error_prozent:.3f}%")

# Aufgabe 4 ######################################################################

x = int(input("Geben Sie eine Nummer x > 0: "))
y = int(input("Geben Sie eine Nummer y > 0: "))

if x>y:
    print(x, " ist größer")
elif x<y:
    print(y, " ist größer")
else:
    print(x, " ist gleich ", y)

# Aufgabe 5 #######################################################################

a_kanten = int(input("Geben Sie die 'a' Kantenlänge: "))
b_kanten = int(input("Geben Sie die 'b' Kantenlänge: "))
c_kanten = (a_kanten ** 2 + b_kanten ** 2) ** 0.5
print("Die Hypotenuse hat die Länge: ",c_kanten)

# Aufgabe 6 ########################################################################

n = int(input("Geben Sie eine nummer  n > 0: "))
zeile1 = "0 " * n
zeile2 = " 0" * n
i = n//2

if n >0 and n%2 == 0:
    print(f"{zeile1} \n {zeile2} \n" * i)
else:
    print("n ist nicht gerade ")