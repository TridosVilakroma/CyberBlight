import engine
import time

def prologue():
    engine.slow_type('The world has grown in population and technology.\n',100)
    time.sleep(1)
    engine.slow_type('''Computers created advanced algorithms that grew 
    in complexity exponentially for centuries.''',100)
    time.sleep(1)
    engine.slow_type('''Long ago civilization moved into an era called The Nexus.
    Where the physical world is being merged into the cyber world.''',100)
    time.sleep(1)
    engine.slow_type('''World leaders praise the machines, attributing peace and prosperity to them. 
    However there are factions who claim that true humanity was given up in exchange for 
    any percieved benefits the machines have brought.''',150)
    time.sleep(1)
    engine.slow_type('''Hacker groups have formed in response to this cyber blight.
    They must remain cloaked and agile to avoid detection. ''',150)
    time.sleep(2)
    engine.slow_type('They are always recruting',new_line=False)
    engine.slow_type('.',new_line=False)
    time.sleep(.5)
    engine.slow_type('.',new_line=False)
    time.sleep(.5)
    engine.slow_type('.',new_line=False)
    time.sleep(.5)
    engine.slow_type('.',new_line=False)

if __name__=='main':
    prologue()