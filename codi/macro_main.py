import time
import board
import digitalio
import json
import usb_hid
import analogio
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Initialize USB HID
keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

# Load Macro Config
config = {"keys": [{"type": "none"}] * 16, "pots": ["none", "none", "none"]}
try:
    with open('macro_config.json', 'r') as f:
        config = json.load(f)
except Exception as e:
    print("No s'ha trobat macro_config.json, o error de format", e)

# Define hardware pins (GP0 to GP15 for keys, A0 to A2 for pots)
BUTTON_PINS = [
    board.GP0, board.GP1, board.GP2, board.GP3,
    board.GP4, board.GP5, board.GP6, board.GP7,
    board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14, board.GP15
]

POT_PINS = [board.A0, board.A1, board.A2]

# Setup inputs
buttons = []
for pin in BUTTON_PINS:
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.DOWN
    buttons.append(btn)

pots = []
for pin in POT_PINS:
    pots.append(analogio.AnalogIn(pin))

# State tracking
last_btn_state = [False] * 16
last_pot_state = [0, 0, 0]

DEBOUNCE_TIME = 0.02
POT_TOLERANCE = 1500 # Threshold to detect movement

def get_modifier(mod_name):
    if mod_name == 'shift': return Keycode.SHIFT
    if mod_name == 'ctrl': return Keycode.CONTROL
    if mod_name == 'alt': return Keycode.ALT
    if mod_name == 'cmd': return Keycode.COMMAND
    return None

def exec_action(cfg, press):
    if cfg['type'] == 'key':
        if not 'val' in cfg: return
        key_str = cfg['val']
        keycode = getattr(Keycode, key_str, None)
        if not keycode: return
        
        if press:
            mods = []
            if cfg.get('ctrl'): mods.append(Keycode.CONTROL)
            if cfg.get('shift'): mods.append(Keycode.SHIFT)
            if cfg.get('alt'): mods.append(Keycode.ALT)
            if cfg.get('cmd'): mods.append(Keycode.COMMAND)
            for m in mods: keyboard.press(m)
            keyboard.press(keycode)
        else:
            keyboard.release_all()
            
    elif cfg['type'] == 'media':
        if not press: return # Media keys usually trigger on press only
        if not 'val' in cfg: return
        code = getattr(ConsumerControlCode, cfg['val'], None)
        if code:
            cc.send(code)

while True:
    # 1. Process Buttons
    for i in range(16):
        curr_state = buttons[i].value
        if curr_state != last_btn_state[i]:
            time.sleep(DEBOUNCE_TIME) # Simple debounce
            curr_state = buttons[i].value # Check again
            if curr_state != last_btn_state[i]:
                last_btn_state[i] = curr_state
                exec_action(config['keys'][i], curr_state)

    # 2. Process Potentiometers (only if configured)
    for i in range(3):
        cfg_pot = config['pots'][i]
        if cfg_pot != 'none':
            curr_val = pots[i].value
            diff = curr_val - last_pot_state[i]
            if abs(diff) > POT_TOLERANCE:
                # Pot moved significantly. Determine direction.
                if diff > 0:
                    if cfg_pot == 'vol': cc.send(ConsumerControlCode.VOLUME_UP)
                    elif cfg_pot == 'bright': cc.send(ConsumerControlCode.BRIGHTNESS_INCREMENT)
                else:
                    if cfg_pot == 'vol': cc.send(ConsumerControlCode.VOLUME_DOWN)
                    elif cfg_pot == 'bright': cc.send(ConsumerControlCode.BRIGHTNESS_DECREMENT)
                
                last_pot_state[i] = curr_val

    time.sleep(0.01)
