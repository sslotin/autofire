import sys
import fire

def main():
    if len(sys.argv) == 1:
        print("Usage: fire <filename> <fn> <args...>")
        print()
        print("See https://github.com/google/python-fire")
    else:
        # TODO: in some extremely rare cases there might be a problem
        # with the namespace, so we might want to start a separate process

        filename = sys.argv.pop(1)

        with open(filename) as file:
            exec(file.read())

        fire.Fire()

if __name__ == '__main__':
    main()
