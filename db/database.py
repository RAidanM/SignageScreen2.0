import sqlite3

conn = sqlite3.connect('database.db')
print("database opened")

conn.execute(
    '''
    CREATE TABLE catalogue (
        slide_id        INT PRIMARY KEY     NOT NULL,
        slide_name      TEXT UNIQUE         NOT NULL,
        file_location   TEXT                NOT NULL,
        must_follow     INT,
        must_precede    INT,
        must_avoid      TEXT
    );
    '''
)

conn.execute(
    '''
    CREATE TABLE schedule (
        schedule_id     INT PRIMARY KEY     NOT NULL,
        slide_id        INT                 NOT NULL,
        start_date      TEXT                NOT NULL,
        end_date        TEXT,
        day             INT,
        FOREIGN KEY (slide_id) REFERENCES LIBRARY(slide_id) ON UPDATE CASCADE ON DELETE CASCADE
    );
    '''
)

conn.close