import unittest
from Atendimento import Atendimento
from SistemaAgendamento import SistemaAgendamento

class TesteSistemaAgendamento(unittest.TestCase):

    def setUp(self):

        self.sistema = SistemaAgendamento(arquivo="DadosAtendimentos_teste.txt")
        
        # Criando os atendimento
        self.at1 = Atendimento()
        self.at1.set_id_atendimento(101)
        self.at1.set_disciplina("Cálculo I")
        self.at1.set_data_hora("2026-10-22 12:00")

        self.at2 = Atendimento()
        self.at2.set_id_atendimento(102)
        self.at2.set_disciplina("Engenharia de software")
        self.at2.set_data_hora("2026-10-24 15:30")

        self.at3 = Atendimento()
        self.at3.set_id_atendimento(103)
        self.at3.set_disciplina("Cálculo I")
        self.at3.set_data_hora("2026-10-25 10:00")
        
        # Cadastrando os atendimentos no sistema
        self.sistema.cadastrar_horario(self.at1)
        self.sistema.cadastrar_horario(self.at2)
        self.sistema.cadastrar_horario(self.at3)

    # Teste para o critério de aceitação 1
    def test_visualizar_disciplinas_cadastradas(self):
        disciplinas = self.sistema.listar_disciplinas()
        self.assertIn("Cálculo I", disciplinas)
        self.assertIn("Engenharia de software", disciplinas)

    # Teste para o critério de aceitação 2
    def test_exibir_horarios_livres(self):
        livres = self.sistema.listar_horarios_livres("Cálculo I")
        self.assertEqual(len(livres), 2)
        self.assertTrue(all(h.get_status() == "LIVRE" for h in livres))

    # Teste para o critério de aceitação 3
    def test_selecionar_horario_livre(self):
        self.assertTrue(self.at1.esta_disponivel())

    # Teste para o critério de aceitação 4 versão de sucesso
    def test_realizar_agendamento_sucesso(self):
        agendado = self.sistema.agendar_horario(101, "2669510")
        self.assertEqual(agendado.get_status(), "RESERVADO")
        self.assertEqual(agendado.get_id_aluno(), "2669510")
        
        # Confirma que não está mais com status de LIVRE
        livres = self.sistema.listar_horarios_livres("Cálculo I")
        self.assertNotIn(agendado, livres)

    # Teste para o critério de aceitação 4 versão de falha
    def test_realizar_agendamento_falha(self):
        self.sistema.agendar_horario(101, "2669510")
        
        # Deve retornar o ValueError, pois já está cadastrado.
        with self.assertRaises(ValueError):
            self.sistema.agendar_horario(101, "5150854")

    # Critério de Aceitação 5
    def test_mostrar_agendamento(self):
        self.sistema.agendar_horario(101, "2669510")
        dados = self.sistema.ver_agendamento(101)
        
        self.assertEqual(dados["id_atendimento"], 101)
        self.assertEqual(dados["disciplina"], "Cálculo I")
        self.assertEqual(dados["status"], "RESERVADO")
        self.assertEqual(dados["id_aluno"], "2669510")


if __name__ == "__main__":

    runner = unittest.TextTestRunner()
    suite = unittest.TestLoader().loadTestsFromTestCase(TesteSistemaAgendamento)
    runner.run(suite)

    print("\n--- Gravando agendamento final no arquivo TXT ---")
    sistema_final = SistemaAgendamento(arquivo="DadosAtendimentos.txt")
    
    atendimento = Atendimento()
    atendimento.set_id_atendimento(101)
    atendimento.set_disciplina("Cálculo I")
    atendimento.set_data_hora("2022-10-1 17:30")
    
    sistema_final.cadastrar_horario(atendimento)
    sistema_final.agendar_horario(101, "2669510")
    
    print("Parabéns! Deu tudo certo!\n")