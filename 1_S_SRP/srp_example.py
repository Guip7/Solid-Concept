class Process:
    def execute(self, username: str, password: str) -> None:
        if self.__verify_input_data(username, password):
            self.__verify_database(username)
            self.__insert_newUser(username, password)
        else:
            self.__raise_errors("Dados Inválidos")

    def __verify_input_data(self, username: str, password:str) -> bool:
        return isinstance(username, str) and isinstance(password, str)
    
    def __verify_database(self, username: str) -> None:
        print("Acessando o Banco de dados...")
        print("validando credencias...")

    def __insert_newUser(self, username:str, password:str) -> None:
        print("usuario cadastrado com sucesso")

    def __raise_errors(self, message: str) -> None:
        raise Exception(message)
    
process = Process()
process.execute("Guilherme", "Guip")