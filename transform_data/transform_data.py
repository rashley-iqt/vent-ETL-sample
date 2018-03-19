import sys
import datetime

seperator = ","

#checks to see if a string can be cast as a float
def isNumeric(inStr):
    returnVal = False
    try:
        float(inStr)
        returnVal = True
    except:
        returnVal = False

    return returnVal

#open file test.extracted for read
#open file test.processed for write
#read row from .extracted, parse out values and multiply by 5
#write line to .processed
def transform(inPath, outPath):
    with open(inPath, "r") as fin:
        with open(outPath, "w") as fout:
            lines = fin.readlines()
            for line in lines:
                items = line.split(seperator)
                if len(items) != 3 or not isNumeric(items[1]):
                    print(items)
                    raise Exception("Malformed Line")
                else:
                    fout.write("{0},{1:f},{2}\n".format(items[0], float(items[1])*5,datetime.datetime.now().isoformat()))

if __name__ == "__main__":
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    transform(in_file, out_file)
