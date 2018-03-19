import sys
import datetime
import mysql.connector

config = {
  'user': 'testUser',
  'password': 'testPass',
  'host': '172.17.0.2',
  'database': 'testDb',
}

query = ("SELECT * FROM testTable WHERE createdOn")

def extract(outPath) :
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute(query)

        with open(outPath, "w") as fout:
            for(ID, testNumber, createdOn) in cursor:
                fout.write("{0},{1:f},{2}\n".format(ID, testNumber, createdOn.isoformat()))
    finally:
        conn.close()
if __name__ == "__main__":
    out_file = sys.argv[1]
    extract(out_file)
