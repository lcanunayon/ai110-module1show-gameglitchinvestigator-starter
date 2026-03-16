from app import check_guess as app_check_guess, attempt_limit_map


# --- Bug fix regression tests ---

def test_hint_message_go_lower_when_too_high():
    # Bug: hint said "Go HIGHER" when guess was above secret — should say "Go LOWER"
    outcome, message = app_check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'Go LOWER' hint but got: {message}"

def test_hint_message_go_higher_when_too_low():
    # Bug: hint said "Go LOWER" when guess was below secret — should say "Go HIGHER"
    outcome, message = app_check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'Go HIGHER' hint but got: {message}"

def test_easy_has_most_attempts():
    # Bug: Easy had fewer attempts than Normal, making it not the easiest difficulty
    assert attempt_limit_map["Easy"] > attempt_limit_map["Normal"] > attempt_limit_map["Hard"]
