import os

def d():
    '''creates a divider line in the terminal'''
    print('=' * 75)

def clear():
    '''clears the terminal'''
    os.system('cls' if os.name == 'nt' else 'clear')