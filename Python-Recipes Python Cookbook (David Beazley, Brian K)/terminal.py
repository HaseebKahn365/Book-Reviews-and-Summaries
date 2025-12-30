import argparse
import os

def draw_banner():
    parser = argparse.ArgumentParser(description = "Draw on terminal banner")
    parser.add_argument('-m', '--message', default='System online', help = "helper text showing")

    args = parser.parse_args()

    try:
        columns, lines = os.get_terminal_size()
    except OSError:
        columns = 80

    print("-"*columns)
    print(args.message.center(columns))
    print("-"*columns)

if __name__ == "__main__":
    draw_banner()