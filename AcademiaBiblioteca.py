import mysql.connector
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="302302",
    database="academiaturmab"
)
meucursor = banco.cursor()
def pesquisar():
    # o fetchall recebe tudo da pesquisa e retona através de uma tupla
    resultado = meucursor.fetchall()
    for x in resultado:
       print(x)


def inserirAluno(nomeAluno, telefoneAluno, cpfAluno, emailAluno):
    #Aqui é para colocar as informações referente a como esta no sql, criando objetos com a função inserir e informações e colocando no cursos no banco.
    sql = "insert into alunos (nome,telefone,cpf,email) values(%s,%s,%s,%s)"
    data = (nomeAluno, telefoneAluno, cpfAluno, emailAluno)
    meucursor.execute(sql, data)
    banco.commit()

def inserirFuncionario(nomeFuncionario, cpfFuncionario,departamentoFuncionario, salarioFuncionario,numero_filhosFuncionario):
    #Aqui é para colocar as informações referente a como esta no sql, criando objetos com a função inserir e informações e colocando no cursos no banco.
    sql = "insert into funcionarios (nome,cpf,departamento,salario,numeros_filhos) values(%s,%s,%s,%s,%s)"
    data = (nomeFuncionario, cpfFuncionario, departamentoFuncionario, salarioFuncionario, numero_filhosFuncionario)
    meucursor.execute(sql, data)
    banco.commit()

def inserirModalidade(nomeModalidade, duracaoModalidade):
    sql = "insert into modalidades (nome,duracao) values(%s,%s)"
    data = (nomeModalidade, duracaoModalidade)
    meucursor.execute(sql, data)
    banco.commit()

def inserirPersonal(cpfPersonal,crefPersonal, nomePersonal, telefonePersonal, enderecoPersonal):
    sql = "insert into personal (cpf,cref,nome,telefone,endereco) values(%s,%s,%s,%s,%s)"
    data = (cpfPersonal, crefPersonal, nomePersonal, telefonePersonal, enderecoPersonal)
    meucursor.execute(sql, data)
    banco.commit()

def deletarAluno(matricula):
    sql = "delete from alunos where matricula = (%s)"
    data = (matricula,)
    meucursor.execute(sql, data)
    banco.commit()

def deletarFuncionario(id_funcionario):
    sql = "delete from funcionarios where id_funcionario = (%s)"
    data = (id_funcionario,)
    meucursor.execute(sql, data)
    banco.commit()

def deletarModalidade(ID_modalidade):
    sql = "delete from modalidades where ID_modalidade = (%s)"
    data = (ID_modalidade,)
    meucursor.execute(sql, data)
    banco.commit()

def deletarPersonal(CPF):
    sql = "delete from personal where CPF = (%s)"
    data = (CPF,)
    meucursor.execute(sql, data)
    banco.commit()

def consultarAlunos():
    print("TABELA DE ALUNOS:\n")
    pesquisaAlunos = "select * from alunos;"
    meucursor.execute(pesquisaAlunos)
    pesquisar()

def consultarFuncionarios():
    print("TABELA DE FUNCIONARIOS:\n")
    pesquisaFuncionarios = "select * from funcionarios;"
    meucursor.execute(pesquisaFuncionarios)
    pesquisar()

def consultarModalidades():
    print("TABELA DE MODALIDADES:\n")
    pesquisaModalidades = "select * from modalidades;"
    meucursor.execute(pesquisaModalidades )
    pesquisar()

def consultarPersonal():
    print("TABELA DE PERSONAL:\n")
    pesquisaPersonal = "select * from personal;"
    meucursor.execute(pesquisaPersonal)
    pesquisar()


