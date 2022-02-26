# Metodo estático

from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f"Temos {cls.contador} usuário(s) no sistema")

    @staticmethod
    def definicao():
        return "uxr344".upper()

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


user1 = Usuario("Angelina", "Jolie", "angelina@gmail.com", "123456")
Usuario.conta_usuarios()
