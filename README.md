# Bongo

A cute bongo cat for your display. Reacts to key input.

## Quick Start

1. Install dependencies with [Circup](https://github.com/adafruit/circup): `circup install -r requirements.txt`

   > Make sure you have downloaded [requirements.txt](https://raw.githubusercontent.com/christanaka/circuitpython-bongo/main/requirements.txt) and your device is connected.

   Alternatively you can download and copy [dependencies](#dependencies) to the `/lib` directory manually.

2. [Download the latest release](https://github.com/christanaka/circuitpython-bongo) and copy its contents to your device

## Usage

```python
from adafruit_macropad import MacroPad
from bongo.bongo import Bongo

# Create and show bongo
macropad = MacroPad()
bongo = Bongo()
macropad.display.show(bongo.group)

# Main loop
while True:
    key_event = macropad.keys.events.get()
    bongo.update(key_event)
```

## API

### Position

You can position bongo by setting `bongo.x` and `bongo.y`:

```python
bongo.x = 30
bongo.y = 20
```

### Animation Time

You can adjust the bounce and tap animation time when creating a bongo instance:

```python
bongo = Bongo(bounce_time=0.05, tap_time=0.05)
```

## Dependencies

- [Adafruit's CircuitPython NeoPixel library](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel)
- [Adafruit's CircuitPython HID library](https://github.com/adafruit/Adafruit_CircuitPython_HID)
- [Adafruit's CircuitPython MIDI library](https://github.com/adafruit/Adafruit_CircuitPython_MIDI>)
- [Adafruit's CircuitPython Display Text library](https://github.com/adafruit/Adafruit_CircuitPython_Display_Text)
- [Adafruit's CircuitPython Simple Text Display library](https://github.com/adafruit/Adafruit_CircuitPython_Simple_Text_Display)
- [Adafruit's CircuitPython Debouncer library](https://github.com/adafruit/Adafruit_CircuitPython_Debouncer)
- [Adafruit's CircuitPython Image Load library](https://github.com/adafruit/Adafruit_CircuitPython_ImageLoad)
- [Adafruit's CircuitPython MacroPad library](https://github.com/adafruit/Adafruit_CircuitPython_MacroPad)
