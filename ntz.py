# add your code in this file
"""
note taker application built for Python 3.9.*.
designed for ZCW Data 3.1 by JJ Heffernan

Installation Commands (in shell):
    echo "#!/usr/bin/env python3" | cat - ntz.py
    chmod +x ntz.py
    cp ./ntz.py /usr/local/bin/ntz.py
    echo "alias ntz='./ntz.py'" >> ~/.bashrc
    source ~/.bashrc
"""
import os
import sys
import datetime

# argument variable declaration
argument = globals()[sys.argv[1]](*sys.argv[2:])  # static global variable that saves input string into mem

# help message for input
help_msg = """Commands: 
  $ ./ntz -r "note"         # remember/Add a new note with name "note"
  $ ./ntz -l                # List notes, ./ntz also returns this
  $ ./ntz -e "note"         # edits existing notes
  $ ./ntz -f "note"         # forget/delete note
  $ ./ntz -c "category"     # move note to new "category", or append to existing category
  $ ./ntz clear             # empties all notes
  $ ./ntz help              # List Commands"""


def ntz_help():
    # writes the help to the CLI
    sys.stdout.buffer.write(help_msg.encode('utf-8'))
    # Use [-r] for remember. Using [-r] on its own will save to the default To-Do category
    # Using -r is the same as `ntz -c To-Do "my first note"`
    # -c flag to create a new category or direct a note to an existing category
    # help function for commands
    # Use [-f] for forget. [-f] requires a category and note number


# add note (-r command)
def add(note):
    f = open('note.txt', 'a')
    f.write(note)
    f.write('\n')
    f.close()
    # s = '"'+s+'"' #
    print(f'Added note {note}')  # need to fix to allow for different files


# edit selected note
def edit(note_name, note_to_add):
    f = open(note_name, 'w')
    f.write(note_to_add)
    f.close()
    print(f'Edited note {note_name}')  # need to fix to allow for different files
    # pass


# create a new note within current category
def create_note(note_name, note_to_add):
    f = open(note_name, 'x')
    f.write(note_to_add)
    f.close()
    print(f'Created note {note_name}')  # need to fix to allow for different files
    # pass


# create new category of notes
def create_cat(cat_name, note_to_add):
    pass


# list function (-l or ntz)
def ls():
    # add
    pass
    # try:
    #     nec()


# ---- directory items ----
def check_status():
    # try:
    #     note_id = int(note_num)
    pass


def clear_notes():
    # clear all notes in memory
    # make sure to prompt with yes/no
    pass


def forget_note():
    # delete specific note
    pass

# main function
def cli():
    # i would like to add the if/else here
    args = get_args()

    # might want to add another try/except or if else here.
    # that could potentially add the multi-line capability

    # note_to_add is the string input to be appended to the file
    # note_name is the category address or note address
    if args[1] == '-r' and len(args[2:]) == 0:  # remember note in ToDo
        pass
    elif args[1] == '-l':  # list all notes
        pass
    elif args[1] == '-e':  # edit existing note (line replace)
        pass
    elif args[1] == '-f':  # forget note
        pass
    elif args[1] == '-c':
        pass
    elif args[1] == 'help':
        pass
    elif args[1] == 'clear':
        pass
    # null operator
    elif args[1] == '':
        ls()
    pass


# get arguments for parsing
def get_args():
    return os.sys.argv


def main():
    try:
        # if else is contained within CLI()
        cli()
        # argument = globals()[sys.argv[1]](*sys.argv[2:])
        # exception handling
    except Exception as e:
        # print exception
        # all 3 do the same thing different ways
        # print(e)
        # sys.stdout.buffer.write(f'Error: {str(e)} \n'.encode('utf-8'))
        os.system(f'echo "Error: {e} \n"')

        ntz_help()


# main program
if __name__ == '__main__':
    # argument = globals()[sys.argv[1]](*sys.argv[2:]) # might also need to be declared here for CLI?
    main()

  
# run the main function
# cli()
