from nota import nota

def junta(notas_alberto, notas_mauricio):
    resultado = []
    atual_mauricio = 0
    atual_alberto = 0
    atual = 0

    while (atual_alberto < len(notas_alberto) and atual_mauricio < len(notas_mauricio)):

        nota1 = notas_mauricio[atual_mauricio].get_nota()
        nota2 = notas_alberto[atual_alberto].get_nota()

        if (nota1 < nota2):
            resultado.insert(atual,notas_mauricio[atual_mauricio])
            atual_mauricio += 1
        else:
            resultado.insert(atual,notas_alberto[atual_alberto])
            atual_alberto += 1
        atual += 1

    while(atual_alberto < len(notas_alberto)):
        resultado.insert(atual, notas_alberto[atual_alberto])
        atual += 1
        atual_alberto += 1

    while (atual_mauricio < len(notas_mauricio)):
        resultado.insert(atual, notas_mauricio[atual_mauricio])
        atual += 1
        atual_mauricio += 1

    return resultado

notas_mauricio = [nota("andre",4),nota("mariana",5),nota("carlos",8.5),nota("paulo",9)]
notas_alberto = [nota("jonas",3),nota("juliana",6.7),nota("guilherme",7),nota("lucia",9.3),nota("ana",10)]

rank = junta(notas_alberto, notas_mauricio)
for nota in rank:
    print(nota.get_aluno(),nota.get_nota())

