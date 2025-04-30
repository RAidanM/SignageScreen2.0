import sqlite3
from models import Slide

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def get_slide(slide_id:int):
    return conn.execute(
    '''
    SELECT *
    FROM catalogue
    WHERE slide_id = 
    
    ;
    '''    
    )
    conn.commit()


def create_slide(slide: Slide):
    return cursor.execute(
            '''
            INSERT INTO catalogue (title, content) 
            VALUES (?, ?)
            ''',
            (slide.title, slide.content)
        )

conn.close()