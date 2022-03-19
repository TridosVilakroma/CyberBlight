from engine import *

class Console():
    def __init__(self) -> None:
        pass

    def main_menu(self):
        action=drop_down('Console',
        {
            'Terminal':self.terminal,
            'Network':self.network,
            'Email':self.email,
            'Settings':self.settings
            })
        action()

    def terminal(self):
        print('hey')

    def network(self):
        pass

    def email(self):
        pass

    def settings(self):
        pass
