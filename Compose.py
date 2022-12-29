from Graph import Vertex, Graph
import os
import re
import string
import random

def get_words_from_text(text_path):
    with open(text_path, 'rb') as file:
        text = file.read().decode("utf-8") 

        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    words = words[:1000]

    return words

def make_graph(words):
    g = Graph() 
    prev_word = None
  
    for word in words:

        vertex = g.get_vertex(word)

        if prev_word:
            prev_word.add_edge_to(vertex)

        prev_word = vertex

    return g

def compose(graph, words, length=50):

    word = graph.get_vertex(random.choices(words)[0])
    composition = []
    
    for i in range(length):
        composition.append(word.value)
        word = graph.get_next_vertex(word)

    composition = ' '.join(composition)

    return composition

def main():
    words = get_words_from_text('hp_sorcerer_stone.txt')

    g = make_graph(words)

    print(compose(g,words))

main()





    
