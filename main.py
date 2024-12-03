import screenData
import gui
import bot
import threading
import time
import keyboard
from tutorial import show_tutorial
from equipt import equip_items  # Assuming equipt.py contains the logic for the Equip Bot

bot_running = False  # Global state for the Appraisal Bot
equip_bot_running = False  # Global state for the Equip Bot

def set_screen_area():
    """Handle screen area selection using screenData."""
    def update_area(area):
        bot.TEXT_AREA = area
        gui.update_area_label(f"Selected Area: {area}")
        gui.update_status_label("appraisal", f"Area successfully set to {area}!")

    screenData.select_screen_area(update_area)

def start_action_loop():
    """Starts the Appraisal Bot's action loop."""
    global bot_running
    if not bot_running:
        bot_running = True
        bot.TOGGLE = True
        target_word = gui.get_gui_value("appraisal_target_word_input", default="")
        gui.update_status_label("appraisal", f"Appraisal Bot is running... Looking for '{target_word}'")
        threading.Thread(target=bot.action_loop, args=(target_word,), daemon=True).start()

def stop_action_loop():
    """Stops the Appraisal Bot's action loop."""
    global bot_running
    if bot_running:
        bot_running = False
        bot.stop_bot()
        gui.update_status_label("appraisal", "Appraisal Bot stopped.")

def start_equip_bot():
    """Starts the Equip Bot."""
    global equip_bot_running
    if not equip_bot_running:
        equip_bot_running = True
        gui.update_status_label("equip", "Equip Bot is running...")
        threading.Thread(
            target=run_equip_bot, 
            args=(
                gui.get_gui_value("equip_default_wait_time_input", 0.8),  # Pass the user-defined default wait time
                gui.get_gui_value("equip_click_wait_time_input", 0.2)   # Pass the user-defined click wait time
            ),
            daemon=True
        ).start()


def stop_equip_bot():
    """Stops the Equip Bot."""
    global equip_bot_running
    if equip_bot_running:
        equip_bot_running = False
        gui.update_status_label("equip", "Equip Bot stopped.")

def run_equip_bot(default_wait_time, click_wait_time):
    """Runs the Equip Bot loop."""
    import equipt  # Import the updated equip_items logic
    try:
        # Pass the dynamically fetched times to equip_items
        equipt.equip_items(
            wait_time=default_wait_time, 
            click_time=click_wait_time
        )
        gui.update_status_label("equip", "Equip Bot actions completed.")
    except Exception as e:
        gui.update_status_label("equip", f"Error: {e}")
    finally:
        global equip_bot_running
        equip_bot_running = False


def monitor_hotkeys(callbacks):
    """Monitors hotkeys for starting and stopping both bots."""
    global bot_running, equip_bot_running

    while True:
        try:
            # Appraisal Bot hotkeys
            appraisal_start_hotkey = gui.get_gui_value("appraisal_start_hotkey", default="F1")
            appraisal_stop_hotkey = gui.get_gui_value("appraisal_stop_hotkey", default="F2")

            if keyboard.is_pressed(appraisal_start_hotkey) and not bot_running:
                callbacks["start_bot"]()

            if keyboard.is_pressed(appraisal_stop_hotkey) and bot_running:
                callbacks["stop_bot"]()

            # Equip Bot hotkeys
            equip_hotkey = gui.get_gui_value("equip_hotkey", default="F3")

            if keyboard.is_pressed(equip_hotkey) and not equip_bot_running:
                callbacks["start_equip_bot"]()

        except Exception as e:
            gui.update_status_label("appraisal", f"Error: {e}")
            gui.update_status_label("equip", f"Error: {e}")

        time.sleep(0.1)

def update_equip_bot_times(settings):
    """Updates the default and click wait times for the Equip Bot."""
    import equipt  # Ensure we are updating the correct module
    equipt.default_wait_time = settings["default_wait_time"]  # No KeyError here
    equipt.click_wait_time = settings["click_wait_time"]  # No KeyError here
    gui.update_status_label("equip", "Equip Bot timings updated!")

if __name__ == "__main__":
    callbacks = {
        # Appraisal Bot callbacks
        "start_bot": start_action_loop,
        "stop_bot": stop_action_loop,
        "set_screen_area": set_screen_area,
        "save_settings_appraisal": lambda settings: bot.update_wait_time(settings["wait_time"]),
        
        # Equip Bot callbacks
        "start_equip_bot": start_equip_bot,
        "save_settings_equip": lambda settings: update_equip_bot_times(settings),

        # Tutorial callback
        "show_tutorial": show_tutorial
    }

    # Pass a callback for updating results to the bot module
    bot.update_results_callback(lambda result: gui.update_status_label("appraisal", result))

    # Start hotkey monitoring in a separate thread
    threading.Thread(target=monitor_hotkeys, args=(callbacks,), daemon=True).start()

    # Run the GUI
    gui.run_app(callbacks)