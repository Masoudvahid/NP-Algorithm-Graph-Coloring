import tests.testing as test
from tests.runtime import *


def perform_tests(runtime=0, unittest=0):
    # Runtime testing
    if runtime == 1:
        perform_runtime_test()
        quit(0)
    # Functionality testing
    if unittest == 1:
        test.unittest.main(module=test)
        quit(0)
