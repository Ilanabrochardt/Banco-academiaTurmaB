from AcademiaBiblioteca import *
print(banco)

command = int(input("digite as opções: \nDELETAR: \n(1)ALUNO \n(2)FUNCIONÁRIO \n(3)MODALIDADE \n(4)PERSONAL \nINSERIR:"
                "\n(5)ALUNO \n(6)FUNCIONÁRIO \n(7)MODALIDADE \n(8)PERSONAL \nCONSULTAR: \n(9)ALUNO \n(10)FUNCIONÁRIO \n(11)MODALIDADE \n(12)PERSONAL \n"))
match command:
    case 1:
        matricula = input("Digite a matricula do aluno que deseja deletar: ")
        deletarAluno(matricula)
    case 2:
        id_funcionario = input("Digite o id_funcionario do aluno que deseja deletar: ")
        deletarFuncionario(id_funcionario)
    case 3:
        ID_modalidade = input("Digite o ID_modalidade do aluno que deseja deletar: ")
        deletarModalidade(ID_modalidade)
    case 4:
        CPF = input("Digite o CPF do personal que deseja deletar: ")
        deletarPersonal(CPF)
    case 5:
         nomeAluno = input("Digite o nome do aluno que deseja inserir: ")
         telefoneAluno = input("Digite o telefone do aluno que deseja inserir:")
         cpfAluno = input("Digite o cpf do aluno como que deseja inserir: ")
         emailAluno = input("Digite o email do aluno que deseja inserir: ")
         inserirAluno(nomeAluno, telefoneAluno, cpfAluno, emailAluno)
    case 6:
        nomeFuncionario =input("Digite o nome do funcionário que deseja inserir:")
        cpfFuncionario =input("Digite o cpf do funcinário que deseja inserir:")
        departamentoFuncionario =input("Digite o departamento do fucnionário que deseja inserir:")
        salarioFuncionario =input("Digite o salário do funcionário que deseja inserir:")
        numero_filhosFuncionario =input("Digite a quantidade de filhos que esse funcinarios tem,que deseja inserir: ")
        inserirFuncionario(nomeFuncionario, cpfFuncionario, departamentoFuncionario, salarioFuncionario,
                           numero_filhosFuncionario)
    case 7:
        nomeModalidade = input("Digite o nome da modalidade que deseja inserir: ")
        duracaoModalidade = input("Digite a duração da modalidade que deseja inserir: ")
        inserirModalidade(nomeModalidade, duracaoModalidade)
    case 8:
        cpfPersonal = input("Digite o cpf do personal que deseja inserir: ")
        crefPersonal = input("Digite o cref do personal que deseja inserir: ")
        nomePersonal = input("Digite o nome do personal que deseja inserir: ")
        telefonePersonal = input("Digite o telefone que deseja inserir: ")
        enderecoPersonal = input("Digite o endereço do personal que deseja inserir: ")
        inserirPersonal(cpfPersonal, crefPersonal, nomePersonal, telefonePersonal, enderecoPersonal)
    case 9:
        print("Consulte abaixo a tabela de ALUNOS:")
        consultarAlunos()
    case 10:
        print("Consulte abaixo a tabela de FUNCIONARIOS:")
        consultarFuncionarios()
    case 11:
        print("Consulte abaixo a tabela de MODALIDADES:")
        consultarModalidades()
    case 12:
        print("Consulte abaixo a tabela de PERSONAIS:")
        consultarPersonal()


meucursor.close()
banco.close()
