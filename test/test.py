from src.scorecard import ScoreCard


def test_all_strikes():
    test_all_strikes = ScoreCard('XXXXXXXXXXXX')
    assert test_all_strikes.get_total_score() == 300

def test_random_score():
    test_random_score = ScoreCard('9-9-9-9-9-9-9-9-9-9-')
    assert test_random_score.get_total_score() == 90

    test_random_score = ScoreCard('9-3/613/815/-/8-7/8/8')
    assert test_random_score.get_total_score() == 131

    test_random_score = ScoreCard('X9-9-9-9-9-9-9-9-9-')
    assert test_random_score.get_total_score() == 100

def test_all_spares():
    test_all_spares = ScoreCard('5/5/5/5/5/5/5/5/5/5/5')
    assert test_all_spares.get_total_score() == 150

def test_two_extra_final_rolls():
    test_two_extra_final_rolls = ScoreCard('9-9-9-9-9-9-9-9-9-X9-')
    assert test_two_extra_final_rolls.get_total_score() == 100

    test_two_extra_final_rolls = ScoreCard('X9-X9-9-9-9-9-9-9-')
    assert test_two_extra_final_rolls.get_total_score() == 110

def test_two_strikes_in_a_row_is_a_double():
    test_two_strikes_in_a_row_is_a_double = ScoreCard('XX9-9-9-9-9-9-9-9-')
    assert test_two_strikes_in_a_row_is_a_double.get_total_score() == 120

def test_three_strikes_in_a_row_is_a_triple():
    test_three_strikes_in_a_row_is_a_triple = ScoreCard('XXX9-9-9-9-9-9-9-')
    assert test_three_strikes_in_a_row_is_a_triple.get_total_score() == 141

def test_two_strikes_in_extra_rolls():
    test_two_strikes_in_extra_rolls = ScoreCard('9-9-9-9-9-9-9-9-9-XXX')
    assert test_two_strikes_in_extra_rolls.get_total_score() == 111

def test_spare_in_extra_roll():
    test_spare_in_extra_roll = ScoreCard('8/549-XX5/53639/9/X')
    assert test_spare_in_extra_roll.get_total_score() == 149

    test_spare_in_extra_roll = ScoreCard('X5/X5/XX5/--5/X5/')
    assert test_spare_in_extra_roll.get_total_score() == 175

