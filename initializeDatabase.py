import sqlite3

conn = sqlite3.connect('database.db')
print("database opened")

conn.execute(
    '''
    CREATE TABLE LIBRARY (
        SLIDE_ID        INT PRIMARY KEY     NOT NULL,
        SLIDE_NAME      TEXT UNIQUE         NOT NULL,
        FILE_LOCATION   TEXT                NOT NULL,
        MUST_FOLLOW     INT,
        MUST_PRECEDE    INT,
        MUST_AVOID      TEXT
    );
    '''
)

conn.execute(
    '''
    CREATE TABLE SCHEDULE (
        SCHEDULE_ID     INT PRIMARY KEY     NOT NULL,
        SLIDE_ID        INT                 NOT NULL,
        START_DATE      TEXT                NOT NULL,
        END_DATE        TEXT,
        DAY             INT,
        FOREIGN KEY (SLIDE_ID) REFERENCES LIBRARY(SLIDE_ID) ON UPDATE CASCADE ON DELETE CASCADE
    );
    '''
)

conn.close