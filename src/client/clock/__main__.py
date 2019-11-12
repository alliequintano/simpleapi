import sys
from clock.current_time import display_current_time

def main():
    """Usage: client [OPTIONS] COMMAND

      A CLI wrapper for the client clock application.
    
    Options:
      --help  Show this message.

    Commands:
      clock   Display the current time.
    
    """

    args = sys.argv[1:]
    for arg in args:
        if (arg == 'clock'):
            display_current_time()
    print(main.__doc__)

if __name__ == '__main__':
    main()