from screeninfo import get_monitors
import pygetwindow as gw

def display_monitor_info():
    monitors = get_monitors()

    if monitors:
        print("Informações dos Monitores:")
        for idx, monitor in enumerate(monitors):
            position = "Principal" if monitor.is_primary else "Secundário"
            print(f"Monitor {idx + 1}: {monitor.name} - {monitor.width}x{monitor.height} - {position}")
    else:
        print("Nenhum monitor encontrado.")

# Exibir as informações dos monitores
display_monitor_info()
