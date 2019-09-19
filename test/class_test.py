import allure


class TestClass(object):
    @allure.id("15")
    @allure.feature("Class")
    def test_class(self):
        pass

    @allure.id("13")
    @allure.feature("Class")
    def test_class_again(self):
        pass
