import sys
import fire

def main():
    filename = sys.argv.pop(1)

    with open(filename) as file:
        exec(file.read())

    fire.Fire()

if __name__ == '__main__':
    main()
