# add your code in this file
import os
import sys
import datetime

# help message for input
help_msg = """Commands: 
  $ ./ntz -r "note"         # remember/Add a new note with name "note"
  $ ./ntz -l                # List notes
  $ ./ntz -e                # edits existing notes
  $ ./ntz -f "note"         # forget/delete note
  $ ./ntz -c "category"     # move note to new "category"
  $ ./ntz clear             # empties all notes
  $ ./ntz help              # List Commands"""


# help function for commands
def ntz_help():
    # writes the help to the CLI
    sys.stdout.buffer.write(help_msg.encode('utf-8'))


# add note (-r command)
def add(note):
    f = open('note.txt', 'a')
    f.write(note)
    f.write('\n')
    f.close()
    s = '"'+s+'"'
    print(f'Added note {s}')


# list function (-l or ntz)
def ls():
    pass
    # try:
    #     nec()


# main function
def cli():
    pass


#get arguments for parsing
def get_args():
    return os.sys.argv


def main():
    try:
        args = get_args()

        if args[1] == '-r' and len(args[2:]) == 0:
            pass
        elif args[1] == '-l':
            pass
        elif args[1] == '-e':
            pass
        elif args[1] == '-f':
            pass
        elif args[1] == '-c':
            pass
        elif args[1] == 'help':
            pass
        elif args[1] == 'clear':
            pass

    except Exception as e:
        print(e)
        sys.stdout.buffer.write(f'Error: {str(e)} \n'.encode('utf-8'))
        ntz_help()


# main program
if __name__ == '__main__':
    main()

  
# run the main function
# cli()
