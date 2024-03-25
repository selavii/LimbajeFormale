import re
from prettytable import PrettyTable

# Define the token types
TOKEN_TYPES = {
    "OPEN_TAG": r"<[a-zA-Z][^\s>]*",
    "CLOSE_TAG": r"</[a-zA-Z][^\s>]*>",
    "ATTRIBUTE": r"[a-zA-Z\-]+=\"[^\"]*\"",
    "TEXT": r"[^\s<]+",
    "WHITESPACE": r"\s+"
}

# Compile regex patterns for each token type
TOKEN_REGEX = {token_type: re.compile(pattern) for token_type, pattern in TOKEN_TYPES.items()}


def tokenize_html(html):
    tokens = []
    while html:
        match = None
        for token_type, regex in TOKEN_REGEX.items():
            match = regex.match(html)
            if match:
                value = match.group(0)
                tokens.append((token_type, value))
                html = html[len(value):]
                break
        if not match:
            raise ValueError("Invalid HTML syntax")
    return tokens


def main():
    html_code = '''
    <html>
        <head>
            <title>Hello, World!</title>
        </head>
        <body>
            <h1>Welcome to My Website</h1>
            <p>This is a paragraph.</p>
        </body>
    </html>
    '''
    tokens = tokenize_html(html_code)

    table = PrettyTable(['Token Type', 'Value'])
    for token in tokens:
        table.add_row(token)

    print(table)


if __name__ == "__main__":
    main()
