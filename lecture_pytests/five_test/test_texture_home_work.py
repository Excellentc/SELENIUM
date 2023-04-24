import pytest


class TestFixtureTests:

    @pytest.mark.from_class
    def test_one(self):
        print ("1 class")

    @pytest.mark.from_class
    def test_two(self):
        print ("2 class")

    @pytest.mark.from_class
    def test_three(self):
        print ("3 class")

    @pytest.mark.from_class
    def test_four(self):
        print ("4 class")

    @pytest.mark.from_class
    def test_five(self):
        print ("5 class")
