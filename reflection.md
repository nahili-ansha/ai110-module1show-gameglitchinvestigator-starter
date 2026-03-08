# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? 

The user interface looks good, it displays "Game Glitch Investigator". It has different sections as Make a guess, Submit Guess, New Game, and Show hint. Once I enter a guess and click on submit guess it displays the hint as go lower or go higher.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards"). 
  
  The first bug is that the hints were backwards. For example: The secret was 97, I entered 51 then it said Guess Lower, which is not true. The second bug is that the difficulty range is wrong, if difficulty == "Hard" it says 1-50 and the "normal" is 1-100, hard should be bigger. The third bug is that Attempts counter starts at 1 instead of 0, meaning that when I attempt the first time the number doesn't change to 1 it will stay the same and then the next time I guess the number will change to one.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 

  "The messages in check_guess are also swapped — "Go HIGHER!" when the   
  guess is too high (should say "Go LOWER"), and vice versa." I verified by swapping the guess logic using if conditions and tested it playing the game.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  When I asked the AI to identify bugs in the guessing game, it initially
  described the check_guess feedback messages as correct and focused on
  the string vs. integer comparison as the sole cause of the wrong hint. 
  However, when I tested the fixed app, guessing 51 with a secret of 97  
  still gave the wrong direction "Go HIGHER!" and "Go     
  LOWER!" were swapped in the logic regardless of the type bug. The AI   
  had missed that guess > secret was returning "Go HIGHER!" when it   
  should say "Go LOWER!". I verified it by running the app manually and  
  tracing through the check_guess function line by line, confirming the text pointed the wrong way.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?  

  I decided a bug was fixed by re-running the app manually and confirming the behavior for example, entering 51 with secret 97 and verifying the hint now correctly said "Go Higher."  

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code. 
  
  I ran the pytest using python -m pytest tests/test_game_logic.py. One test test_high_guess_gives_lower_hint, used the exact case (guess=51, secret=97) and confirmed the outcome was "Too Low" with a "GO HIGHER" message. All 6 tests passed.

- Did AI help you design or understand any tests? How?  

  Yes the AI helped me to generate and understand the tests. It caught that the existing tests were broken asserting against a string when check_guess actually returns a tuple, which I wouldn't have noticed until the tests failed.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? 
  
  Every time you click a button, Streamlit reruns the whole script from  
  scratch like a page refresh. session_state is a dictionary that 
  survives those reruns, so things like your score and secret number don't reset on every click.  

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git. 

  Writing tests that reproduce the exact bug case before marking a fix as done like using guess=51, secret=97 to pin the specific failure. 

- What is one thing you would do differently next time you work with AI on a coding task? 

Test AI suggestions manually before trusting them. The AI missed the swapped hint messages on the first pass, and I only caught it by actually running the app.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

AI-generated code can look completely reasonable and still have subtle logic bugs. I now treat it as a first draft that needs verification, not a finished solution.
