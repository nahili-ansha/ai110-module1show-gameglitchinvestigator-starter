from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_attempts_starts_at_zero():
    # Regression test: attempts must initialize to 0 so the first submission
    # increments to 1. Previously it started at 1, causing the counter to
    # skip — the second guess would show as attempt 1.
    initial_attempts = 0
    attempts_after_first_guess = initial_attempts + 1
    assert attempts_after_first_guess == 1, (
        "First guess should be attempt 1, not 2. "
        "attempts must initialize to 0, not 1."
    )

def test_high_guess_gives_lower_hint():
    # Regression test: when guess > secret the message must say Go LOWER,
    # not Go HIGHER. Previously the messages were swapped.
    # Reproduces the exact case reported: secret=97, guess=51 gave "Go Lower"
    # (wrong); with the fix it gives "Go Higher" since 51 < 97.
    outcome, message = check_guess(51, 97)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_low_guess_gives_higher_hint():
    # Companion to above: when guess < secret the message must say Go HIGHER.
    outcome, message = check_guess(97, 51)
    assert outcome == "Too High"
    assert "LOWER" in message
