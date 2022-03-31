def get_maior (q, q1):
  if q >= q1 :
    return q
  else: 
    return q1

def get_media (q, q1):
  return (q+q1)/2

def aprovado (media):
  if media >= 6:
    return True

q = float(input("Prova 1\n"))
q1 = float(input("Prova 2\n"))

maior = get_maior(q,q1)
media = get_media(q,q1)
Isaprovado = aprovado(media)


if Isaprovado == True : 
  print("Aprovado ")
else:
  sub = float(input("Digite uma nota substutiva\n"))
  if (sub+maior)/2 >= 6:
    print("Aprovado ") 
  else:
    exame = float(input("Digite a nota de Exame\n"))
    if (exame+media)/2 >= 6:
      print("Aprovado ")
    else:
      print("Conseguiu reprovar ")

