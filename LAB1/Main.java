package LAB1;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Grammar grammar = new Grammar();
        FiniteAutomaton finiteAutomaton = grammar.convertToFiniteAutomaton();
        System.out.println("Generated Strings:");
        for (String str : grammar.generateStrings(5)) {
            System.out.println(str);
        }
        System.out.println("Finite Automaton:");
        System.out.println(finiteAutomaton);


        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter input string: ");
        String inputString = scanner.nextLine();


        boolean canReach = finiteAutomaton.canReachString(inputString);
        if (canReach) {
            System.out.println("Input string can be obtained via state transitions.");
        } else {
            System.out.println("Input string cannot be obtained via state transitions.");
        }

        scanner.close();
    }
}
