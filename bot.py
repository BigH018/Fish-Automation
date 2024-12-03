import easyocr
from queue import Queue
import time
import threading
import keyboard
import numpy as np
from PIL import Image, ImageGrab, ImageEnhance, ImageOps

# Initialize EasyOCR
reader = easyocr.Reader(['en'], gpu=False)

WAIT_TIME = 0.80
TOGGLE = False
TEXT_AREA = (0, 0, 100, 100)
ocr_queue = Queue()
results_callback = None

def update_results_callback(callback):
    global results_callback
    results_callback = callback

def update_wait_time(wait_time):
    global WAIT_TIME
    WAIT_TIME = wait_time

def preprocess_image(img):
    """Preprocess the image for OCR."""
    img = ImageOps.grayscale(img)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)  # Increase contrast for better detection
    img = img.resize((img.width * 2, img.height * 2), Image.LANCZOS)  # Resize for better accuracy
    return img

def perform_actions():
    """Perform the predefined actions (pressing "s", "enter", "5")."""
    keyboard.send("s")
    time.sleep(WAIT_TIME)
    keyboard.send("enter")
    time.sleep(WAIT_TIME)
    keyboard.send("5")
    time.sleep(WAIT_TIME)

def check_for_word(roll_count, target_word):
    """Check for the target word in the defined screen capture area."""
    img = ImageGrab.grab(bbox=TEXT_AREA)
    img = preprocess_image(img)
    img_np = np.array(img)
    results = reader.readtext(img_np, detail=0)
    results = [result.strip().lower() for result in results]
    normalized_target = target_word.strip().lower()

    for result in results:
        if normalized_target in result:
            if results_callback:
                results_callback(f"Target '{target_word}' found after {roll_count} rolls. Bot stopped.")
            stop_bot()
            return True
    return False

def action_loop(target_word):
    """Main loop for the bot actions."""
    global TOGGLE
    roll_count = 0
    while TOGGLE:
        roll_count += 1
        if check_for_word(roll_count, target_word):
            break
        perform_actions()

def stop_bot():
    """Stop the bot and clean up."""
    global TOGGLE
    TOGGLE = False
    while not ocr_queue.empty():
        ocr_queue.get()
        ocr_queue.task_done()