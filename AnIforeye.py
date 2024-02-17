#Name: Colton Matthews
#File: AnIforeye.py
#Date: 9/24/2022

#Assign sequence of abbreviated words by number of characters
sequence = {
    2: {
        'at': '@',
        'to': '2',
        'be': 'b',
        'oh': 'o',
        'At': '@',
        'To': '2',
        'Be': 'B',
        'Oh': 'O'
    },
    3: {
        'and': '&',
        'one': '1',
        'won': '1',
        'too': '2',
        'two': '2',
        'for': '4',
        'bea': 'b',
        'bee': 'b',
        'sea': 'c',
        'see': 'c',
        'eye': 'i',
        'owe': 'o',
        'are': 'r',
        'you': 'u',
        'why': 'y',
        'And': '&',
        'One': '1',
        'Won': '1',
        'Too': '2',
        'Two': '2',
        'For': '4',
        'Bea': 'B',
        'Bee': 'B',
        'Sea': 'C',
        'See': 'C',
        'Eye': 'I',
        'Owe': 'O',
        'Are': 'R',
        'You': 'U',
        'Why': 'Y'
    },
    4: {
        'four': '4',
        'Four': '4'
    }
}

def abbreviate(string):
    lists = list(string)
    length = len(lists)
    current = 0
    while current < length - 1:
        #if the word has four characters
        if current < length - 3 and string[current : current + 4] in sequence[4]:
            lists[current] = sequence[4][string[current : current + 4]]
            lists[current + 1] = '\0'
            lists[current + 2] = '\0'
            lists[current + 3] = '\0'
            current += 4
        #If the word has three characters
        elif current < length - 2 and string[current : current + 3] in sequence[3]:
            lists[current] = sequence[3][string[current : current + 3]]
            lists[current + 1] = '\0'
            lists[current + 2] = '\0'
            current += 3
        #If the word has two characters
        elif string[current : current + 2] in sequence[2]:
            lists[current] = sequence[2][string[current : current + 2]]
            lists[current + 1] = '\0'
            current += 2
        #Default of one character goes to the next character
        else:
            current += 1
    #returns the list of characters before endline
    return ''.join((c for c in lists if c != '\0'))

def main():
    for _ in range(int(input())):
        #iterates to update the string by calling abbreviate method
        print(' '.join((abbreviate(string) for string in input().split())))

if __name__ == "__main__":
    main()