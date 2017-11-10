from nose.tools import ok_, eq_

def test_case01():
    print("In test_case01()...")
    ok_(2+2 == 4, "Test Case Failure... ")

def test_case02():
    print("In test_case02()...")
    eq_(2+2, 4, "Test Case Failure...")

def test_case03():
    print("In test_case03()...")
    ok_(2+2 == 5, "Test Case Failure...")

def test_case04():
    print("In test_case04()...")
    eq_(2+2, 5, "Test Case Failure...")
