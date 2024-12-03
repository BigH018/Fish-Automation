# Revised code, retaining all original Appraisal Bot pages while including the Equip Bot section.

import dearpygui.dearpygui as dpg

# Appraisal Bot Tutorial Pages
APPRAISAL_PAGES = [
    "Welcome to the Appraisal Bot Tutorial!\n\n"
    "This tool is designed for automating the fish appraisal system in the game.\n\n"
    "Make sure you read through this tutorial carefully to fully understand the Fish Appraisal Bot.\n\n"
    "Click 'Next Page' to begin.",
    "Step 1: Capture Area Settings\n\n"
    "The 'Capture Area' is the part of your screen where the bot will look for text. For this tool, it's important to capture the slot 5 in your hotbar where the fish will be placed.\n\n"
    "To set it:\n\n"
    "1. Click the 'Set Capture Area' button in the main window.\n"
    "2. Drag your mouse to draw a rectangle over the slot 5 area.\n"
    "3. Release the mouse button to confirm the selection.\n\n"
    "The bot will only read text from this region, so make sure it's set correctly.",
    "Step 2: Target Word Settings\n\n"
    "The 'Target Word' is the word or phrase you want the bot to search for in the capture area.\n\n"
    "How to use it:\n\n"
    "1. Enter the target word (e.g., 'Big', 'Giant', or any other fish size) in the input box.\n\n"
    "2. The bot will keep running until it finds this word.\n\n"
    "Make sure the word matches exactly as it appears in the game (case doesn't matter).",
    "Step 3: Hotkey Settings\n\n"
    "Hotkeys let you control the bot quickly and easily.\n\n"
    "There are two hotkeys to set:\n\n"
    "- 'Start Hotkey': Use this key to start the bot.\n"
    "- 'Stop Hotkey': Use this key to stop the bot instantly.\n\n"
    "How to set them:\n\n"
    "1. Choose a key from the dropdown menus in the main window.\n"
    "2. Ensure the keys are convenient and not used for other actions during gameplay.",
    "Step 4: Timing Settings\n\n"
    "The 'Wait Time' setting controls how long the bot waits between actions.\n\n"
    "How it works:\n\n"
    "- A shorter wait time makes the bot faster, but it may cause errors if the seller speaks slowly.\n\n"
    "- A longer wait time makes the bot slower but more stable.\n\n"
    "The default is 0.05 seconds, but the **recommended range is 0.5 to 1 second**. Personally, I use **0.8 seconds**, as the bot is limited by how fast the seller speaks.",
    "Step 5: Pre-Setup Instructions\n\n"
    "Now that you've chosen your settings, here's what you need to do before starting the bot:\n\n"
    "1. Open Roblox settings and turn on **UI Navigation**.\n"
    "2. Select the fish you want to roll and place it in **slot 5 of your hotbar** (where you captured the screen earlier).\n\n"
    "3. Close your inventory and make sure you are holding the fish.\n"
    "4. Talk to the appraisal guy one time to get to the prompt for the appraisal.\n\n"
    "5. Press your **UI Navigation key** to open the seller UI. (For me, it's '#', but for you, it might be '\\').\n\n"
    "After this, all you need to do is press your start hotkey and sit back and relax.",
    "You're ready to go!\n\n"
    "Congratulations! You now know how to use the Appraisal Bot.\n\n"
    "Happy automating!"
]

