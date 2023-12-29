import unittest
from unittest.mock import patch, MagicMock
from scripts.main import Arduino, open_new_page, pulso_unico, pulso_periodico
import scripts.utilities


class TestMain(unittest.TestCase):

    @patch('serial.Serial')
    def test_Arduino(self, mock_serial):
        mock_serial.return_value = MagicMock()

        self.assertIsNotNone(Arduino('COM1'))
        self.assertIsNone(Arduino('Selecione a porta'))

    @patch('scripts.main.open_new_page')
    def test_pulso_unico(self, mock_open_new_page):
        mock_open_new_page.return_value = None

        self.assertIsNone(pulso_unico())

    @patch('scripts.main.open_new_page')
    def test_pulso_periodico(self, mock_open_new_page):
        mock_open_new_page.return_value = None

        self.assertIsNone(pulso_periodico())


if __name__ == '__main__':
    unittest.main()
