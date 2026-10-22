from Atendimento import *

# classe de sistema de agendamento 
class SistemaAgendamento:
    def __init__(self, arquivo="DadosAtendimentos.txt"):
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
        self.__arquivo = arquivo

    # Métodos
    # metodo que cadastra um atendimento
    def cadastrar_horario(self, atendimento):
        self.get_atendimentos()[atendimento.get_id_atendimento()] = atendimento

        # Reescreve o arquivo atualizado com o cabeçalho
        with open(self.get_arquivo(), "w", encoding="utf-8") as arquivo:
            arquivo.write("=- --------------------------------------------------------- -=\n")
            arquivo.write("=- Id atendimento | Id aluno | Disciplina | Horário | Status -=\n")
            arquivo.write("=- --------------------------------------------------------- -=\n")
            for at in self.get_atendimentos().values():
                arquivo.write(f"{at.get_id_atendimento()} | {at.get_id_aluno()} | {at.get_disciplina()} | {at.get_data_hora()} | {at.get_status()}\n")

    # metodo que lista as disciplinas
    def listar_disciplinas(self):
        print("=- --------------------------------------------------- -=")
        print("=-          Lista de disciplinas cadastradas           -=")
        print("=- --------------------------------------------------- -=")

        for disciplina in self.__disciplinas:
            print(f"=- {disciplina} -=")

        print("=- --------------------------------------------------- -=")
        
        # RETORNO CRUCIAL: permite que o unittest verifique a lista
        return self.__disciplinas

    # metodo que lista os atendimentos disponiveis
    def listar_horarios_livres(self, disciplina):
        print("=- --------------------------------------------------- -=")
        print("=-              Lista de horários livres               -=")
        print("=- --------------------------------------------------- -=")

        livres = []
        for horarios in self.get_atendimentos().values():
            if horarios.esta_disponivel() and horarios.get_disciplina() == disciplina:
                print(f"=- {horarios.get_data_hora()} | {horarios.get_status()} -=")
                livres.append(horarios)

        print("=- --------------------------------------------------- -=")
        
        return livres

    # metodo que reserva o atendimento com um aluno especifico
    def agendar_horario(self, id_atendimento, id_aluno):
        if id_atendimento not in self.get_atendimentos():
            raise KeyError("Atendimento não encontrado")

        atendimento = self.get_atendimentos()[id_atendimento]
        atendimento.reservar(id_aluno)

        with open(self.get_arquivo(), "w", encoding="utf-8") as arquivo:
            arquivo.write("=- --------------------------------------------------------- -=\n")
            arquivo.write("=- Id atendimento | Id aluno | Disciplina | Horário | Status -=\n")
            arquivo.write("=- --------------------------------------------------------- -=\n")

            for at in self.get_atendimentos().values():
                arquivo.write(f"{at.get_id_atendimento()} | {at.get_id_aluno()} | {at.get_disciplina()} | {at.get_data_hora()} | {at.get_status()}\n")

        return atendimento

    # metodo que mostra o agendamento do atendimento escolhido
    def ver_agendamento(self, id_atendimento):
        if id_atendimento not in self.get_atendimentos():
            raise KeyError("Atendimento não encontrado")

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

        # É preciso retornar os dados do atendimento para realizar a verificação nos testes.
        return {
            "id_atendimento": atendimento.get_id_atendimento(),
            "id_aluno": atendimento.get_id_aluno(),
            "disciplina": atendimento.get_disciplina(),
            "data_hora": atendimento.get_data_hora(),
            "status": atendimento.get_status()
        }

    # getters
    def get_atendimentos(self):
        return self.__atendimentos

    def get_arquivo(self):
        return self.__arquivo