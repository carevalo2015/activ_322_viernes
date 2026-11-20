import unittest
from hola import saludar

class TestHola(unittest.TestCase):

	def test_saludo(self):
		self.assertEqual(
			saludar(),
			"Hola Mundo DSO"
		)

if __name__ == "__main__":
	unittest.main()
