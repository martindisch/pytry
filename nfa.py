from collections import deque


class NFA:
    """A nondeterministic finite automaton."""

    def __init__(self, transitions, initial, accepting):
        """Instantiate a new NFA.

        The states (and therefore the keys in the transition dictionaries)
        can be integers or strings, as long as this is done consistently.

        Parameters
        ----------
        transitions : dict
            Dictionary with states as keys and dictionaries for transitions.
            The keys in the transition dictionaries are the characters that
            are allowed in that state and lead to a list of next states.
            Example with integers as states:
            transitions = {
                0: {'a': [0, 1], 'c': [3]},
                1: {'b': [2, 4]},
                2: {'a': [3], 'c': [0, 4]},
                3: {'c': [3]},
                4: {'c': [1]}
            }
        initial : int, str
            The initial state
        accepting : list of int or str
            The set of accepting states
        """
        self.transitions = transitions
        self.initial = initial
        self.accepting = accepting

    def __repr__(self):
        return "NFA(transitions={}, initial={}, accepting={})".format(
            self.transitions, self.initial, self.accepting)

    def consume(self, input):
        """Return whether the input is accepted by this NFA.

        Parameters
        ----------
        input : str
            The input string

        Returns
        -------
        bool
            True if the NFA accepts this input, False otherwise
        """
        # This holds all steps (tuples of state and input) that are checked
        steps = deque()
        # Put initial state into steps
        steps.append((self.initial, input))
        # Start working on the steps
        while steps:
            # Grab a step
            state, string = steps.popleft()
            # Finish prematurely if input has been accepted
            if state in self.accepting and len(string) == 0:
                return True
            # Skip this step if there is no input or transition
            if len(string) == 0 or string[0] not in self.transitions[state]:
                continue
            # Enqueue steps for all transitions
            for next_state in self.transitions[state][string[0]]:
                steps.append((next_state, string[1:]))
        # If we arrived here, the input has not been accepted
        return False


if __name__ == "__main__":
    transitions = {
        0: {'a': [0, 1], 'c': [3]},
        1: {'b': [2, 4]},
        2: {'a': [3], 'c': [0, 4]},
        3: {'c': [3]},
        4: {'c': [1]}
    }
    nfa = NFA(transitions, 0, [1, 3])
    print(nfa.consume("abc"))

    d1 = {
        0: {'0': [1]},
        1: {'1': [2]},
        2: {'1': [2]}
    }
    dfa1 = NFA(d1, 0, [2])
    print(dfa1.consume("011"))

    d2 = {
        0: {'0': [1]},
        1: {'0': [1], '1': [2]},
        2: {'0': [3]},
        3: {'1': [4]},
        4: {}
    }
    dfa2 = NFA(d2, 0, [4])
    print(dfa2.consume("0000101"))

    d3 = {
        0: {'0': [1]},
        1: {'0': [2]},
        2: {'0': [3]},
        3: {'0': [3], '1': [2]}
    }
    dfa3 = NFA(d3, 0, [2])
    print(dfa3.consume("00000101"))

    d4 = {
        'q0': {'0': ['q1']},
        'q1': {'0': ['q2']},
        'q2': {'0': ['q3']},
        'q3': {'0': ['q3'], '1': ['q2']}
    }
    dfa4 = NFA(d4, 'q0', ['q2'])
    print(dfa4.consume("00000101"))
