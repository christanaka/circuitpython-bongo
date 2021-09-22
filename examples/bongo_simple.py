import displayio
from adafruit_macropad import MacroPad
from bongo.bongo import Bongo

# Create macropad and bongo
macropad = MacroPad()
bongo = Bongo()

# Create a group and add bongo to it
group = displayio.Group()
group.append(bongo.group)

# Show the group
macropad.display.show(group)

# Main loop
while True:
    key_event = macropad.keys.events.get()
    bongo.update(key_event)
