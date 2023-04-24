import pytest


@pytest.mark.param
@pytest.mark.parametrize("val", ["one_param"])
def test_one_out(val):
    print("param = ", val)


@pytest.mark.param
@pytest.mark.parametrize("param", [1, 2])
def test_two_out(param):
    print("param = ", param)


@pytest.mark.param
@pytest.mark.parametrize("param_1", [345], ids=["my_id"])
def test_three_out(param_1):
    print("param = ", param_1)
