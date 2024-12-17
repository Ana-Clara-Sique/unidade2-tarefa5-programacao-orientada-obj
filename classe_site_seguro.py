class Usuario:
    def __init__(self,nome,idade,telefone,login,senha):
        self.__nome = nome
        self.__idade = idade
        self.__telefone = telefone
        self.__login = login
        self.__senha = senha

    def alterar_telefone(self, novo_telefone , senha_validacao):
        if senha_validacao == self.__senha:
            self.__telefone = novo_telefone
        else:
            print("Senha invalida! Nâo foi possivel alterar o telefone")

    def alterar_login(self,novo_login,senha_validacao):
        if senha_validacao == self.__senha:
            self.__login = novo_login
        else:
            print("senha invalida!Nâo foi possivel alterar o login.")

    def alterar_senha(self,nova_senha, senha_validacao):
        if senha_validacao == self.__senha:
            self.__senha = nova_senha
        else:
            print("Senha invalida! Nâo possvel alterar a senha.")

    def mostrar_dados(self,senha_validacao):
        if senha_validacao ==self.__senha:
            print(f"Nome:{self.__nome}") 
            print(f"Idade: {self.__idade}")
            print(f"Telefone: {self.__telefone}")
            print(f"Login: {self.__login}")
        else:
            print("Senha invalida! Não foi possivel mostrar os dados.")

    def mostrar_dados_publicos(self):
        print(f"Nome : {self.__nome}")
        print(f"Idade:{self.__idade}")

usuario1 = Usuario("Maria" , 30 , "1234-5678" , "Maria123" , "minhasenha")
usuario1.alterar_telefone("9876-5432" , "minhasenha")
usuario1.alterar_login("novologin123", "senhaerrada")
usuario1.mostrar_dados("minhasenha")
usuario1.mostrar_dados_publicos()

        