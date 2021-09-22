import displayio
from adafruit_macropad import MacroPad
from bongo.bongo import Bongo

macropad = MacroPad()
bongo = Bongo()

group = displayio.Group()
group.append(bongo.group)
macropad.display.show(group)

while True:
    key_event = macropad.keys.events.get()
    bongo.update(key_event)
