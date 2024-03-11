package LAB2;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Grammar {
    Map<String, List<String>> language;

    public Grammar(Map<String, List<String>> language) {
        this.language = language;
    }

    public String classifyGrammar() {
        if (isType0()) {
            return "Type 0 (Unrestricted)";
        } else if (isType1()) {
            return "Type 1 (Context-Sensitive)";
        } else if (isType2()) {
            return "Type 2 (Context-Free)";
        } else if (isType3()) {
            return "Type 3 (Regular)";
        } else {
            return "Unknown Type";
        }
    }

    private boolean isType0() {
        // Type 0 grammars are always unrestricted
        return true;
    }

    private boolean isType1() {
        // Check if any rule violates the context-sensitive condition
        for (String variable : language.keySet()) {
            for (String production : language.get(variable)) {
                if (!production.matches(".*[A-Z].*->[A-Za-z]*[A-Z][A-Za-z]*.*")) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean isType2() {
        // Check if all productions are of the form A -> w where A is a single variable
        for (String variable : language.keySet()) {
            for (String production : language.get(variable)) {
                if (!production.matches("[A-Z]->[a-zA-Z]*")) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean isType3() {
        // Check if all productions are of the form A -> aB or A -> a where A and B are variables and a is a terminal
        for (String variable : language.keySet()) {
            for (String production : language.get(variable)) {
                if (!production.matches("[A-Z]->[a-z][A-Z]?")) {
                    return false;
                }
            }
        }
        return true;
    }
}

