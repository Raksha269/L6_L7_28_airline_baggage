import pytest

from airline_baggage import baggage_fee, carry_on_ok, check_in_status


def test_within_allowance():
    assert baggage_fee("economy", 10, "domestic", False) == 0


def test_carry_on_ok():
    assert carry_on_ok(5, 1, False) is True


def test_unknown_cabin():
    with pytest.raises(ValueError, match="unknown cabin"):
        baggage_fee("first", 10, "domestic", False)


def test_invalid_weight():
    with pytest.raises(ValueError, match="invalid weight"):
        baggage_fee("economy", -1, "domestic", False)


def test_member_extra_allowance():
    assert baggage_fee("economy", 20, "domestic", True) == 0


def test_domestic_excess():
    assert baggage_fee("economy", 20, "domestic", False) == 100


def test_international_excess():
    assert baggage_fee("economy", 20, "international", False) == 225


def test_large_domestic_excess():
    assert baggage_fee("economy", 40, "domestic", False) == 1000


def test_large_international_excess():
    assert baggage_fee("economy", 40, "international", False) == 2500


def test_infant_two_items():
    assert carry_on_ok(10, 2, True) is True


def test_infant_more_than_two_items():
    assert carry_on_ok(10, 3, True) is False


def test_carry_on_over_weight():
    assert carry_on_ok(8, 1, False) is False


def test_carry_on_too_many_items():
    assert carry_on_ok(5, 2, False) is False


def test_check_in_open_with_baggage():
    assert check_in_status(60, True, False) == "open"


def test_check_in_late_with_baggage():
    assert check_in_status(50, True, False) == "late"


def test_check_in_closed_with_baggage():
    assert check_in_status(40, True, False) == "closed"


def test_check_in_open_without_baggage():
    assert check_in_status(45, False, False) == "open"


def test_check_in_late_international():
    assert check_in_status(105, False, True) == "open"


def test_check_in_closed_international():
    assert check_in_status(100, False, True) == "late"