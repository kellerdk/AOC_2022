#!/usr/bin/env python3

""" AOC 2022 - Day 5
"""

import re

number = re.compile(r"\d+")
chars = re.compile(r"([A-Z]+)(\d+)")


def get_data(fname):
    """Get data from input file
    """
    with open(fname, encoding="utf-8") as fptr:
        return fptr.read().split("\n")[:-1]

def parse(xss):
    """parent config parser
    """
    init, instructions = xss[:9], xss[9:]
    return parse_state(init), parse_moves(instructions)


def parse_moves(xss):
    """Parse move list
    """
    return [k for k in [[int(j) for j in number.findall(i)] for i in xss] if k]


def parse_state(xss):
    """Parse initial state of crates from input
    """
    state = ["".join(i) for i in list(zip(*xss))]
    xxs = [chars.search(i).groups() for i in state if chars.search(i)]
    return {int(k): list(v) for v, k in xxs}


def move_crates(instate):
    """Move crates one at a time. FIFO semantics
    """
    state, moves = parse(instate)
    for qty, src, dst in moves:
        while qty > 0:
            state[dst] = list(state[src].pop(0)) + state[dst]
            qty -= 1
    return state


def move_stack(instate):
    """Move crates by stack of crates in one move. FILO semantics
    """
    state, moves = parse(instate)
    for qty, src, dst in moves:
        state[dst] = state[src][:qty] + state[dst]
        state[src] = state[src][qty:]
    return state


def report_state(state):
    """Report the final string state of the crates
    """
    return "".join(v[0] for v in state.values())


if __name__ == "__main__":
    directions = get_data("input/day5_input.txt")
    for apply in [move_crates, move_stack]:
        print(f"{apply.__name__}:", report_state(apply(directions)))
