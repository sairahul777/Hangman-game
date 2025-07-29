# 🔤 Hangman Game (Python)

A fun and interactive **Hangman Game** built using Python. Guess the hidden word one letter at a time — but be careful, you only get 6 lives!

---

## 🎮 Game Overview

- Randomly selects a word from a large vocabulary list
- Player has 6 lives to guess the word correctly
- ASCII art stages of the hangman as you lose lives
- Tracks correct and repeated guesses
- Ends with a win or a loss when lives run out

---

## 🧪 Example Gameplay

Guess a letter: a


You guessed 'a', that's not in the word. You lose a life.

<pre>
  +---+
  |   |
      |
      |
      |
      |
=========

******************* 6/6 LIVES LEFT **********************


</pre>
Guess a letter: e
You guessed correctly!

...


---

## 🧠 Concepts Used

- `random.choice()` to select a word
- Loops and conditional logic (`while`, `if`, `else`)
- ASCII art for hangman stages
- User input handling and validation
- String operations and lists

---

## 📁 File

- `hangman_game.py` — Main Python file containing the game code

---

## 🛠️ How to Run

1. Make sure Python is installed (recommended: Python 3.6+)
2. Clone this repository or download the script
3. Open terminal or command prompt and run:

```bash
python hangman_game.py


✅ Ideal For
Python beginners

Practicing loops and string logic

Understanding how to build text-based games

Fun terminal-based projects

💡 Bonus Ideas
Add difficulty levels (Easy/Medium/Hard)

Track and display incorrect guesses

Implement a high-score or leaderboard

Add word categories (animals, movies, etc.)
