from nota import nota

def intercala(notas, inicio, meio, fim):
    resultado = []
    atual = 0
    atual1 = inicio
    atual2 = meio

    while atual1 < meio and atual2 < fim:
        nota1 = notas[atual1].get_nota()
        nota2 = notas[atual2].get_nota()

        if(nota1 < nota2):
            resultado.insert(atual, notas[atual1])
            atual1 += 1
        else:
            resultado.insert(atual, notas[atual2])
            atual2 += 1

        atual += 1

    while (atual1 < meio):
        resultado.insert(atual, notas[atual1])
        atual += 1
        atual1 += 1

    while (atual2 < fim):
        resultado.insert(atual, notas[atual2])
        atual += 1
        atual2 += 1

    del notas[inicio:fim]
    for x in range(len(resultado)):
        notas.insert(x + inicio, resultado[x])

    return notas

notas = [nota("andre",4),nota("mariana",5),nota("carlos",8.5),nota("paulo",9),nota("jonas",3),nota("juliana",6.7),nota("guilherme",7),nota("lucia",9.3),nota("ana",10)]

rank = intercala(notas, 0, 4, len(notas))

for alunos in notas:
    print(alunos.get_aluno(),alunos.get_nota())
