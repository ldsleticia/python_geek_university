from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


user1 = Usuario("Angelina", "Jolie", "angelina@gmail.com", "123456")

nome = input("Informe seu nome: ")
sobrenome = input("Informe o sobrenome")
email = input("Informe o email")
senha = input("Informe a senha")
confirma_senha = input("Confirme a senha")

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print("Senha não confere")
    exit(42)

print("Usuário criado com sucesso")

senha = input("Informe a senha para acesso")
if user.checa_senha(senha):
    print("Acesso permitido")
else:
    print("Acesso negado")
