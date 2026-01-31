from idlelib.multicall import MC_ENTER
from tkinter.constants import CENTER

import dearpygui.dearpygui as dpg
import sys
import pathlib
import webbrowser

# Robusteren Import von FibPoetry anbieten (falls Projektpfad nicht in sys.path)
try:
    import FibPoetry
except Exception:
    project_dir = pathlib.Path(__file__).resolve().parent
    if str(project_dir) not in sys.path:
        sys.path.append(str(project_dir))
    import FibPoetry

def on_poetry_click(sender, app_data, user_data):
    text = dpg.get_value("fib_input")
    try:
        result = FibPoetry.fibo_poem(text)
    except Exception as e:
        result = f"Fehler beim Erzeugen des Gedichts: {e}"
    dpg.set_value("fib_output", result)

def add_data_menu_with_impressum(window_tag: str = "main_window"):
    url = "https://www.facebook.com/BrianBilston/posts/pfbid0PnieZPXmdzgNy6vWzRjFkDsKch4YvTCEJv65LS5sGa4daYoygbHJcG1TVK5Nw9SGl"

    # Menüleiste im angegebenen Fenster anlegen
    with dpg.menu_bar(parent=window_tag):
        with dpg.menu(label="Data"):
            dpg.add_menu_item(label="Impressum", callback=lambda s, a, u: dpg.show_item("impressum_win"))

    # Modal-Popup (initial versteckt)
    with dpg.window(label="Impressum", modal=True, show=False, tag="impressum_win", width=480, height=220):
        dpg.add_text("Datum: 31.01.2026")
        dpg.add_text("Version: 1.0.0")
        dpg.add_text("Author: Norman Fober")
        dpg.add_text(" -------- ")
        dpg.add_text("Die Software ist angelehnt an den FB Post von Brian Bilston")
        dpg.add_spacing(count=1)
        dpg.add_text("Link:")
        dpg.add_same_line()
        dpg.add_text(url, color=[0, 120, 215])

        dpg.add_spacing(count=2)
        # Buttons: Link öffnen und Popup schließen
        dpg.add_button(label="Öffne Link", callback=lambda s, a, u: webbrowser.open(url))
        dpg.add_same_line()
        dpg.add_button(label="Schließen", callback=lambda s, a, u: dpg.hide_item("impressum_win"))

def build_ui():
    dpg.create_context()
    width = 1028
    height = 768
    with dpg.window(label="Fibonacci Poetry inspired by Brian Bilston", width=width, height=height, no_collapse=True):

        add_data_menu_with_impressum("main_window")
        dpg.add_spacing(count=1)

        # Eingabebereich
        dpg.add_text("Eingabetext", tag="lbl_Eingabe")
        dpg.add_input_text(tag="fib_input", width=-1, hint="Gib hier den Eingabetext ein")

        dpg.add_separator()

        # Ausgabebereich
        dpg.add_text("Fibonacci Poetry Output")
        # Mehrzeilig und readonly, damit Zeilenumbrüche akzeptiert werden und Ausgabe nicht editierbar ist
        dpg.add_input_text(tag="fib_output", multiline=True, height=200, width=-1, readonly=True)

        dpg.add_spacing(count=1)

        # Button
        dpg.add_button(label="Poetry Text", height=20,callback=on_poetry_click)

    dpg.create_viewport(title="Fibonacci Poetry", width=width, height=height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

# Nur starten, wenn das Modul als Skript ausgeführt wird (wichtig, damit importierende Tests/Module nicht die GUI starten)
if __name__ == "__main__":
    build_ui()
