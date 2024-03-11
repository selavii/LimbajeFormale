package LAB2;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Grammar grammar = new Grammar();
        FiniteAutomaton finiteAutomaton = grammar.convertToFiniteAutomaton();

        // Display generated strings
        System.out.println("Generated Strings:");
        for (String str : grammar.generateStrings(5)) {
            System.out.println(str);
        }

        // Display finite automaton
        System.out.println("Finite Automaton:");
        System.out.println(finiteAutomaton);

        // Check if input string can be reached by finite automaton
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter input string: ");
        String inputString = scanner.nextLine();
        boolean canReach = finiteAutomaton.canReachString(inputString);
        if (canReach) {
            System.out.println("Input string can be obtained via state transitions.");
        } else {
            System.out.println("Input string cannot be obtained via state transitions.");
        }

        // Classify the grammar and display its type
        String grammarType = grammar.classify();
        System.out.println("Grammar type: " + grammarType);

        scanner.close();
    }
}
