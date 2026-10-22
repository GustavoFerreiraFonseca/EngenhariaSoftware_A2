# classe dos atendimentos
class Atendimento:
    def __init__(self):
        # atributos privados da classe
        self.__id_atendimento = None
        self.__id_aluno = None
        self.__disciplina = ""
        self.__data_hora = None
        self.__status = "LIVRE" # (LIVRE, RESERVADO e CANCELADO)

    # Metodos da classe
    # metodo que verifica se o atendimento está disponivel, ou seja se o status está como "LIVRE"
    def esta_disponivel(self):
        if self.__status == "LIVRE":
            return True
        return False

    # Metodos que reserva o atendimento com um aluno
    def reservar(self, id_aluno):
        if not self.esta_disponivel():
            raise ValueError("Atendimento não disponivel")

        self.__status = "RESERVADO"
        self.__id_aluno = id_aluno


    # getters
    def get_id_atendimento(self):
        return self.__id_atendimento

    def get_id_aluno(self):
        return self.__id_aluno

    def get_disciplina(self):
        return self.__disciplina
        
    def get_data_hora(self):
        return self.__data_hora

    def get_status(self):
        return self.__status


    # setters
    def set_id_atendimento(self, id_atendimento):
        self.__id_atendimento = id_atendimento

    def set_id_aluno(self, id_aluno):
        self.__id_aluno = id_aluno

    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina

    def set_data_hora(self, data_hora):
        self.__data_hora = data_hora

    def set_status(self, status):
        self.__status = status