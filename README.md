# ❌⭕ Tic-Tac-Toe (XOX) in Python

A clean, interactive Command-Line Interface (CLI) implementation of the classic **Tic-Tac-Toe** game written in Python. Play either against a computer opponent or challenge a friend locally.

---

## 📌 Features

* **Two Game Modes:**
  * **Player vs. Computer:** Play against an automated computer opponent.
  * **Player vs. Player:** Play locally with two players taking turns on the same screen.
* **Cartesian Grid Layout:** Custom coordinate system starting from `(0,0)` at the bottom-left corner.
* **Color-Coded Board:** Colorized row and column indices for enhanced terminal visibility.
* **Automatic Game Logic:** Real-time checking for horizontal, vertical, and diagonal win patterns, as well as draw detection.

---

## 🎮 How Coordinates Work

The board uses a standard 3x3 coordinate plane where **(0, 0)** is at the **bottom-left**:

```text
  ＿＿＿＿＿＿＿＿
2 │   │   │   │
  ─────────────
1 │   │   │   │
  ─────────────
0 │   │   │   │
  ─────────────
    0   1   2

When prompted, enter your move by typing the X (column) and Y (row) coordinates separated by a space:
Example: 1 1 places your marker in the exact center of the board.

---

How to Run

TicTacToe.py
