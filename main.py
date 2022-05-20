import os,sys,time,random
from engine import *
from save_data import data_IO
import text,character_sheet,console,inventory,logic_dispatch

clear_console()
slow_type('\n\n-Welcome to the world of Cyber Blight-\n',100)
time.sleep(1)
profile=drop_down('Select your file',data_IO.existing_files(r'save_data\saves'))

if profile == 'New Game':
    player_name=input('    Enter your name:\n    >>')
    player=character_sheet.Player(player_name)
    data_IO.save(player,player_name)
    clear_console()
    text.prologue()
    time.sleep(2)
    jump(3)
    slow_type('You sit down at your console')
    jump(2)
else:
    save_data=data_IO.load(profile)
    clear_console()

while True:
    logic_dispatch.focus_switch()
    logic_dispatch.aux_state()

