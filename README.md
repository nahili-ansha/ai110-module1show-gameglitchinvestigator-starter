# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Game Purpose:**
A number guessing game where the player tries to guess a secret number within a limited number of attempts. The app gives hints after each guess to guide the player higher or lower depending on the difficulty setting.

**Bugs Found:**

1. **Wrong hint direction** — `check_guess` had the messages swapped: when the guess was too high it said "Go HIGHER!" and when too low it said "Go LOWER!". Test case: secret=97, guess=51 incorrectly told the player to guess lower.
2. **String vs. integer comparison** — On every even-numbered attempt, the secret was converted to a string before being passed to `check_guess`. This caused lexicographic comparison (e.g. `"51" > "97"` is `False`) instead of numeric comparison
3. **Attempts counter started at 1** — `session_state.attempts` was initialized to `1` instead of `0` and the attempt counter displayed incorrectly from the start.
4. **Hard difficulty range was easier than Normal** — Hard returned `1–50` while Normal returned `1–100`, making Hard objectively easier. The info message also hardcoded "between 1 and 100" regardless of difficulty.

**Fixes Applied:**

1. Corrected the hint messages in `check_guess`: `guess > secret` → "Go LOWER!", `guess < secret` → "Go HIGHER!".
2. Removed the string conversion of the secret — always pass the integer to `check_guess`.
3. Changed `session_state.attempts` initialization from `1` to `0`.
4. Changed Hard difficulty range to `1–200` and updated the info message to use `{low}` and `{high}` dynamically.
5. Moved `check_guess` into `logic_utils.py` and updated `app.py` to import it from there.
6. Added regression tests in `tests/test_game_logic.py` covering all fixed bugs, and fixed existing tests that were asserting against a string instead of unpacking the returned tuple.

## 📸 Demo

 ![Fixed winning game](images/Screenshot.jpg) 

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
