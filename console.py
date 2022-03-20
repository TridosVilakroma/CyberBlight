from engine import *

class Console():
    def __init__(self) -> None:
        pass

    def main_menu(self):
        action=drop_down('Console',
        {
            'Terminal':'console_terminal',
            'Network':'console_network',
            'Email':'console_email',
            'Settings':'console_settings'
            })
        game.focus=action

    def terminal(self):
        action=drop_down('Terminal',
        {
            'Terminal':'console_terminal',
            'Network':'console_network',
            'Email':'console_email',
            'Settings':'console_settings'
            })
        game.focus=action

    def network(self):
        pass

    def email(self):
        clear_console()
        action=drop_down('E-mail',
        {
            'Inbox':'console_email_inbox',
            'Close':'console_main_menu'
        },
        '>>')
        game.focus=action

    def inbox(self):
        pass

    def settings(self):
        pass
