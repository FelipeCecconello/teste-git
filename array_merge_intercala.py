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

def ordena(notas,inicio,fim):
    quantidade = fim - inicio
    if(quantidade > 1):
        meio = int((inicio + fim) / 2)
        ordena(notas, inicio, meio)
        ordena(notas, meio, fim)
        intercala(notas, inicio, meio, fim)

def busca(notas, inicio, fim, buscando):
    if inicio > fim:
        return -1

    meio = int((inicio + fim) / 2)
    nota = notas[meio]
    if(buscando == nota.get_nota()):
        return meio
    if(buscando < nota.get_nota()):
        return busca(notas,inicio,meio-1,buscando)
    return busca(notas,meio+1,fim,buscando)

notas = [nota("juliana",6.7),nota("andre",4),nota("carlos",8.5),nota("mariana",5),nota("ana",10),nota("paulo",9),nota("jonas",3),nota("guilherme",7),nota("lucia",9.3)]

ordena(notas,0,len(notas))
encontrei = busca(notas, 0, len(notas), 9.3)

print("Encontrei a nota no indice ",encontrei)
for alunos in notas:
    print(alunos.get_aluno(),alunos.get_nota())

print("!!!!!Testando servidor git!!!!!!")