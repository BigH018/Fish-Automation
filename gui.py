import dearpygui.dearpygui as dpg

_UI_COMPONENTS = {}  # Dictionary to store references to GUI elements

def run_app(callbacks):
    """Sets up and runs the GUI application."""
    dpg.create_context()
    setup_ui(callbacks)
    dpg.create_viewport(title="Fish Bot -BigH", width=600, height=650)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

def setup_ui(callbacks):
    """Builds the GUI and links it to provided callbacks."""
    global _UI_COMPONENTS

    # Apply styling for a clean and modern look
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (40, 40, 40, 255))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (60, 60, 60, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Button, (70, 70, 70, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (100, 100, 100, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (230, 230, 230, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 8, 4)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 12, 8)
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 15, 15)

    dpg.bind_theme(global_theme)

    # Main window container
    with dpg.window(label="Fish Bot - BigH", width=600, height=650, no_resize=True):
        # Tabs container
        with dpg.tab_bar():
            # Original Tab
            with dpg.tab(label="Appraisal Bot"):
                setup_appraisal_tab(callbacks)

            # Equip Bot Tab
            with dpg.tab(label="Equip Bot"):
                setup_equip_tab(callbacks)


def setup_appraisal_tab(callbacks):
    """Sets up the Appraisal Bot tab."""
    global _UI_COMPONENTS

    # Main window
    with dpg.group(horizontal=False):
        dpg.add_text("Capture Area Settings", bullet=True)
        dpg.add_button(label="Set Capture Area", callback=callbacks["set_screen_area"], width=200)
        _UI_COMPONENTS["appraisal_area_label"] = dpg.add_text("No area selected", color=(200, 200, 200))

        dpg.add_separator()
        dpg.add_text("Target Word Settings", bullet=True)
        _UI_COMPONENTS["appraisal_target_word_input"] = dpg.add_input_text(label="Enter Target Word", width=250)

        dpg.add_separator()
        dpg.add_text("Hotkey Settings", bullet=True)
        hotkeys = [
            "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12",
            "Left Shift", "Right Shift", "Left Ctrl", "Right Ctrl",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        ]
        _UI_COMPONENTS["appraisal_start_hotkey"] = dpg.add_combo(label="Start Hotkey", items=hotkeys, default_value="F1")
        _UI_COMPONENTS["appraisal_stop_hotkey"] = dpg.add_combo(label="Stop Hotkey", items=hotkeys, default_value="F2")

        dpg.add_separator()
        dpg.add_text("Timing Settings", bullet=True)
        _UI_COMPONENTS["appraisal_wait_time_input"] = dpg.add_input_float(
            label="Wait Time (Seconds)", 
            default_value=0.05, 
            min_value=0.01, 
            step=0.01, 
            width=200
        )

        dpg.add_separator()
        dpg.add_text("Bot Status", bullet=True)
        _UI_COMPONENTS["appraisal_status_label"] = dpg.add_text("Waiting for settings...", wrap=500, color=(150, 150, 150))

        dpg.add_spacer(height=10)
        dpg.add_button(label="Save Settings", callback=lambda: save_settings("appraisal", callbacks), width=200)

        dpg.add_spacer(height=10)
        dpg.add_button(label="Tutorial", callback=callbacks["show_tutorial"], width=200)



def setup_equip_tab(callbacks):
    """Sets up the Equip Bot tab."""
    global _UI_COMPONENTS

    with dpg.group(horizontal=False):
        # Hotkey Settings
        dpg.add_text("Hotkey Settings", bullet=True)
        hotkeys = [
            "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12",
            "Left Shift", "Right Shift", "Left Ctrl", "Right Ctrl",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        ]
        _UI_COMPONENTS["equip_hotkey"] = dpg.add_combo(
            label="Equip Hotkey", 
            items=hotkeys, 
            default_value="F3"
        )

        dpg.add_separator()

        # Timing Settings
        dpg.add_text("Timing Settings", bullet=True)
        _UI_COMPONENTS["equip_default_wait_time_input"] = dpg.add_input_float(
            label="Default Wait Time (Seconds)",
            default_value=0.8,  # Matches the default_wait_time in equip.py
            min_value=0.01,
            step=0.1,
            width=200
        )
        _UI_COMPONENTS["equip_click_wait_time_input"] = dpg.add_input_float(
            label="Click Wait Time (Seconds)",
            default_value=0.2,  # Matches the click_wait_time in equip.py
            min_value=0.01,
            step=0.1,
            width=200
        )

        dpg.add_separator()

        # Bot Status
        dpg.add_text("Bot Status", bullet=True)
        _UI_COMPONENTS["equip_status_label"] = dpg.add_text(
            "Waiting for settings...", 
            wrap=500, 
            color=(150, 150, 150)
        )

        dpg.add_spacer(height=10)

        # Save Settings Button
        dpg.add_button(
            label="Save Settings", 
            callback=lambda: save_settings("equip", callbacks), 
            width=200
        )



def save_settings(tab, callbacks):
    """Handles saving settings via GUI for a specific tab."""
    if tab == "appraisal":
        settings = {
            "start_hotkey": get_gui_value("appraisal_start_hotkey", "F1"),
            "stop_hotkey": get_gui_value("appraisal_stop_hotkey", "F2"),
            "wait_time": get_gui_value("appraisal_wait_time_input", 0.05),
        }
    elif tab == "equip":
        settings = {
            "equip_hotkey": get_gui_value("equip_hotkey", "F3"),
            "default_wait_time": get_gui_value("equip_default_wait_time_input", 0.8),  # Ensure this key exists
            "click_wait_time": get_gui_value("equip_click_wait_time_input", 0.2),  # Ensure this key exists
        }

    # Pass settings to the respective bot
    callbacks[f"save_settings_{tab}"](settings)
    update_status_label(tab, "Settings saved!")

def update_area_label(area_text):
    """Updates the area label in the GUI."""
    if "appraisal_area_label" in _UI_COMPONENTS:
        dpg.set_value(_UI_COMPONENTS["appraisal_area_label"], area_text)


def get_gui_value(key, default=None):
    """Safely retrieves a value from the GUI components."""
    return dpg.get_value(_UI_COMPONENTS[key]) if key in _UI_COMPONENTS else default

def update_status_label(tab, status):
    """Updates the status label in the GUI for the specified tab."""
    label_key = f"{tab}_status_label"
    if label_key in _UI_COMPONENTS:
        dpg.set_value(_UI_COMPONENTS[label_key], status)