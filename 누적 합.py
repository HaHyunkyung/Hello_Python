# -*- coding: utf-8 -*-
import sys
def build_cumulative_tree(elements):
    n = len(elements)
    tree_size = 2 ** ((n - 1).bit_length())
    tree = [0] * (2 * tree_size)

    for i in range(n):
        tree[tree_size + i] = elements[i]

    for i in range(tree_size - 1, 0, -1):
        tree[i] = tree[2 * i] + tree[2 * i + 1]

    return tree


def print_cumulative_tree(tree, tree_size):
    row_size = 1
    current_index = 1

    while current_index < tree_size:
        for i in range(row_size):
            print(tree[current_index], end=" ")
            current_index += 1

        print()
        row_size *= 2

N = int(input())
elements = list(map(int, input().split()))

cumulative_tree = build_cumulative_tree(elements)

print_cumulative_tree(cumulative_tree, len(cumulative_tree))
