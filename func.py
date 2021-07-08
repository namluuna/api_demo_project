import sqlite3

def get_all(query):
    conn = sqlite3.connect("data/dbquestion.db")
    data= conn.execute(query).fetchall()
    conn.close()
    return data

def get_by_id(number):
    conn = sqlite3.connect("data/dbquestion.db")
    sql="""
    select q.number, q.content , a.option_key, a.option_content from questions q inner join answers_option a on q.number = a.number
    where q.number = ?
    """
    data = conn.execute(sql,(number)).fetchall()
    conn.close()
    return data






