import unittest
from unittest.mock import patch, MagicMock, call
import scripts.led_pulse as led_pulse


class TestLedPulse(unittest.TestCase):

    @patch('scripts.led_pulse.Arduino')
    def test_led_single_pulse(self, mock_Arduino):
        mock_Arduino.return_value = MagicMock()
        led_pulse.led('COM1', 1, 0.5)
        mock_Arduino.return_value.digital[0].write.assert_any_call(1)
        mock_Arduino.return_value.digital[0].write.assert_any_call(0)

    @patch('scripts.led_pulse.Arduino')
    def test_led_periodic_pulse(self, mock_Arduino):
        mock_Arduino.return_value = MagicMock()
        led_pulse.led('COM1', 2, 0.5, 0.5, 3)
        calls = [call(1), call(0)]
        mock_Arduino.return_value.digital[0].write.assert_has_calls(calls * 3)


if __name__ == '__main__':
    unittest.main()
