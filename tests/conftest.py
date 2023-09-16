from subprocess import CompletedProcess


def mock_stdout():
    return """3 sink(s) available.
        index: 1
        name: <alsa_output.pci-0000_00_1f.3.analog-stereo>
        driver: <module-alsa-card.c>
        active port: <analog-output-headphones>
      * index: 2
        name: <alsa_output.platform-snd_aloop.0.analog-stereo>
        driver: <module-alsa-card.c>
        active port: <analog-output>
        index: 4
        name: <alsa_output.pci-0000_01_00.1.hdmi-stereo-extra2>
        driver: <module-alsa-card.c>
        active port: <hdmi-output-2>
    """.encode()


def mock_subprocess_run(*__, **___):
    return CompletedProcess(
        None,
        0,
        stdout=mock_stdout(),
    )
