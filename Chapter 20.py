# Chapter 20: Command-Line Tools with Clean Code

import argparse

def main():
    parser = argparse.ArgumentParser(description="Example CLI")
    parser.add_argument('name', help='Your name')
    parser.add_argument('--count', type=int, default=1, help='Number of greetings')

    args = parser.parse_args()

    for _ in range(args.count):
        print(f"Hello, {args.name}!")

if __name__ == '__main__':
    main()