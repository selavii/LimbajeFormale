package LAB2;


import java.util.List;
import java.util.Map;

public class Grammar {
    Map<String, List<String>> language;

    public Grammar(Map<String, List<String>> language) {
        this.language = language;
    }

    public String classifyGrammar() {
        boolean isRegular = true;
        boolean isContextFree = true;
        boolean isContextSensitive = true;

        for (String variable : language.keySet()) {
            for (String production : language.get(variable)) {
                if (!(production.length() == 1 && production.matches("[a-d]")) &&
                        !(production.length() == 2 && (
                                (Character.isLowerCase(production.charAt(0)) && Character.isUpperCase(production.charAt(1))) ||
                                        (Character.isUpperCase(production.charAt(0)) && Character.isLowerCase(production.charAt(1)))))) {
                    isRegular = false;
                }
                if (!Character.isUpperCase(variable.charAt(0))) {
                    isContextFree = false;
                }
                if (production.length() < variable.length()) {
                    isContextSensitive = false;
                }
            }
        }

        if (isRegular) {
            return "Type 3 (Regular)";
        } else if (isContextFree) {
            return "Type 2 (Context-Free)";
        } else if (isContextSensitive) {
            return "Type 1 (Context-Sensitive)";
        } else {
            return "Type 0 (Recursively enumerable)";
        }
    }
}
