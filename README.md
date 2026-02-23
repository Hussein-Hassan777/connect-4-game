# MiniMax Connect-4 (GUI)

A **Python-based Connect-4 game** with a graphical user interface (GUI) built using **Tkinter**. Features a **Human vs AI** mode powered by the **MiniMax algorithm** with intelligent move selection.

---

## Table of Contents

- Features
- Technology Stack
- Installation / Setup
- Usage
- How AI Works
- Contributing
- Author

---

## Features

- **Graphical User Interface** – Simple and interactive GUI using Tkinter.
- **Human vs AI Mode** – Play against an intelligent AI opponent.
- **MiniMax AI Algorithm** – AI makes strategic decisions using MiniMax with depth control.
- **Move Validation** – Prevents invalid moves and handles game-over conditions.
- **Endgame Alerts** – Shows win/draw messages using Tkinter message boxes.

---

## Technology Stack

- **Programming Language:** Python 3.6+
- **GUI Framework:** Tkinter
- **AI Algorithm:** MiniMax with optional depth pruning

---

## Installation / Setup

1. Clone the repository:

```
git clone https://github.com/Hussein-Hassan777/Connect-4-game.git
```

1. Navigate to the project folder:

```
cd Connect-4-game
```

1. Install dependencies (if not already installed):

```
pip install tk
```

> Tkinter usually comes pre-installed with Python on most systems.
> 

---

## Usage

Run the game using:

```
python connect4.py
```

- The GUI window will open.
- Players can click on columns to drop their piece.
- The AI will respond automatically.
- The game shows alerts when someone wins or if it’s a draw.

---

## How AI Works

- **MiniMax Algorithm:** Evaluates all possible moves to maximize the AI’s chance of winning while minimizing the player’s chance.
- **Depth Control:** Limits how many moves ahead the AI looks, balancing difficulty and performance.
- **Optimal Play:** Ensures AI chooses the best possible moves within its search depth.

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

---

## Author

**Hussein Hassan Hendawy** – Computer Science & AI | Benha University
