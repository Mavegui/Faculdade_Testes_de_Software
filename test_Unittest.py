import unittest
from unittest.mock import patch
from maior_ou_menor import main

class TesteComUnittest(unittest.TestCase):
    """
    Nessa forma de testar  usando unittest é usado:
        - mock_input para simular entradas do usuários.
        - side_effect para receber múltiplos valores.
        - Os testes são baseados na atividade proposta no enunciado. 
    """
    @patch("builtins.input")
    def test_A_primeiro_caso(self, mock_input):
        mock_input.side_effect = ['10', '20']
        
        resultado = main()
        self.assertEqual(resultado, (10, 20))
        
    @patch("builtins.input")
    def test_B_segundo_caso(self, mock_input):
        mock_input.side_effect = ['30', '20']
        
        resultado = main()
        self.assertEqual(resultado, (30, 20))
    
    @patch("builtins.input")
    def test_C_terceiro_caso(self, mock_input):
        mock_input.side_effect = ['100', '100']
        
        resultado = main()
        self.assertEqual(resultado, (100, 100))
    
    @patch("builtins.input")
    def test_D_try(self, mock_input):
        mock_input.side_effect = ['abc', '200', '300']
        
        resultado = main()
        self.assertEqual(resultado, (200, 300))
        
if __name__ == "__main__":
    unittest.main()