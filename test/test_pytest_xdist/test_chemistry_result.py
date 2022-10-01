import time
from pytest import mark

@mark.new
def test_result_1_completes_as_excepted():
    time.sleep(5)
    print("Result 1 completed successfully")

@mark.new
def test_result_2_completes_as_excepted():
    time.sleep(5)
    print("Result 2 completed successfully")

@mark.new
def test_result_3_completes_as_excepted():
    time.sleep(5)
    print("Result 3 completed successfully")

@mark.new
def test_result_4_completes_as_excepted():
    time.sleep(5)
    print("Result 4 completed successfully")