from flask import Flask, render_template, url_for, g
from supabase import create_client, Client
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
      join series_test on single_album.series_id = series_test.id
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
   return render_template('imas.html')

@app.route('/cg')
def cg():
  return render_template('cg.html')

@app.route('/ml')
def ml():
  return render_template('ml.html')

@app.route('/m')
def m():
  return render_template('m.html')

@app.route('/sc')
def sc():
  return render_template('sc.html')

@app.route('/gkms')
def gkms():
  return render_template('gkms.html')

if __name__ == '__main__':
  app.run(debug=True)