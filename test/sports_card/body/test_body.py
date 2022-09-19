from pytest import mark

@mark.body
class BodyTests:
    @mark.door
    def test_body_functions_as_expected(self, chrome_browser):
        chrome_browser.get("http://stackoverflow.com")
        assert True

    def test_bumper(self):
        assert True
        
    def windshield(self):
        assert True