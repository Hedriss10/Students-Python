import unittest
from pessoa import Pessoa 
from unittest.mock import patch

class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Hedris', 'Rocha')



    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Hedris')


    def test_pessoa_attr_str(self):
        self.assertIsInstance(self.p1.nome, str)

   
    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Rocha')


    def test_pessoa_attr_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)


    
    def test_pessoa_attr_dados_obetidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obetidos, False)



    def test_obter_todos_os_dados_sucesso(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.obeter_todos_os_dados(), 'CONECTADO')



    def test_obter_todos_dados_falha_404(self):
        with patch('request.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.obeter_todos_os_dados(), "ERRO 404")
            self.assertFalse(self.p1.dados_obetidos)



        





if __name__ == '__main__':

    unittest.main(verbosity=2)
