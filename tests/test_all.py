from tests.test_color import TestColor

for test in (TestColor,):
    print(f"Running tests of {test.__name__}")
    test.run_all()