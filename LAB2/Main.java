package LAB2;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        Map<String, List<String>> language = new HashMap<>();
        language.put("S", Arrays.asList("aB", "bB"));
        language.put("B", Collections.singletonList("cD"));
        language.put("D", Arrays.asList("dQ", "a"));
        language.put("Q", Arrays.asList("bB", "dQ"));

        Grammar grammar = new Grammar(language);
        System.out.println("Grammar is: " + grammar.classifyGrammar());
    }
}
