# -*- coding: utf-8 -*-
import sys

'''
Simulate a DFA
- read description of a DFA N from a txt file
- read any number of strings over N's alphabet from another txt file
- indicate ( to std output ) whether N accepts or rejects each of the strings.

@Author: Lawton C. Mizell

DFA (Q, Σ, δ, q', F)
Q  - states
Σ  - alphabet
δ  - transitions
q' - start_state
F  - accepting_states
'''
class DFA:
    current_state = None;

    #initalize class variables based on DFA tuple
    def __init__(self, states, alphabet, transitions, start_state, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accepting_states = accepting_states

    # transition to state based on state and alphabet
    def transition_to_state(self, string_val):
        if ((self.current_state, string_val) not in self.transitions.keys()):
            self.current_state #stay in the current state
        else:
            self.current_state = self.transitions[(self.current_state, string_val)] # transition

    # determine whether or not we are in the accepting state
    def in_accept_state(self):
        #print "last current state ",self.current_state
        if self.current_state in self.accepting_states:
            print "accept"
        else:
            print "reject"

    # simulate a finite-state machine that accepts and rejects strings of symbols
    def simulate_DFA(self, input_string):
        self.current_state = self.start_state;
        for string_val in input_string:
            #print "string val ", string_val
            #print "current state ",self.current_state
            self.transition_to_state(string_val); # transition
        return self.in_accept_state() # are we in the accepting state ?

def main():
    #two files read in from command line arguments
    DFA_descritpion = sys.argv[1]
    strings_alphabet = sys.argv[2]

    states = [] # Q - states
    alphabet = [] # Σ - alphabet
    transitions = {} # δ - transitions
    start_state = 0 # q' - start_state
    accepting_states = [] # F - accepting_states

    transition_table = [] # temp variable to hold transitions
    content = [] #strings to read in

    with open(strings_alphabet, 'r') as f: # open file
        content = f.readlines()
        content = [x.strip() for x in content]

    with open(DFA_descritpion, 'r') as f: # open file
        for i, line in enumerate(f): # read lines
            if i == 0:
                states = range(int(line.split(":")[1]))
            elif i == 1:
                accepting_states_raw = line.split(":")[1].strip().split(" ")
                for i in accepting_states_raw:
                    accepting_states.append(int(i))
            elif i == 2:
                for i in line.split("Alphabet: ",1)[1].replace("\n", ""):
                    alphabet.append(i)
            elif i > 2:
                transition_table.append(line.strip())

        for i, val in enumerate(states):
            for j, line in enumerate(alphabet):
                transitions[(val,alphabet[j])] = int(transition_table[i].split()[j])

    dfa = DFA(states, alphabet, transitions, start_state, accepting_states)
    #print "alphabet ",alphabet
    #print "states ",states
    #print "accepting_states ",accepting_states
    #print transitions
    for i in content:
        #print "string:"+i
        dfa.simulate_DFA(i)

if __name__ == '__main__':
    main()
