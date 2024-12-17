### Hexlet tests and linter status:
[![Actions Status](https://github.com/putilovms/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/putilovms/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/64ec9061d66fe2e1241b/maintainability)](https://codeclimate.com/github/putilovms/python-project-49/maintainability)

# Brain games
*Educational project*

A set of 5 arithmetic console mini-games. To win, you need to answer the question correctly three times in a row.

## Installation
1. Requires Python version 3.10 or higher and Poetry
2. Clone the project: `>> git clone https://github.com/putilovms/brain-games.git`
3. Install the project: `>> make install`
4. Build the project: `>> make build`
5. Install the package: `>> make package-install`
6. To launch games:
   1. Run game Even: `>> brain-even`
   2. Run game Calc: `>> brain-calc`
   3. Run game GCD: `>> brain-gcd`
   4. Run game Progression: `>> brain-progression`
   5. Run game Prime: `>> brain-prime`

## Docker
1. Create an image: `>> docker build . -t brain-games`
2. Run the container in the background: `>> docker run --name brain-games -itd --rm brain-games`
3. Connect to a container: `>> docker exec -it brain-games bash`

## Examples of games
### Gameplay game Even
*Answer the question, is the number even?*
[![asciicast](https://asciinema.org/a/UFMh51rbmmqEVdHev0iHE8yib.svg)](https://asciinema.org/a/UFMh51rbmmqEVdHev0iHE8yib)

### Gameplay game Calc
*Write down the result of the calculations*
[![asciicast](https://asciinema.org/a/647108.svg)](https://asciinema.org/a/647108)

### Gameplay game GCD
*Write down the greatest common divisor*
[![asciicast](https://asciinema.org/a/YefknwQq74p6AcJK0XJ5htIQL.svg)](https://asciinema.org/a/YefknwQq74p6AcJK0XJ5htIQL)

### Gameplay game Progression
*Complete the sequence of numbers*
[![asciicast](https://asciinema.org/a/MBaPEbUaemLbpBJwJqde3w9jc.svg)](https://asciinema.org/a/MBaPEbUaemLbpBJwJqde3w9jc)

### Gameplay game Prime
*Guess if the number is prime?*
[![asciicast](https://asciinema.org/a/647353.svg)](https://asciinema.org/a/647353)
