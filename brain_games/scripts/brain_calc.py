#!/usr/bin/env python3
from brain_games import controller
from brain_games.games import calc


def main():
    controller.play(calc)


if __name__ == '__main__':
    main()
