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
    #read file in from command line argument
    string_w_file = sys.argv[1]

    with open(string_w_file, 'r') as f: # open file
        string_w = f.readlines()
        string_w = [x.strip() for x in string_w]

    char_in_string = ''.join(set(string_w[0])) # characters in the string_w
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    states = range(len(string_w[0])+1) # Q - states
    accepting_states = [len(string_w[0])] # F - accepting_states
    transitions = {} # δ - transitions
    reference_table = {}
    possible_strings_table = {}
    print "Number of states:",len(string_w[0])+1
    print "Accepting states:",len(string_w[0])
    print "Alphabet: abcdefghijklmnopqrstuvwxyz"

    # Create empty transition table for # states x alphabet
    for i, i_val in enumerate(states):
        for j, j_val in enumerate(alphabet):
            string_w_whole = string_w[0]
            if i < len(string_w_whole):
                if j_val == string_w_whole[i]:
                    transitions[(i_val,alphabet[j])] = i_val+1
                else:
                    transitions[(i_val,alphabet[j])] = 0
            if i_val in accepting_states:
                transitions[(i_val,alphabet[j])] = i_val # last row filled with accepting_state (loop on accepting)

    # build reference table
    curr_string=""
    for i, i_val in enumerate(string_w[0]):
        curr_string=curr_string+i_val
        reference_table[curr_string]=i+1

    # build possible strings table
    for k,v in sorted(reference_table.iteritems()):
        for i in char_in_string:
            if k+i not in reference_table.keys():
                possible_strings_table[k+i]=v

    # fill loop back transitions
    for k,v in sorted(reference_table.iteritems()):
        for k2,v2 in possible_strings_table.iteritems():
            if v not in accepting_states and v2 not in accepting_states:
                if k2.endswith(k):
                    transitions[(v2,k2[-1])]=v

    # print transitions table
    for i in states:
        for j in alphabet:
            print transitions[(i,j)],
        print

if __name__ == '__main__':
    main()
