# Daniel Durbailo LAB 5 LFA
# The implementation of the logic

from Grammar import GenericGrammar
import unittest

class BreakFromLoops(Exception):
    pass

class Grammar(GenericGrammar):
    def cfg_to_cnf(self):
        self._start_symbol_rhs_removal()
        self._remove_null_productions()
        self._remove_unit_productions()
        self._remove_inaccessible_symbols()
        self._replace_terminals_with_nonterminals()
        self._reduce_production_length()
    def _start_symbol_rhs_removal(self):
        try:
            for value in self.P.values():
                for production in value:
                    for character in production:
                        if character == self.S:
                            raise BreakFromLoops
        except:
            new_P = {'X': [self.S]}
            new_P.update(self.P)
            self.P = new_P
            self.S = 'X'
            self.Vn.append(self.S)

    def _create_new_productions(self, production, character):
        results = []
        for i in range(len(production)):
            if production[i] == character:
                new_production = production[:i] + production[i+1:]
                results.append(new_production)
        return results

    def _remove_null_productions(self):
        count_null = 0
        null_prods = []
        for key, value in self.P.items():
            for production in value:
                if production == 'ε':
                    count_null += 1
                    null_prods.append(key)
                    value.remove(production)
        for i in range(count_null):
            new_P = self.P
            for key, value in self.P.items():
                for production in value:
                    for character in production:
                        if character == null_prods[i]:
                            new_productions = self._create_new_productions(production, null_prods[i])
                            for j in new_productions:
                                if j not in new_P[key]:
                                    new_P[key].append(j)
                            break
            self.P = new_P

    def _remove_unit_productions(self):
        for key, value in self.P.items():
            for production in value:
                if key == production:
                    self.P[key].remove(production)
        changes = True
        while changes:
            changes = False
            for key, value in self.P.items():
                for production in value:
                    if production in self.Vn:
                        changes = True
                        self.P[key].remove(production)
                        for prod in self.P[production]:
                            if prod not in self.P[key]:
                                self.P[key].append(prod)

    def _remove_inaccessible_symbols(self):
        accessible = set([self.S])
        queue = [self.S]

        while queue:
            current = queue.pop(0)
            for production in self.P.get(current, []):
                for symbol in production:
                    if symbol in self.Vn and symbol not in accessible:
                        accessible.add(symbol)
                        queue.append(symbol)

        self.Vn = [nt for nt in self.Vn if nt in accessible]
        for nt in list(self.P.keys()):
            if nt not in accessible:
                del self.P[nt]


    def _replace_terminals_with_nonterminals(self):
        def new_nonterminal(existing):
            for char in (chr(i) for i in range(65, 91)):
                if char not in existing:
                    return char
            raise ValueError("Ran out of single-letter nonterminal symbols!")

        terminal_to_nonterminal = {}
        new_P = {}
        for key, productions in self.P.items():
            new_productions = []
            for prod in productions:
                if len(prod) > 1:
                    new_prod = ''
                    for char in prod:
                        if char in self.Vt:
                            if char not in terminal_to_nonterminal:
                                new_nt = new_nonterminal(self.Vn)
                                self.Vn.append(new_nt)
                                terminal_to_nonterminal[char] = new_nt
                                new_P[new_nt] = [char]
                            new_prod += terminal_to_nonterminal[char]
                        else:
                            new_prod += char
                    new_productions.append(new_prod)
                else:
                    new_productions.append(prod)
            new_P[key] = new_productions
        self.P.update(new_P)

    def _reduce_production_length(self):
        def new_nonterminal(existing):
            for char in (chr(i) for i in range(65, 91)):
                if char not in existing:
                    return char
            raise ValueError("Ran out of single-letter nonterminal symbols!")

        existing_binaries = {}
        new_productions_dict = {}
        for key, productions in list(self.P.items()):
            new_productions = []
            for production in productions:
                if len(production) > 2:
                    while len(production) > 2:
                        last_two = production[-2:]
                        if last_two not in existing_binaries:
                            new_nt = new_nonterminal(set(self.Vn) | set(new_productions_dict.keys()))
                            self.Vn.append(new_nt)
                            new_productions_dict[new_nt] = [last_two]
                            existing_binaries[last_two] = new_nt
                        production = production[:-2] + existing_binaries[last_two]
                    new_productions.append(production)
                else:
                    new_productions.append(production)
            self.P[key] = new_productions
        self.P.update(new_productions_dict)


class TestGrammarMethods(unittest.TestCase):
    def setUp(self):
        self.grammar = Grammar(['S', 'A', 'B', 'C', 'D'], ['a', 'b'], {
            'S': ['bA', 'BC'],
            'A': ['a', 'aS', 'bAaAb'],
            'B': ['A', 'bS', 'aAa'],
            'C': ['ε', 'AB'],
            'D': ['AB']
        }, 'S')

    def test_start_symbol_rhs_removal(self):
        self.grammar._start_symbol_rhs_removal()
        for prod in self.grammar.P.values():
            self.assertNotIn(self.grammar.S, prod)

    def test_remove_null_productions(self):
        self.grammar._remove_null_productions()
        for prods in self.grammar.P.values():
            self.assertNotIn('ε', prods)

    def test_remove_unit_productions(self):
        self.grammar._remove_unit_productions()
        for key, prods in self.grammar.P.items():
            for prod in prods:
                self.assertFalse(len(prod) == 1 and prod.isupper())

    def test_remove_inaccessible_symbols(self):
        self.grammar.Vn.append('Z')
        self.grammar._remove_inaccessible_symbols()
        self.assertNotIn('Z', self.grammar.Vn)

    def test_replace_terminals_with_nonterminals(self):
        self.grammar._replace_terminals_with_nonterminals()
        for prods in self.grammar.P.values():
            for prod in prods:
                if len(prod) > 1:
                    self.assertTrue(all(char in self.grammar.Vn for char in prod))

    def test_reduce_production_length(self):
        self.grammar._replace_terminals_with_nonterminals()
        self.grammar._reduce_production_length()
        for prods in self.grammar.P.values():
            for prod in prods:
                self.assertTrue(len(prod) <= 2)

    def test_grammar_print(self):
        self.grammar.cfg_to_cnf()
        self.grammar.print_grammar()

if __name__ == '__main__':
    unittest.main()
