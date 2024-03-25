import re
from prettytable import PrettyTable

# Define the token types and their corresponding regex patterns
TOKEN_TYPES = [
    ('NUMBER', r'\b\d+(\.\d*)?([eE][+-]?\d+)?\b'),
    ('KEYWORD', r'\b(abstract|continue|for|new|switch|assert|default|goto|package|synchronized|boolean|do|if|private|this|break|double|implements|protected|throw|byte|else|import|public|throws|case|enum|instanceof|return|transient|catch|extends|int|short|try|char|final|interface|static|void|class|finally|long|strictfp|volatile|const|float|native|super|while)\b'),
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),
    ('LEFT_PAREN', r'\('),
    ('RIGHT_PAREN', r'\)'),
    ('LEFT_SQUARE', r'\['),
    ('RIGHT_SQUARE', r'\]'),
    ('LEFT_CURLY', r'\{'),
    ('RIGHT_CURLY', r'\}'),
    ('LESS_THAN', r'<'),
    ('GREATER_THAN', r'>'),
    ('EQUAL', r'='),
    ('DOUBLE_EQUAL', r'=='),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('ASTERISK', r'\*'),
    ('SLASH', r'/'),
    ('HASH', r'#'),
    ('DOT', r'\.'),
    ('COMMA', r','),
    ('COLON', r':'),
    ('SEMICOLON', r';'),
    ('SINGLE_QUOTE', r'\''),
    ('DOUBLE_QUOTE', r'"'),
    ('COMMENT', r'\/\/.*|\/\*(.|\n)*?\*\/'),
    ('PIPE', r'\|'),
    ('END', r'\0'),
    ('UNEXPECTED', r'.')
]


def tokenize(code):
    tokens = []
    while code:
        code = code.strip()
        for token_type, pattern in TOKEN_TYPES:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                value = match.group(0)
                tokens.append((token_type, value))
                code = code[len(value):]
                break
        else:
            raise SyntaxError(f'Illegal character: {code[0]}')
    return tokens


java_code = """
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        System.out.println("You entered: " + number);
    }
}
"""

tokens = tokenize(java_code)

pt = PrettyTable()
pt.field_names = ["Token Type", "Token Value"]

for token in tokens:
    pt.add_row([token[0], token[1]])

print(pt)
