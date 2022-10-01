from unittest import skip
from pytest import mark


def test_tv_turns_on(tv_brand):
    print(f"{tv_brand} Testing turns on as expected")


@skip
def test_browser_can_navigate_to_training_ground(chrome_browser):
    chrome_browser.get("https://google.com/")