# Equip Bot Tutorial Pages
EQUIP_PAGES = [
    "Welcome to the Equip Bot Tutorial!\n\n"
    "This bot is designed to automate equipping the Advanced Diving Gear, Super Flippers, and Fish Radar.\n\n"
    "Follow these steps to set up the Equip Bot. Click 'Next Page' to begin.",
    "Step 1: Hotkey Settings\n\n"
    "Set a hotkey for equipping items quickly.\n\n"
    "1. Choose a key from the dropdown in the main window.\n"
    "2. Ensure the key is convenient and not used for other game actions.\n\n"
    "This hotkey will be used to initiate the equipping process.",
    "Step 2: Timing Settings\n\n"
    "Configure the bot's wait times to match the game's speed.\n\n"
    "- Default Wait Time controls how long the bot waits between actions.\n\n"
    "- Click Wait Time controls how long the bot holds each click.\n\n"
    "**Recommended Timings:**\n\n"
    "- Default Wait Time: 0.05 seconds\n"
    "- Click Wait Time: 0.2 seconds\n\n"
    "Adjust these settings to balance speed and reliability.",
    "Step 3: Pre-requisites\n\n"
    "Before starting the bot, make sure the following is done:\n\n"
    "1. Open Roblox settings and turn on **UI Navigation**.\n"
    "2. Make sure your inventory is closed.\n"
    "3. Hover your mouse over 'dead space' on the screen, somewhere you can click and it won't affect anything.\n\n"
    "4. Press your **UI Navigation key** to open the UI (e.g., '#' or '\\').\n\n"
    "Once these steps are complete, you're ready to use the Equip Bot.",
    "You're ready to go!\n\n"
    "Congratulations! You now know how to use the Equip Bot.\n\n"
    "Happy automating!"
]

# Current page indices
current_pages = {"appraisal": 0, "equip": 0}


def show_tutorial():
    """Creates and displays the tutorial window with tabs."""
    if dpg.does_item_exist("tutorial_window"):
        dpg.delete_item("tutorial_window")

    with dpg.window(label="Tutorial", modal=True, tag="tutorial_window", width=500, height=500, no_resize=True):
        with dpg.tab_bar(tag="tutorial_tabs"):
            # Appraisal Bot Tab
            with dpg.tab(label="Appraisal Bot", tag="appraisal_tab"):
                dpg.add_text(APPRAISAL_PAGES[current_pages["appraisal"]], wrap=450, tag="appraisal_text")
                with dpg.group(horizontal=True, tag="appraisal_buttons"):
                    update_buttons("appraisal")

            # Equip Bot Tab
            with dpg.tab(label="Equip Bot", tag="equip_tab"):
                dpg.add_text(EQUIP_PAGES[current_pages["equip"]], wrap=450, tag="equip_text")
                with dpg.group(horizontal=True, tag="equip_buttons"):
                    update_buttons("equip")


def update_buttons(bot_type):
    """Updates navigation buttons dynamically based on the current page for a specific bot."""
    dpg.delete_item(f"{bot_type}_buttons", children_only=True)
    with dpg.group(horizontal=True, parent=f"{bot_type}_buttons"):
        if current_pages[bot_type] > 0:
            dpg.add_button(label="Back Page", callback=lambda: previous_page(bot_type), width=100)
        else:
            dpg.add_spacer(width=100)

        dpg.add_spacer(width=250)
        if current_pages[bot_type] < len(APPRAISAL_PAGES if bot_type == "appraisal" else EQUIP_PAGES) - 1:
            dpg.add_button(label="Next Page", callback=lambda: next_page(bot_type), width=100)


def next_page(bot_type):
    """Goes to the next page in the tutorial for a specific bot."""
    if bot_type == "appraisal" and current_pages[bot_type] < len(APPRAISAL_PAGES) - 1:
        current_pages[bot_type] += 1
        dpg.set_value("appraisal_text", APPRAISAL_PAGES[current_pages["appraisal"]])
    elif bot_type == "equip" and current_pages[bot_type] < len(EQUIP_PAGES) - 1:
        current_pages[bot_type] += 1
        dpg.set_value("equip_text", EQUIP_PAGES[current_pages["equip"]])
    update_buttons(bot_type)


def previous_page(bot_type):
    """Goes to the previous page in the tutorial for a specific bot."""
    if current_pages[bot_type] > 0:
        current_pages[bot_type] -= 1
        if bot_type == "appraisal":
            dpg.set_value("appraisal_text", APPRAISAL_PAGES[current_pages["appraisal"]])
        elif bot_type == "equip":
            dpg.set_value("equip_text", EQUIP_PAGES[current_pages["equip"]])
    update_buttons(bot_type)
