import unittest
import main3

class TestAppend(unittest.TestCase):

	def test_calculator(self):
		self.assertEqual(main3.calculator(2,2), 4)



if __name__ == "__main__":
	unittest.main()