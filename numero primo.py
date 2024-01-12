n= int(input("Escribe un numero: "))
valor= range(2,n)
contador = 0

for i in valor:
  if n % i == 0:
    contador +=1
    
    if contador > 0 :
      print("El numero no es primo" )
    else:
      print("El numero es primo")