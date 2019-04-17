import os
import _sqlite3
import pandas as pd

headers = [
'season', 
'episode_number',
'number_in_season',
'episode_name',
'director',
'writer',
'original_air_date',
'us_viewers',
'runtime',
'imdb_description',
'imdb_votes',
'imbdb_rating',
'notable_death_count'
]

got = pd.read_csv('got_csv.csv')

if os.path.exists('got.db'):
    os.remove('got.db')

conn = _sqlite3.connect('got.db')
got.to_sql('got', conn, dtype={

'season':'INTEGER',
'episode_number':'INTEGER',
'Number In Season':'INTEGER',
'episode_name':'VARCHAR256',
'Director':'VARCHAR(256)',
'Writer':'VARCHAR(256)',
'Original Air Date':'DATE',
'US Viewers (million)': 'FLOAT',
'Runtime': 'INTEGER',
'IMDB Description': 'VARCHAR(256)',
'IMDB Votes': 'INTEGER',
'IMDB Rating': 'FLOAT',
'Notable Death Count': 'INTEGER'
})

conn.row_factory = _sqlite3.Row

def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows 

def sql_edit_insert(query, var):
    cur = conn.cursor()
    cur.execute(query, var)
    conn.commit()

def sql_delete(query, var):
    cur = conn.cursor()
    cur.execute(query, var)
    conn.commit()

def sql_query2(query, var):
    cur = conn.cursor()
    print(query)
    print(var)
    cur.execute(query, var)
    rows = cur.fetchall()
    return rows
