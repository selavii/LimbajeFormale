package LAB1;
import java.util.*;

public class Grammar {
    private Set<Character> VN;
    private Set<Character> VT;
    private Map<Character, List<String>> P;

    public Grammar() {
        VN = new HashSet<>(Arrays.asList('S', 'B', 'D', 'Q'));
        VT = new HashSet<>(Arrays.asList('a', 'b', 'c', 'd'));
        P = new HashMap<>();
        P.put('S', Arrays.asList("aB", "bB"));
        P.put('B', Collections.singletonList("cD"));
        P.put('D', Arrays.asList("dQ", "a"));
        P.put('Q', Arrays.asList("bB", "dQ"));
    }

    public Set<Character> getVN() {
        return VN;
    }

    public Set<Character> getVT() {
        return VT;
    }

    public Map<Character, List<String>> getP() {
        return P;
    }

    public List<String> generateStrings(int count) {
        Set<String> uniqueStrings = new HashSet<>();
        List<String> validStrings = new ArrayList<>();

        while (uniqueStrings.size() < count) {
            StringBuilder sb = new StringBuilder();
            generateStringHelper('S', sb);
            String generatedString = sb.toString();
            if (uniqueStrings.add(generatedString)) {
                validStrings.add(generatedString);
            }
        }

        return validStrings;
    }

    private void generateStringHelper(char symbol, StringBuilder sb) {
        List<String> productions = P.get(symbol);
        if (productions != null) {

            String production = productions.get(new Random().nextInt(productions.size()));

            for (char c : production.toCharArray()) {
                if (VN.contains(c)) {

                    generateStringHelper(c, sb);
                } else {

                    sb.append(c);
                }
            }
        }
    }

    public FiniteAutomaton convertToFiniteAutomaton() {
        FiniteAutomaton finiteAutomaton = new FiniteAutomaton();

        finiteAutomaton.setStates(VN);
        finiteAutomaton.setAlphabet(VT);


        for (char symbol : P.keySet()) {
            for (String production : P.get(symbol)) {
                char inputSymbol = production.charAt(0);
                char nextState = (production.length() == 1) ? 'f' : production.charAt(1);
                finiteAutomaton.addTransition(symbol, inputSymbol, nextState);
                finiteAutomaton.getAlphabet().add(inputSymbol); // Add all symbols to alphabet
            }
        }

        finiteAutomaton.setInitialState('S');
        finiteAutomaton.setFinalStates(getFinalStates());

        return finiteAutomaton;
    }

    private Set<Character> getFinalStates() {
        Set<Character> finalStates = new HashSet<>();
        for (char symbol : VN) {
            for (String production : P.get(symbol)) {
                if (production.length() == 1) {
                    finalStates.add(production.charAt(0));
                }
            }
        }
        return finalStates;
    }
}