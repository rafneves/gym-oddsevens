# Odds and Evens OpenAI Environment

`gym_oddsevens` is a gym environment that implements some versions of the Odds and Evens game.

## Motivation ("When DRL meets Nash")

The Odds and Evens is a simple simultaneous game, where we can test the DRL solutions to what is expected according the game theory. 
The game has a simple analysis and clear results in a game theory concepts (mixed-strategy Nash Equibriums). That way we compare if the agent learn what is expected by game structure analysis.

In that implementation the `Agent` plays against the `Environment`, and to make the comparasion easier there are three versions of the game depending on how smart or adaptative the `Environment` is.

## Implementation

The `Agent` and the `Environment` play Odds and Evens. In all versions the game:

1. Starts with the `Environment` choosing what kind of result (odds or evens) will won the match, and sending a message containing two numbers to the `Agent`. 
2. Based on that, the `Agent` replies the `Environment` with a message containing a single number (0 if the `Agent` plays evens, 1 if `Agent` plays odds).
3. The `Environment`:

    3.1. Chooses a number (0 if the `Environment` plays evens, 1 if `Environment` plays odds). Of course, without taking in account what the `Agent` sent to him.
  
    3.2 Sum the two values and check if matches what the `Environment` chosed in (1).

    3.3. If it matches the `Environment` wins and *reward* the `Agent` with -1. Otherwise, the `Agent` wins and receives 1.

The game continues until `done` (that is set by the `Environment`) is equal to `FALSE`.

## Game Versions

### OddsEvens-v0

This version implements a `Environment` that plays odds with a fixed probability, regardless what the `Agent` did in the last matches.

### OddsEvensAdversarial-v0

This version implements a `Environment` that plays odds with an adaptive probability, based on previous matches in the same `episode`.
The `Environment` uses a hard (discontinuous) rule:

1. The `Environment` calculates the proportion of Evens played by the `Agent` based on the past matches within an `episode`. 
2. Guess that the `Agent` will play Evens if the result is $>0.5$. And guess that the `Agent` will play Odds otherwise.
3. Plays according with these guess.

When you call `reset()` the `Environment` clean its memory.

### OddsEvensAdversarial-v1

This version implements a `Environment` that plays odds with an adaptive probability, based on previous matches in the same `episode`.
The `Environment` uses a soft rule:

1. The `Environment` calculates the proportion of Evens played by the `Agent` based on the past matches within an `episode`. 
2. To make the guess, it sample from a Bernoulli distribution using as the probability the average calculated in the previous step.
3. Plays according with these guess.

When you call `reset()` the `Environment` clean its memory.


## Installation
You will need an Anaconda to fully test the notebooks.

Do:
```
conda create --name drl_oddsevens
conda source activate drl_oddsevens
python3 -m pip install jupyter tensorflow==2.1.0
python3 -m pip install -e .
```

## Test
To test the environment:

1. Inside `drl_oddsevens` environment start your notebook:
```
python3 notebok
```

2. Go to your broswer, enter in Jupyter Notebook, find and run `/examples/lecture_policygradients.ipynb`.
