import nltk
from nltk.tree import Tree

sentence = "The cat is sitting on the mat."
parse_tree_string = "(S (NP (Det The) (N cat)) (VP (V is) (VP (V sitting) (PP (P on) (NP (Det the) (N mat))))))"
parse_tree = Tree.fromstring(parse_tree_string)
parse_tree.pretty_print()
print("Name:KailashBadu\nRollNo:-09")
