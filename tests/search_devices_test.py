from conftest import mock_subprocess_run

from simpleaudiocontroller import SearchDevices, DeviceType
from unittest.mock import patch


@patch("subprocess.run", mock_subprocess_run)
def test_search_microphones():
    devices = SearchDevices().get_microphones()
    assert len(devices) == 3
    devices = [device.dict() for device in devices]
    assert devices == [
        {
            "index": "1",
            "is_current_device": False,
            "name": "alsa_output.pci-0000_00_1f.3.analog-stereo",
            "type": "microphone",
        },
        {
            "index": "2",
            "is_current_device": True,
            "name": "alsa_output.platform-snd_aloop.0.analog-stereo",
            "type": "microphone",
        },
        {
            "index": "4",
            "is_current_device": False,
            "name": "alsa_output.pci-0000_01_00.1.hdmi-stereo-extra2",
            "type": "microphone",
        },
    ]


@patch("subprocess.run", mock_subprocess_run)
def test_search_headphones():
    devices = SearchDevices().get_headphones()
    assert len(devices) == 3
    devices = [device.dict() for device in devices]
    assert devices == [
        {
            "index": "1",
            "is_current_device": False,
            "name": "alsa_output.pci-0000_00_1f.3.analog-stereo",
            "type": "headphone",
        },
        {
            "index": "2",
            "is_current_device": True,
            "name": "alsa_output.platform-snd_aloop.0.analog-stereo",
            "type": "headphone",
        },
        {
            "index": "4",
            "is_current_device": False,
            "name": "alsa_output.pci-0000_01_00.1.hdmi-stereo-extra2",
            "type": "headphone",
        },
    ]


@patch("subprocess.run", mock_subprocess_run)
def test_get_current_microphone():
    device = SearchDevices().get_current_microphone()
    assert device.dict() == {
        "index": "2",
        "is_current_device": True,
        "name": "alsa_output.platform-snd_aloop.0.analog-stereo",
        "type": "microphone",
    }


@patch("subprocess.run", mock_subprocess_run)
def test_get_current_headphone():
    device = SearchDevices().get_current_headphone()
    assert device.dict() == {
        "index": "2",
        "is_current_device": True,
        "name": "alsa_output.platform-snd_aloop.0.analog-stereo",
        "type": "headphone",
    }


@patch("subprocess.run", mock_subprocess_run)
def test_get_microphone_by_name():
    device = SearchDevices().get_device_by_name(
        "alsa_output.pci-0000_01_00.1.hdmi-stereo-extra2", DeviceType.MICROPHONE)
    assert device.dict() == {
        "index": "4",
        "is_current_device": False,
        "name": "alsa_output.pci-0000_01_00.1.hdmi-stereo-extra2",
        "type": "microphone",
    }


@patch("subprocess.run", mock_subprocess_run)
def test_get_headphone_by_name():
    device = SearchDevices().get_device_by_name(
        "alsa_output.pci-0000_01_00.1.hdmi-stereo-extra2", DeviceType.HEADPHONE)
    assert device.dict() == {
        "index": "4",
        "is_current_device": False,
        "name": "alsa_output.pci-0000_01_00.1.hdmi-stereo-extra2",
        "type": "headphone",
    }
