from itertools import permutations
def solve_cryptoarithmetic(w1, w2, w3):
    letters = set(w1 + w2 + w3)
    if len(letters) > 10:
        print("Something is wrong with the input")
        return
    letters = list(letters)
    l4 = len(letters)
    values = [0] * l4
    def pos(x):
        return letters.index(x)
    def add(s):
        nonlocal l4
        for c in s:
            if c not in letters:
                letters.append(c)
                l4 += 1
    add(w1)
    add(w2)
    add(w3)
    tries = list(permutations(range(10), l4))
    for values in tries:
        if values[pos(w1[0])] == 0 or values[pos(w2[0])] == 0 or values[pos(w3[0])] == 0:
            continue
        n1 = int(''.join(str(values[pos(c)]) for c in w1))
        n2 = int(''.join(str(values[pos(c)]) for c in w2))
        n3 = int(''.join(str(values[pos(c)]) for c in w3))
        if n1 + n2 == n3:
            print("\n\nSolution found:")
            for i, c in enumerate(letters):
                print(f"{c} = {values[i]}")
            return
    print("\n\nNo solution found")
w1 = input("Enter the first word: ")
w2 = input("Enter the second word: ")
w3 = input("Enter the sum word: ")
solve_cryptoarithmetic(w1, w2, w3)
print("Name:KailashBadu\nRollNo:-09")
