"""
#print("Aprendendo como utilizar cometário")
print("Primeira linha") #aqui é um comentário que não será interpretado
#print("Segunda linha")


print("Aprendendo como utilizar cometário")
print("Primeira linha")

print("Segunda linha")


num_int = 5
num_dec = 7.3
val_str = "qualquer texto"

print (num_int)

print ("o valor é:", num_int)
print ("o valor é: %i" %num_int)
print ("o valor é: " + str(num_int))

print ("o valor é:", num_dec)
print ("o valor é: %.10f" %num_dec) #%.10f especifica a quantiade de casas decimais a serem colocadas depois da vírgula
print ("o valor é: " + str(num_dec))

print ("Concatenando string", val_str)
print ("Concatenando string %s" %val_str)
print ("Concatenando string:" + val_str)

"""

login = input("Login:")
senha = input("Senha:")

print ("O usuário informado foi: %s, e a senha foi: %s" %(login,senha))

