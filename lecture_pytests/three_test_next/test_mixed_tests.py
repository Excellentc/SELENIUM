import pytest


class TestFixtureTests1:

    @pytest.mark.pack
    @pytest.mark.other
    def test_one_out(self):
        print("mixed 1")

    @pytest.mark.pack
    @pytest.mark.other
    def test_two_out(self):
        print("mixed 2")


@pytest.mark.pack
@pytest.mark.rest
def test_three_out():
    print("mixed 3")
