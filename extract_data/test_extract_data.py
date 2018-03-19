import pytest
import datetime
import os
from extract_data import extract

expectedLines = [
"1,1.0",
"2,1.0",
"3,2.0",
"4,3.0"
]

out_file = "./test.processed"
seperator = ","

testStartDate = datetime.datetime.now()

def setUp():
    return

def tearDown():
    os.remove(out_file)

def test_transform():
    setUp()

    try:
        extract(out_file)
        with open(out_file) as f:
            new_lines = f.readlines()
            for line in new_lines:
                i = new_lines.index(line)
                line = line.rstrip("\n")
                print(i)
                expectedLine = expectedLines[i]
                print(line)
                expected = expectedLine.split(seperator)
                actual = line.split(seperator)
                assert actual[0] == expected[0]
                assert float(actual[1]) == float(expected[1])
                assert datetime.datetime.strptime(actual[2], "%Y-%m-%dT%H:%M:%S")
    finally:
        tearDown()
