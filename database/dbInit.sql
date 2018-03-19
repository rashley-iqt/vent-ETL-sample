CREATE TABLE IF NOT EXISTS testDb.testTable (
    ID          INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    testNumber  DECIMAL(10,5) NOT NULL,
    createdOn   DATETIME
);
SET @current_date = NOW();
INSERT INTO testDb.testTable
(testNumber, createdOn)
VALUES
(1.0, @current_date);
INSERT INTO testDb.testTable
(testNumber, createdOn)
VALUES
(1.0, @current_date);
INSERT INTO testDb.testTable
(testNumber, createdOn)
VALUES
(2.0, @current_date);
INSERT INTO testDb.testTable
(testNumber, createdOn)
VALUES
(3.0, @current_date);
