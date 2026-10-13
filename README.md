# Asteroids

A space survival game built with Python and Pygame as part of the Boot.dev course. You control a rocket, dodge incoming asteroids, and shoot them to earn points. The goal is to survive as long as possible and get a high score.

## How to play

You start with three lives and the Speed Shot weapon. Asteroids enter from the edges of the screen. Shooting a large asteroid breaks it into two smaller, faster pieces. The smallest asteroids disappear when hit.

Each asteroid you hit gives you one point, including the smaller pieces. Colliding with an asteroid costs a life, with a three-second cooldown between losing lives. When you run out of lives, the game shows your final score and closes after five seconds.

Your rocket wraps around the screen: flying off one edge brings you back on the opposite side.

## Controls

| Key | Action |
| --- | --- |
| **W** | Move forward |
| **S** | Move backward |
| **A** | Turn left |
| **D** | Turn right |
| **Space** | Shoot (hold to keep firing) |
| **R** | Switch to a random different weapon |

Close the game window to quit. To play again after game over, run the game again.

## Weapons

All five weapons are available from the start. The selected weapon appears below your score.

| Weapon | What it does |
| --- | --- |
| Starter Gun | Fires one shot at a time |
| Triple Shot | Fires three shots in a small spread |
| Rapid Shot | Fires more often than the Starter Gun |
| Pierce Gun | Fires shots that keep moving after hitting an asteroid |
| Speed Shot | Fires faster-moving shots |

## Setup and running

You need **Python 3.13 or newer**. The game uses **Pygame 2.6.1** and needs a desktop environment to display its window.

Open a terminal in this project's folder. If you have `uv` installed, run:

```sh
uv sync
uv run main.py
```

You can also use Python's built-in virtual environment tools.

**macOS or Linux:**

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pygame==2.6.1
python main.py
```

**Windows PowerShell:**

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pygame==2.6.1
python main.py
```

Run these commands from the project folder so the game can find its images. Keep the image files and the `explosion` folder in their original locations.

## How the code is organised

| File | Purpose |
| --- | --- |
| `main.py` | Runs the game loop, checks collisions, and displays lives and score |
| `player.py` | Handles the rocket's movement, lives, score, and weapon selection |
| `weapon.py` | Controls firing speed, shot direction, and weapon behaviour |
| `shot.py` | Moves and draws bullets |
| `asteroid.py` | Moves, draws, and splits asteroids |
| `asteroidfield.py` | Creates asteroids at random screen edges |
| `circleshape.py` | Provides shared position, movement, and collision code |
| `explosion.py` | Plays explosion animations |
| `constants.py` | Stores settings such as screen size and movement speed |
| `logger.py` | Records game state and events for debugging |

To experiment with the game, try changing values in `constants.py`, such as the asteroid spawn rate or the rocket's turn speed.
