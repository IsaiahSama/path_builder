#! python3

# Takes a dictionary of prebuilt paths. When given a key from the command line, prints out the path

from sys import argv
from os import chdir, listdir, getcwd
try:
    from pyperclip import copy
except ImportError:
    print("Having the pyperclip module is recommend for full functionality. Do this by typing: 'pip install pyperclip' in the command line")

# The base path
BASE = "D:\\Programs\\code\\Python\\"

def main():
    """Main function, which takes care of the main handling."""
    try:
        keys = get_args()
    except IndexError:
        print("No arguments were provided. Use in format getpath.py dir_name_1 dir_name_2")
        input()
        raise SystemExit
    
    valid_count = find_path(keys)
    if not valid_count:
        print("Could not find any directories matching any of the names provided.")
        input(": ")
        raise SystemExit
    
    if valid_count < len(keys):
        print("Could not find valid directories for all the given paths. Here's what we have so far.")
    
    print(getcwd())
    try:
        copy(str(getcwd()))
        print("Copied path to clipboard")
    except NameError:
        pass
    input()

def get_args():
    """Returns the arguments from the command line"""
    return argv[1:]

def find_path(args):
    """Function that searches through directories for the first match of a given arg, and returns an integer of how many of the directories were valid
    
    Will use chdir to navigate through"""
    chdir(BASE)

    valid = 0

    for arg in args:
        dir_name = find_matching_dir(arg)
        if dir_name:
            valid += 1
            chdir(dir_name)
    return valid 

def find_matching_dir(name):
    """Function that when given a name, will look for directories that have the given name within them, and returns the first match."""
    for dir_name in listdir():
        if name.lower() in dir_name.lower(): return dir_name
    return False

main()