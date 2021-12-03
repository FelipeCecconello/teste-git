class nota:

    def __init__(self, aluno, nota=0):
        self.aluno = aluno
        self.nota = nota


    def get_nota(self):
        return self.nota

    def set_nota(self, nota):
        self.nota = nota

    def get_aluno(self):
        return self.aluno


