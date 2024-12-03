import time
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController, Button

# Initialize controllers
keyboard = KeyboardController()
mouse = MouseController()

# Default wait time between actions (in seconds)
default_wait_time = 0.8

# Wait time before a mouse click (in seconds)
click_wait_time = 0.2

def send_char_by_char(text, delay=0.01):
    """Types a string character by character with a small delay."""
    for char in text:
        keyboard.type(char)
        time.sleep(delay)

def equip_items(wait_time=default_wait_time, click_time=click_wait_time):
    """Performs the sequence of actions described in the AHK script."""
    # Action 2: Press the "s" key
    keyboard.press('s')
    keyboard.release('s')
    time.sleep(wait_time)

    # Action 3: Press the "w" key
    keyboard.press('w')
    keyboard.release('w')
    time.sleep(wait_time)

    # Action 4: Press "Enter"
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(wait_time)

    # Action 2: Press the "s" key
    keyboard.press('s')
    keyboard.release('s')
    time.sleep(wait_time)

    # Action 4: Press "Enter"
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(wait_time)

    # Action 5: Press "Backspace"
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    time.sleep(wait_time)

    # Action 6: Type "advanced diving gear"
    send_char_by_char("advanced diving gear")
    time.sleep(wait_time)

    # Action 7: Press "Enter"
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(wait_time)

    # Action 8: Press "s"
    keyboard.press('s')
    keyboard.release('s')
    time.sleep(wait_time)

    # Action 9: Press "s" again
    keyboard.press('s')
    keyboard.release('s')
    time.sleep(wait_time)

    # Action 10: Press "Enter"
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(wait_time)

    # Action 11: Perform a mouse click (with click_wait_time)
    time.sleep(click_time)  # Wait before the click
    mouse.click(Button.left)
    time.sleep(wait_time)  # Wait after the click

    # Action 12: Press "w"
    keyboard.press('w')
    keyboard.release('w')
    time.sleep(wait_time)

    # Action 13: Press "Enter"
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(wait_time)

    # Action 14: Press "Backspace"
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    time.sleep(wait_time)

    # Action 15: Type "super flippers"
    send_char_by_char("super flippers")
    time.sleep(wait_time)

    # Action 16: Press "Enter"
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(wait_time)

    # Action 17: Press "s"
    keyboard.press('s')
    keyboard.release('s')
    time.sleep(wait_time)

    # Action 18: Press "s" again
    keyboard.press('s')
    keyboard.release('s')
    time.sleep(wait_time)

    # Action 19: Press "Enter"
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(wait_time)

    # Action 20: Perform another mouse click (with click_wait_time)
    time.sleep(click_time)  # Wait before the click
    mouse.click(Button.left)
    time.sleep(wait_time)  # Wait after the click

    # Action 21: Press "w"
    keyboard.press('w')
    keyboard.release('w')
    time.sleep(wait_time)

    # Action 22: Press "Enter"
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(wait_time)

    # Action 23: Press "Backspace"
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    time.sleep(wait_time)

    # Action 24: Type "fish radar"
    send_char_by_char("fish radar")
    time.sleep(wait_time)

    # Action 25: Press "Enter"
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(wait_time)

    # Action 26: Press "s"
    keyboard.press('s')
    keyboard.release('s')
    time.sleep(wait_time)

    # Action 27: Press "s" again
    keyboard.press('s')
    keyboard.release('s')
    time.sleep(wait_time)

    # Action 28: Press "Enter"
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(wait_time)

    # Action 29: Perform another mouse click (with click_wait_time)
    time.sleep(click_time)  # Wait before the click
    mouse.click(Button.left)
    time.sleep(wait_time)  # Wait after the click
