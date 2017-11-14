# -*- coding: utf-8 -*-
import sys

'''
Text Search
- read a string w from a text file
- output a DFA that accepts a string x if and only if w is a substring of x

@Author: Lawton C. Mizell

DFA (Q, Σ, δ, q', F)
Q  - states
Σ  - alphabet
δ  - transitions
q' - start_state
F  - accepting_states
'''
def main():
    #read file in from command line argumen
    string_w_file = sys.argv[1]

    with open(string_w_file, 'r') as f: # open file
        string_w = f.readlines()
        string_w = [x.strip() for x in string_w]

    char_in_string = ''.join(set(string_w[0])) # characters in the string_w
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    states = range(len(string_w[0])+1) # Q - states
    accepting_states = [len(string_w[0])] # F - accepting_states
    transitions = {} # δ - transitions
    print "Number of states:",len(string_w[0])+1
    print "Accepting states:",len(string_w[0])
    print "Alphabet: abcdefghijklmnopqrstuvwxyz"

    # Create empty transition table for # states x alphabet
    for i, i_val in enumerate(states):
        for j, j_val in enumerate(alphabet):
            transitions[(i_val,alphabet[j])] = 0
            if i_val in accepting_states:
                transitions[(i_val,alphabet[j])] = i_val # last row filled with accepting_state (loop on accepting)

    current_state = 0
    #print string_w[0]
    #fill transitions for the string itself
    for i in string_w[0]:
        transitions[(current_state,i)] = current_state + 1
        current_state = current_state + 1

    for k,v in sorted(transitions.iteritems()):
        for i in char_in_string:
            if i in k:
                print k,v

if __name__ == '__main__':
    main()
