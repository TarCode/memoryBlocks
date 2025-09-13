# Memory Puzzle Game

A classic memory matching game built with Pygame.

## What it is

- Click boxes to reveal hidden icons underneath
- Find matching pairs of shapes and colors
- Complete the board by finding all pairs

## How to Play

1. Click a box to reveal its icon
2. Click another box to reveal its icon
3. If they match, they stay revealed
4. If they don't match, they cover back up
5. Remember where icons are located
6. Match all pairs to win and start a new round

## Controls

- **Mouse** - Click boxes to reveal them
- **ESC** - Quit game

## Requirements

- Python 3.x
- Pygame (`pip install pygame`)

## How to Run

```bash
python memoryPuzzle.py
```

## Features

- 8x8 grid (64 boxes, 32 pairs)
- 5 different shapes: donut, square, diamond, lines, oval
- 7 different colors
- Smooth reveal/cover animations
- Victory animation with flashing background
- Auto-restart after winning
