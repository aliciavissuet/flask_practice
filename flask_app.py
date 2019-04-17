from flask import Flask, request, redirect, render_template

app = Flask(__name__)
@app.route('/')
def sql_database():
    from functions.sqlquery import sql_query
    results = sql_query(''' SELECT * FROM got ''')
    msg = 'Return all rows'
    return render_template('sqldatabase.html', results=results, msg=msg)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/delete', methods = ['POST', 'GET'])
def sql_datadelete():
    from functions.sqlquery import sql_delete, sql_query, sql_query2
    if request.method == 'GET':
        # print('here')
        name=request.args.get('episode_name')
        print(name)
        # fname=request.args.get('fname')
        # item = sql_query2(''' SELECT * FROM got WHERE `episode name`= ? ''', (name, ))
        # print(item, 'ITEM')
        sql_delete(
'''DELETE FROM got where `episode name` = (?)''', (name,))

    results=sql_query(''' SELECT * FROM got''')
    msg='deleted the '+name+' item from db'
    return render_template('sqldatabase.html', results = results, msg = msg)

@app.route('/new', methods = ['GET'])
def sql_form():
        return render_template('sqlform.html')

@app.route('/post', methods = ['POST'])
def sql_create():
        # print(request.values)
        from functions.sqlquery import sql_edit_insert, sql_query
        season = request.form['season']
        episode_number = request.form['episode_number']
        number_in_season = request.form['number_in_season']
        episode_name = request.form['episode_name']
        director = request.form['director']
        writer = request.form['writer']
        original_air_date = request.form['original_air_date']
        us_viewers = request.form['us_viewers']
        runtime = request.form['runtime']
        imdb_description = request.form['imdb_description']
        imdb_votes = '0'
        imdb_rating = '10'
        notable_death_count = request.form['notable_death_count']
        print(notable_death_count)
        sql_edit_insert(''' INSERT INTO got (`season`,`episode number`,`number in season`,`episode name`,`director`,`writer`, `original air date`, `us viewers (million)`, `runtime (mins)`, `imdb description`, `imdb votes`, `imdb rating`, `notable death count`) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?) ''',
                        (season, episode_number, number_in_season, episode_name, director, writer, original_air_date, us_viewers, runtime, imdb_description, imdb_votes, imdb_rating, notable_death_count))
        results = sql_query(''' SELECT * FROM got''')
        msg='added the '+episode_name+' item from db'
        return render_template('sqldatabase.html', results = results, msg = msg)

@app.route('/edit', methods = ['GET'])
def sql_edit():
        from functions.sqlquery import sql_query2
        name = request.args.get('episode_name')
        episode_to_edit = sql_query2(''' SELECT * FROM got WHERE `episode name` = ?''', (name, ))
        return render_template('sqlform2.html', results=episode_to_edit)

@app.route('/update', methods = ['POST'])
def sql_update():
        from functions.sqlquery import sql_edit_insert, sql_query
        
        old_episode_name = request.form['old_episode_name']
        season = request.form['season']
        episode_number = request.form['episode_number']
        number_in_season = request.form['number_in_season']
        episode_name = request.form['episode_name']
        director = request.form['director']
        writer = request.form['writer']
        original_air_date = request.form['original_air_date']
        us_viewers = request.form['us_viewers']
        runtime = request.form['runtime']
        imdb_description = request.form['imdb_description']
        imdb_votes = '0'
        imdb_rating = '10'
        notable_death_count = request.form['notable_death_count']
        # print(old_episode_name)
        sql_edit_insert(''' UPDATE got set `season`=?, `episode number`=?, `number in season`=?, `episode name`=?, `director`=?, `writer`=?, `original air date`=?, `us viewers (million)`=?, `runtime (mins)`=?, `imdb description`=?, `imdb votes`=?, `imdb rating`=?, `notable death count`=? WHERE `episode name` = ?''',
                        (season, episode_number, number_in_season, episode_name, director, writer, original_air_date, us_viewers, runtime, imdb_description, imdb_votes, imdb_rating, notable_death_count, old_episode_name))
        results = sql_query(''' SELECT * FROM got''')
        # print(results[0]['Episode Name'])
        msg = 'updated the '+old_episode_name+' item from db'
        return render_template('sqldatabase.html', results=results, msg=msg)

