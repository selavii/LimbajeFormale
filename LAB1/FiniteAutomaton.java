package LAB1;

import java.util.*;

public class FiniteAutomaton {
    private Set<Character> states;
    private Set<Character> alphabet;
    private Map<Character, Map<Character, Character>> transitions;
    private Character initialState;
    private Set<Character> finalStates;

    public FiniteAutomaton() {
        states = new HashSet<>();
        alphabet = new HashSet<>();
        transitions = new HashMap<>();
        finalStates = new HashSet<>();
    }

    public void setStates(Set<Character> states) {
        this.states = states;
    }

    public void setAlphabet(Set<Character> alphabet) {
        this.alphabet = alphabet;
    }

    public void addTransition(Character fromState, Character symbol, Character toState) {
        if (!transitions.containsKey(fromState)) {
            transitions.put(fromState, new HashMap<>());
        }
        transitions.get(fromState).put(symbol, toState);
    }

    public void setInitialState(Character initialState) {
        this.initialState = initialState;
    }

    public void setFinalStates(Set<Character> finalStates) {
        this.finalStates = finalStates;
    }

    public boolean canReachString(String inputString) {

        Character currentState = initialState;


        for (char symbol : inputString.toCharArray()) {
            System.out.println("Current State: " + currentState + ", Symbol: " + symbol);


            if (!transitions.containsKey(currentState)) {
                System.out.println("No transitions defined for state " + currentState);
                return false;
            }


            if (!transitions.get(currentState).containsKey(symbol)) {
                System.out.println("No transition defined for symbol " + symbol + " in state " + currentState);
                return false;
            }


            currentState = transitions.get(currentState).get(symbol);
            System.out.println("New State: " + currentState);


            if (currentState == 'f') {
                System.out.println("Reached final state 'f'");
                return true;
            }
        }


        return finalStates.contains(currentState);
    }





    public Set<Character> getStates() {
        return states;
    }

    public Set<Character> getAlphabet() {
        return alphabet;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("States: ").append(states).append("\n");
        sb.append("Alphabet: ").append(alphabet).append("\n");
        sb.append("Transitions: ").append(transitions).append("\n");
        sb.append("Initial State: ").append(initialState).append("\n");
        sb.append("Final States: ").append(finalStates).append("\n");
        return sb.toString();
    }
}
