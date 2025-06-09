from flask import Flask, render_template, url_for, g
# from supabase import create_client, Client
from dotenv import load_dotenv
import os
import psycopg2


app = Flask(__name__)


# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")


def get_db():
  # Opens a new database connection if there is none yet for the current application context.
  if 'db' not in g:
      g.db = psycopg2.connect(
          user=USER,
          password=PASSWORD,
          host=HOST,
          port=PORT,
          dbname=DBNAME
      )
  return g.db

@app.teardown_appcontext
def close_db(e=None):
    # Closes the database again at the end of the request.
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute(f"""
    select
      *
    from
      single_album
      join series on single_album.series_id = series.id
    order by
      release_date desc
    limit
      5
  """)
  data = cursor.fetchall()
  cursor.close()
  return render_template('index.html', data=data)

@app.route('/765as')
def imas():
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute(f"""
    select
      *
    from
      single_album
      join series on series_id = series.id
    where
      brand = 'as'
    order by
      release_date desc
    limit
      5
  """)
  data = cursor.fetchall()
  cursor.close() 
  return render_template('imas.html', data=data)

@app.route('/cg')
def cg():
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute(f"""
    select
      *
    from
      single_album
      join series on series_id = series.id
    where
      brand = 'cg'
    order by
      release_date desc
    limit
      5
  """)
  data = cursor.fetchall()
  cursor.close()
  return render_template('cg.html', data=data)

@app.route('/ml')
def ml():
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute(f"""
    select
      *
    from
      single_album
      join series on series_id = series.id
    where
      brand = 'ml'
    order by
      release_date desc
    limit
      5
  """)
  data = cursor.fetchall()
  cursor.close()
  return render_template('ml.html', data=data)

@app.route('/m')
def m():
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute(f"""
    select
      *
    from
      single_album
      join series on series_id = series.id
    where
      brand = 'm'
    order by
      release_date desc
    limit
      5
  """)
  data = cursor.fetchall()
  cursor.close()
  return render_template('m.html', data=data)

@app.route('/sc')
def sc():
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute(f"""
    select
      *
    from
      single_album
      join series on series_id = series.id
    where
      brand = 'sc'
    order by
      release_date desc
    limit
      5
  """)
  data = cursor.fetchall()
  cursor.close()
  return render_template('sc.html', data=data)

@app.route('/gkms')
def gkms():
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute(f"""
    select
      *
    from
      single_album
      join series on series_id = series.id
    where
      brand = 'gkms'
    order by
      release_date desc
    limit
      5
  """)
  data = cursor.fetchall()
  cursor.close()
  return render_template('gkms.html', data=data)

if __name__ == '__main__':
  app.run(debug=True)