name = input("Qual seu nome? ")
number = int(input("Quantos anos voce tem?"))

if number >= 18:
    print("Ola {name}, Voce e maior de idade")
elif number == 16 or number == 17:
    print("Voce esta quase de maior")
else:
    print("Voce e de menor ainda lerdão")