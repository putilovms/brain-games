#!/usr/bin/env python3
from brain_games import controller
from brain_games.games import gcd


def main():
    controller.play(gcd)


if __name__ == '__main__':
    main()
