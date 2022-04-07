lista = []
soma = 0
qt = input('Quantidade de notas ')

#append (acrescentar na lista)
for n in range(0,int(qt)): 
    lista.append(int(input(f"Nota do jurado {n+1} ")))

print ('Maior número da lista: ', max(lista))   
print ('Menor número da lista: ', min(lista))  

#faz a soma dos itens na lista e resulta na soma
for number in lista:
    soma += number
  
# subtrai o valor maximo e minimo e divide por 8 para tirar a média entre as 8 notas validas
soma = (soma - max(lista) - min(lista)) / 8
print (soma)
