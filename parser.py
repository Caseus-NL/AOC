import re
from time import perf_counter

# Over het algemeen bestaan input-bestanden uit AOC uit verschillende rijen of kolommen.
# Soms is een rij vervolgens verdeeld in getallen of zijn elementen gescheiden met spaties.
# Over het algemeen komt het inlezen van puzzelbestanden dus neer op het inlezen van regels, en daarna nodige conversies uitvoeren.
# Eerst defineer ik een functie die regels los inleest:

def lines(input : str): return input.splitlines()

# Hieronder defineer ik bepaalde structuren die elke regel kan hebben
def split_numbers(line : str) : return [int(element) for element in re.findall(r'\d+', line)]
def split_whitespace(line : str) : return line.split()

def parse(input : str, structure_type : callable, split_method : callable):
    return [split_method(segment) for segment in structure_type(input)]

def T(input : list):
    ### Transposeren van de lijst, dus rij i, kolom j wordt rij j, kolom i
    return [[input[i][j] for i in range(len(input))] for j in range(len(input[0]))]


def run(func : callable, input):
    t_0 = perf_counter()
    result = func(input)
    t_1 = perf_counter()
    print(f"Result: {result} in {1000*(t_1 - t_0) : .5f} ms.")
    return result

def test(func: callable, input, output):
    res = run(func, input)
    assert res == output, f"Result was {res}, but {output} was expected."