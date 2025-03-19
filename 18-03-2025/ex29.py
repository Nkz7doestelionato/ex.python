def exibir_menu():
    print("Bem vindo ao menu de cadastro")
    print("1 - novo cadastro")
    print("2 - ver cadastro")
    print("3 - sair")
    print("---------------------------------")

def cadastrar_pessoa(cadastros):
    nome = input("Nome:")
    idade = input("Idade:")
    turma = input("Turma:")
    curso = input("Curso:")
    cadastros.append({"Nome": nome, "idade": idade, "turma": turma, "curso": curso})
    print("Cadastro realizado com sucesso!")

def ver_cadastros(cadastros):
    if not cadastros:
        print("Nenhum cadastro realizado!")
    else:
        print("\n ------ LISTAS DE CADASTRO ------")

        for i, pessoa in enumerate (cadastros, 1):
            print(f"{i}. Nome: {pessoa['nome']}, idade: {pessoa['idade']}, turma: {pessoa['turma']}, curso: {pessoa['curso']}")

def main():
    cadastros = []
    while True:
        exibir_menu()
        opção = input("escolha uma opção:")
        if opção == "1":
            cadastrar_pessoa (cadastros)
        elif opção == "2":
            ver_cadastros (cadastros)
        elif opção == "3":
            print("Obrigado por utilizar o sistema de cadastro.")
            break

        else:
            print("opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()