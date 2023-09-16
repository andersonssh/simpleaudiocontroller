from conftest import mock_subprocess_run
from simpleaudiocontroller import AudioController
from unittest.mock import patch, call


@patch("subprocess.run", return_value=mock_subprocess_run())
def test_set_default_microphone(mock_subprocess):
    audio_controller = AudioController()
    microphones = audio_controller.get_microphones()
    device = microphones[0]
    audio_controller.set_default_device(device)
    assert mock_subprocess.call_args == call(
        ['pacmd', 'set-default-source', device.index], stdout=-1, stderr=-1)


@patch("subprocess.run", return_value=mock_subprocess_run())
def test_set_default_headphone(mock_subprocess):
    audio_controller = AudioController()
    headphones = audio_controller.get_headphones()
    device = headphones[0]
    audio_controller.set_default_device(device)
    assert mock_subprocess.call_args == call(
        ['pacmd', 'set-default-sink', device.index], stdout=-1, stderr=-1)
