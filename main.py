import os,sys,time,random
from engine import *
from save_data import data_IO

clear_console()
slow_type('\n\n-Welcome to the world of Cyber Blight-\n',1000)
time.sleep(1)
profile=drop_down('Select your file',data_IO.existing_files(r'save_data\saves'))

if profile == 'New Game':
    player_name=input('    Enter your name:\n    >>')
    data_IO.save(profile,player_name)





# slow_type('The world has grown in knowledge and technology.',75)
# time.sleep(1)
# slow_type('''Computers have created more advanced computers for 
# so long that most of humanity does not remember the beginning.''',100)
# time.sleep(1)
# slow_type('This has led to ',25,False)
# slow_type('disaster',1000,False)
# slow_type('.',1,False)
# slow_type('.',1,False)
# slow_type('.',1,False)
# slow_type('.',1,False)
# time.sleep(10)