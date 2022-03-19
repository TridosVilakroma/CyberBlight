import os,sys,time,random

'''these functions should be used throughout the project to automate
repetetive or complex tasks.
this is the 'engine' of our game.
'''

def slow_type(text,typing_speed= 50,new_line=True):
    """print function that feels like a human is typing.
    
    typing_speed is an integer that equals words per minute.
    
    new_line is a boolean, it controls weather the console will begin 
    the next print operation on the same line or a new line.
    """
    for letter in text:
        #this looks at each letter and prints it, then waits a random amount of time.
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    if new_line:
        print ('')

def drop_down(prompt,items={},input_prompt='>'):
    '''makes a drop down menu from a dict of choices

    returns: a value from the dict passed into it,
    there is no way to exit this menu loop without a valid selection.

    if you want to add an exit clause, than make an exit value 
    in your dict to be returned and then handle that return value
    from your calling code.

    example:

    selection=drop_down(prompt,items={},input_prompt='>')
    if selection == exit_value:
        break

    input_prompt defaults to a single '>'
    it is recommended to modify this to show how many menus
    deep a player is.

    if the input is not recognized too many times the menu 
    prompt will be re-printed to prevent the player from having to
    scroll up to read the available options.

    input will be valid if a key from the dict is typed out in upper
    or lowercase, or if the index of the menu item is input
    '''
    print(prompt+':')
    for index,item in enumerate(items):
        print(f'[{index+1}] {item}')
    typo=0
    while True:
        if typo==4:
            typo=0
            print('\n'+prompt+':')
            for index,item in enumerate(items):
                print(f'[{index+1}] {item}')
        selection=input(input_prompt)
        try:
            selection = int(selection)-1
            for index,item in enumerate(items):
                if index == selection:
                    return items[item]
        except ValueError:
            if selection in items:
                return items[selection]
        print('\nThat is not on the list.\nVerify your selection.')
        typo+=1

def clear_console():
    '''removes all text from the console preventing scrolling up'''

    os.system('cls')
    print('\n\n')

def jump(amount=1):
    '''prints new lines
    
    new lines are blank spaces between the last thing printed and the next.
    enter an amount of lines to skip. defaults to 1
    '''
    print('\n'*amount)

