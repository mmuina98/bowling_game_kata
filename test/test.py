from src.scorecard import Scorecard


def test_get_total_score():
    test_all_strikes = Scorecard('XXXXXXXXXXXX')
    assert test_all_strikes.get_total_score() == 300

def test_random_score():
    test = Scorecard('9-9-9-9-9-9-9-9-9-9-')
    assert test.get_total_score() == 90

    test = Scorecard('9-3/613/815/-/8-7/8/8')
    assert test.get_total_score() == 131

    test = Scorecard('X9-9-9-9-9-9-9-9-9-')
    assert test.get_total_score() == 100

def test_all_spares():
    test = Scorecard('5/5/5/5/5/5/5/5/5/5/5')
    assert test.get_total_score() == 150

def test_two_extra_final_rolls():
    test = Scorecard('9-9-9-9-9-9-9-9-9-X9-')
    assert test.get_total_score() == 100

    test = Scorecard('X9-X9-9-9-9-9-9-9-')
    assert test.get_total_score() == 110

def test_two_strikes_in_a_row_is_a_double():
    test = Scorecard('XX9-9-9-9-9-9-9-9-')
    assert test.get_total_score() == 120

def test_three_strikes_in_a_row_is_a_triple():
    test = Scorecard('XXX9-9-9-9-9-9-9-')
    assert test.get_total_score() == 141

def test_two_strikes_in_extra_rolls():
    test = Scorecard('9-9-9-9-9-9-9-9-9-XXX')
    assert test.get_total_score() == 111

def test_spare_in_extra_roll():
    test = Scorecard('8/549-XX5/53639/9/X')
    assert test.get_total_score() == 149

    test = Scorecard('X5/X5/XX5/--5/X5/')
    assert test.get_total_score() == 175

