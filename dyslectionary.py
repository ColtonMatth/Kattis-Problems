#Name: Colton Matthews
#File: dislectionary.py
#Date: 9/23/2022

def sort_print(longest, words):
    for w in sorted(words, key = lambda w: w[:: -1]):
        padding = ' ' * (longest - len(w))
        print(f'{padding}{w}')

def main():
    longest, words = -1, []
    while True:
        try:
            w = input()
            if not w:
                sort_print(longest, words)
                print()
                longest, words = -1, []
            else:
                longest = max(longest, len(w))
                words.append(w)
        except EOFError:
            sort_print(longest, words)
            break


if __name__ == "__main__":
    main()