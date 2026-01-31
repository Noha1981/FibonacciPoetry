import dearpygui.dearpygui as dpg
import sys
import pathlib

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

def build_ui():
    dpg.create_context()
    width = 1028
    height = 768
    with dpg.window(label="Fibonacci Poetry inspired by Brian Bilston", width=width, height=height, no_collapse=True):
        dpg.add_spacing(count=1)

        # Eingabebereich
        dpg.add_text("Eingabetext", tag="lbl_Eingabe")
        dpg.add_input_text(tag="fib_input", width=-1,height = 10, hint="Gib hier den Eingabetext ein")

        dpg.add_separator()

        # Ausgabebereich
        dpg.add_text("Fibonacci Poetry Output")
        # Mehrzeilig und readonly, damit Zeilenumbrüche akzeptiert werden und Ausgabe nicht editierbar ist
        dpg.add_input_text(tag="fib_output", multiline=True, height=200, width=-1, readonly=True)

        dpg.add_spacing(count=1)

        # Button
        dpg.add_button(label="Poetry Text", callback=on_poetry_click)

    dpg.create_viewport(title="Fibonacci Poetry", width=width, height=height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

# Nur starten, wenn das Modul als Skript ausgeführt wird (wichtig, damit importierende Tests/Module nicht die GUI starten)
if __name__ == "__main__":
    build_ui()
