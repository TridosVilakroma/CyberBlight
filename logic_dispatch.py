import text,character_sheet,console,inventory,engine

test_console=console.Console()

def focus_switch():
    if engine.game.focus=='console_main_menu':
        test_console.main_menu()
    elif engine.game.focus=='console_terminal':
        test_console.terminal()
    elif engine.game.focus=='console_network':
        test_console.network()
    elif engine.game.focus=='console_email':
        test_console.email()
    elif engine.game.focus=='console_settings':
        test_console.settings()
def aux_state():
    pass