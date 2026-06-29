# Column Game

A Python implementation of the classic **Columns puzzle game** using **Pygame**. Players control falling columns consisting of three colored blocks and attempt to create matches of three or more blocks of the same color horizontally, vertically, or diagonally.

The project also includes an automated replay mode that reads moves from an input file and reproduces gameplay step by step.

---

## Features

* 🎮 Real-time gameplay using Pygame
* 🧩 Falling columns of three colored blocks
* ⬅️➡️ Horizontal movement
* 🔄 Column rotation
* ✨ Match detection in four directions:

  * Vertical
  * Horizontal
  * Diagonal (↘)
  * Diagonal (↗)
* ⬇️ Gravity simulation after blocks are removed
* 🏆 Score tracking
* 📄 Input-file-based replay mode

---

## Game Rules

1. A column containing three colored blocks falls from the top of the board.
2. The player can:

   * Move the column left
   * Move the column right
   * Rotate the order of colors
   * Drop the column faster
3. Whenever three or more blocks of the same color are aligned, they are removed.
4. After blocks are removed, the remaining blocks fall due to gravity.
5. The game continues until no more columns can be placed.

---

## Controls

| Key         | Action             |
| ----------- | ------------------ |
| Left Arrow  | Move left          |
| Right Arrow | Move right         |
| Space       | Rotate colors      |
| Down Arrow  | Accelerate falling |
| S           | Pause/Resume       |
| Q           | Quit               |
| Esc         | Quit               |

---

## Replay Mode

The repository includes a replay system that reads actions from an input file.

Example:

```text
CCH
Left
Left
Rotate
FREEZE
CGH
Right
FREEZE
CCA
FREEZE
```

Where:

* `CCH`, `CGH`, `CCA` represent newly generated columns
* `Left` moves the column left
* `Right` moves the column right
* `Rotate` changes the order of colors
* `FREEZE` drops and locks the column in place

This mode can be used for:

* Testing
* Demonstrations
* Automated gameplay reproduction
* Debugging

---

## Project Structure

```text
.
├── game.py
├── input.txt
└── README.md
```

---

## Requirements

* Python 3.x
* Pygame

Install dependencies:

```bash
pip install pygame
```

---

## Running the Game

### Interactive Mode

```bash
python game.py
```

### Replay Mode

```bash
python game.py
```

The program reads commands from `input.txt` and reproduces the game automatically.

---

## Implementation Details

The game is implemented using:

* Matrix-based board representation
* Collision detection
* Pattern matching algorithms
* Gravity simulation
* Event-driven programming with Pygame
* File-based action replay

---

## Educational Purpose

This project was developed as an educational exercise in:

* Python programming
* Object-oriented and event-driven design
* Matrix and grid manipulation
* Game logic implementation
* Algorithmic problem solving using Pygame

---

## Author

**Parham Hassan**
