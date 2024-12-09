import unittest

class TestSomaLista(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(soma_lista([1, 2, 3, 4]), 10)

    def test_soma_negativos(self):
        self.assertEqual(soma_lista([-1, -2, -3, -4]), -10)

    def test_soma_mistos(self):
        self.assertEqual(soma_lista([1, -1, 2, -2]), 0)

    def test_lista_vazia(self):
        self.assertEqual(soma_lista([]), 0)

    def test_valores_invalidos(self):
        with self.assertRaises(ValueError):
            soma_lista([1, 'dois', 3])
