import pytest
import datetime
import os
from transform_data import transform

lines =[
"1,1.0,03/18/2018\n",
"2,1.0,03/18/2018\n",
"3,2.0,03/18/2018\n",
"4,3.0,03/18/2018\n"
]

expectedLines = [
"1,5.0",
"2,5.0",
"3,10.0",
"4,15.0"
]

in_file = "./test.extracted"
out_file = "./test.processed"
seperator = ","

testStartDate = datetime.datetime.now()

def setUp():
    with open(in_file, "w") as f:
        f.writelines(lines)

def tearDown():
    os.remove(in_file)
    os.remove(out_file)

def test_transform():
    setUp()

    try:
        transform(in_file, out_file)
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
                assert testStartDate < datetime.datetime.strptime(actual[2], "%Y-%m-%dT%H:%M:%S.%f") < datetime.datetime.now()
    finally:
        tearDown()
