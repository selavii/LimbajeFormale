import re
import random

def generate_string_expression_1(limit=5):
    combinations = set()
    for i in range(limit + 1):
        for j in range(limit + 1):
            for k in range(limit + 1):
                for l in range(limit + 1):
                    for m in range(limit + 1):
                        text = ''
                        text += 'a' * i
                        text += 'b' * j
                        text += 'c' * k
                        text += 'd' * l
                        text += 'E' * m
                        text += 'G' if m > 0 else ''
                        combinations.add(text)
    return combinations

def generate_string_expression_2(limit=5):
    combinations = set()
    for i in range(limit + 1):
        for j in range(limit + 1):
            for k in range(limit + 1):
                for l in range(limit + 1):
                    text = ''
                    text += 'P'
                    text += 'Q' if i > 0 else ''
                    text += 'R' if j > 0 else ''
                    text += 'S' if k > 0 else ''
                    text += 'T'
                    text += 'U' * i
                    text += 'V' * i
                    text += 'W' * i
                    text += 'X' * i
                    text += 'Z' * j
                    combinations.add(text)
    return combinations

def generate_string_expression_3(limit=5):
    combinations = set()
    for i in range(limit + 1):
        for j in range(limit + 1):
            for k in range(limit + 1):
                for l in range(limit + 1):
                    for m in range(limit + 1):
                        text = ''
                        text += '1'
                        text += '0' * i
                        text += '1' * i
                        text += '2' * j
                        text += '3' * k
                        text += '4' * k
                        text += '5' if l > 0 else ''
                        text += '6'
                        combinations.add(text)
    return combinations

# Test with examples
print("Combinations for the first expression:")
print(random.sample(generate_string_expression_1(), 10))
print()

print("Combinations for the second expression:")
print(random.sample(generate_string_expression_2(), 10))
print()

print("Combinations for the third expression:")
print(random.sample(generate_string_expression_3(), 10))
