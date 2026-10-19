from Atendimento import *

# classe de sistema de agendamento 
class SistemaAgendamento:
    def __init__(self):
        # atributos da classe
        self.__atendimentos = {}
        self.__disciplinas = [
            "Fundamentos de programação",
            "Lógica de programação",
            "Cálculo I",
            "Cálculo II",
            "Cálculo III",
            "Engenharia de software"
        ]
        self.__arquivo = "DadosAtendimentos"

        # criando arquivo para guardar os dados dos atendimentos
        with open(self.get_arquivo(), "w", encoding="utf-8") as arquivo:
            arquivo.write("=- --------------------------------------------------------- -=\n")
            arquivo.write("=- Id atendimento | Id aluno | Disciplina | Horário | Status -=\n")
            arquivo.write("=- --------------------------------------------------------- -=\n")

    # Métodos
    # metodo que cadastra um atendimento
    def cadastrar_horario(self, atendimento):
        self.get_atendimentos()[atendimento.get_id_atendimento()] = atendimento

        with open(self.get_arquivo(), "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{atendimento.get_id_atendimento()} | {atendimento.get_id_aluno()} | {atendimento.get_disciplina()} | {atendimento.get_data_hora()} | {atendimento.get_status()}\n")

    # metodo que cadastra um atendimento
    def listar_disciplinas(self):
        print("=- --------------------------------------------------- -=")
        print("=-          Lista de disciplinas cadastradas           -=")
        print("=- --------------------------------------------------- -=")

        for disciplina in self.__disciplinas:
            print(f"=- {disciplina} -=")

        print("=- --------------------------------------------------- -=")
        
    # metodo que lista os atendimentos disponiveis
    def listar_horarios_livres(self, disciplina):
        print("=- --------------------------------------------------- -=")
        print("=-              Lista de horários livres               -=")
        print("=- --------------------------------------------------- -=")

        for horarios in self.get_atendimentos().values():
            if horarios.esta_disponivel() and horarios.get_disciplina() == disciplina:
                print(f"=- {horarios.get_data_hora()} | {horarios.get_status()} -=")

        print("=- --------------------------------------------------- -=")

    # metodo que reserva o atendimento com um aluno especifico
    def agendar_horario(self, id_atendimento, id_aluno):
        atendimento = self.get_atendimentos()[id_atendimento]

        atendimento.reservar(id_aluno)

        with open(self.get_arquivo(), "w", encoding="utf-8") as arquivo:
            arquivo.write("=- --------------------------------------------------------- -=\n")
            arquivo.write("=- Id atendimento | Id aluno | Disciplina | Horário | Status -=\n")
            arquivo.write("=- --------------------------------------------------------- -=\n")

            for atendimento in self.get_atendimentos().values():
                arquivo.write(f"{atendimento.get_id_atendimento()} | {atendimento.get_id_aluno()} | {atendimento.get_disciplina()} | {atendimento.get_data_hora()} | {atendimento.get_status()}\n")


    # metodo que mostra o agendamento do atendimento escolhido
    def ver_agendamento(self, id_atendimento):
        atendimento = self.get_atendimentos()[id_atendimento]
        print("=- --------------------------------------------------- -=")
        print("=-                    Agendamento                      -=")
        print("=- --------------------------------------------------- -=")

        print(f"=- Id - {atendimento.get_id_atendimento()} -=")
        print(f"=- Id do aluno - {atendimento.get_id_aluno()} -=")
        print(f"=- Disciplina - {atendimento.get_disciplina()} -=")
        print(f"=- Horário - {atendimento.get_data_hora()} -=")
        print(f"=- Status - {atendimento.get_status()} -=")

        print("=- --------------------------------------------------- -=")

    # getters
    def get_atendimentos(self):
        return self.__atendimentos

    def get_arquivo(self):
        return self.__arquivo