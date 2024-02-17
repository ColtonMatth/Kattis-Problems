#Name: Colton Matthews
#Class: MCS-394
#Date: 9/13/2022

#assign notes to numbered fingers as provided from Kattis
note_to_fingers = {
    'c': (2, 3, 4, 7, 8, 9, 10),
    'd': (2, 3, 4, 7, 8, 9),
    'e': (2, 3, 4, 7, 8),
    'f': (2, 3, 4, 7),
    'g': (2, 3, 4),
    'a': (2, 3),
    'b': (2,),
    'C': (3,),
    'D': (1, 2, 3, 4, 7, 8, 9),
    'E': (1, 2, 3, 4, 7, 8),
    'F': (1, 2, 3, 4, 7),
    'G': (1, 2, 3, 4),
    'A': (1, 2, 3),
    'B': (1, 2),
}

t = int(input()) #taking input of how many sequences you'll be entering
for _ in range(t): #taking t for number of sequence of the user will enter
    notes = input()

    press_count = {i:0 for i in range(1, 11)} #display the index of numbers from 1-10
    last_fingers = () #creating an empty tuple
    for n in notes: #for loop for each note
        for finger in note_to_fingers[n]: #checks the tuple of the note n
            if finger not in last_fingers: #if finger not in last_finger tuple, then adds finger from note n to press_count by 1
                press_count[finger] += 1 
        last_fingers = note_to_fingers[n] #taking the note before going to n+1, so n is being stored to last_fingers
    #prints the display of ten numbers that represents the finger[index] from 1-10 and how many fingers are being pressed
    # from the sequence of notes.
    print(*press_count.values()) 