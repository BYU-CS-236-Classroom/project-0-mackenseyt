import os
import sys
import pytest

import project0
TEST_FUNC = project0.project0
TEST_ROOT_DIR = "./project0-passoff/"

@pytest.fixture
def bucket(request):
    return request.config.getoption("--bucket")

def read_file_contents(filepath):
    with open(filepath, "r") as f:
        return f.read()

def test_project1(bucket):
    test_dir = TEST_ROOT_DIR + bucket
    test_filenames = [f for f in os.listdir(test_dir) if f.startswith("input")]
    passed = True
    for filename in test_filenames:
        input_file = os.path.join(test_dir, filename)
        input_contents = read_file_contents(input_file)

        answer_file = os.path.join(test_dir, filename.replace('input', 'answer'))
        answer_contents = read_file_contents(answer_file)
        try:
            assert answer_contents == TEST_FUNC(input_contents)
            print("\n")
            print("Passed test: " + filename)
        except AssertionError as e:
            passed = False
            print("\n")
            print("Failed input: " + filename)
            print("--------------------------")
            print(e)
            print("--------------------------")
    assert passed
