# Audio Controller Documentation

## Overview
The `AudioController` class provides a set of functionalities for controlling audio devices on a Linux system using the `pacmd` command-line utility. It allows you to manage audio input (microphones) and output (headphones/speakers) devices, set defaults, and retrieve information about the available devices.

## Classes

### `PacmdExecutor`
This class is responsible for executing `pacmd` commands using the `subprocess` module. It provides a way to run `pacmd` commands and capture the standard output and standard error.

#### Methods
- `execute(exec_args: List[str]) -> subprocess.CompletedProcess`: Executes a `pacmd` command with the specified arguments and returns the result as a `subprocess.CompletedProcess` object.

### `Device`
Represents an audio device with attributes like `index`, `name`, and whether it is the current device (`is_current_device`).

#### Constructor
- `Device(index: str, name: str, is_current_device: bool = False)`: Initializes a `Device` object with the provided `index`, `name`, and an optional flag indicating whether it is the current device.

### `SearchDevices`
This class is responsible for parsing the text output from `pacmd` and extracting information about audio devices.

#### Constructor
- `SearchDevices(text_stdout: str)`: Initializes a `SearchDevices` object with the raw text output from `pacmd`.

#### Methods
- `search() -> List[Device]`: Parses the raw text output and returns a list of `Device` objects representing the available audio devices.

- `parse_text_stdout(text_stdout: str) -> List[str]`: Static method that splits the raw text output into individual device text blocks for further parsing.

### `AudioController`
The main class that provides audio control functionalities. It uses the `PacmdExecutor` and `SearchDevices` classes to interact with `pacmd`.

#### Constructor
- `AudioController()`: Initializes an `AudioController` object.

#### Methods
- `set_default_headphone(device: Device) -> bool`: Sets the default audio output device to the provided `Device`. Returns `True` if the operation is successful, `False` otherwise.

- `set_default_microphone(device: Device) -> bool`: Sets the default audio input (microphone) device to the provided `Device`. Returns `True` if the operation is successful, `False` otherwise.

- `get_current_headphone() -> Union[Device, None]`: Retrieves the currently set default audio output device (headphone). Returns a `Device` object if found, `None` otherwise.

- `get_current_microphone() -> Union[Device, None]`: Retrieves the currently set default audio input (microphone) device. Returns a `Device` object if found, `None` otherwise.

- `get_microphone_by_name(name: str) -> Union[Device, None]`: Retrieves an audio input (microphone) device by its name. Returns a `Device` object if found, `None` otherwise.

- `get_phone_by_name(name: str) -> Union[Device, None]`: Retrieves an audio output (headphone/speaker) device by its name. Returns a `Device` object if found, `None` otherwise.

- `get_phones() -> List[Device]`: Retrieves a list of available audio output (headphone/speaker) devices. Returns a list of `Device` objects.

- `get_microphones() -> List[Device]`: Retrieves a list of available audio input (microphone) devices. Returns a list of `Device` objects.

## Example Usage
```python
from simpleaudiocontroller import AudioController

# Create an AudioController object
audio_controller = AudioController()

# Get the list of available headphones
headphones = audio_controller.get_phones()

# Set the default headphone to the first one in the list
if headphones:
    default_headphone = headphones[0]
    audio_controller.set_default_headphone(default_headphone)

# Get the current default microphone
current_microphone = audio_controller.get_current_microphone()
if current_microphone:
    print(f"Current microphone: {current_microphone.name}")

# Search for a microphone by name
desired_microphone = audio_controller.get_microphone_by_name("My Microphone")

# Set the default microphone
if desired_microphone:
    audio_controller.set_default_microphone(desired_microphone)
```
