import allure
import pytest


@allure.feature("Parametrized")
@pytest.mark.parametrize("param", [True, False], ids=["pass", "fail"])
def test_parametrized(param):
    assert param


@allure.feature("Parametrized")
@pytest.mark.parametrize("param", [1, 2], ids=["one", "two"])
def test_another_parametrized(param):
    pass
