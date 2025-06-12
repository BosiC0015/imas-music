from flask import Flask, render_template, url_for, g, request, jsonify
from dotenv import load_dotenv
import os
import psycopg2
import urllib.parse


app = Flask(__name__)


# Load environment variables from .env
load_dotenv()

# Fetch variables
# USER = os.getenv("user")
# PASSWORD = os.getenv("password")
# HOST = os.getenv("host")
# PORT = os.getenv("port")
# DBNAME = os.getenv("dbname")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("DB_PORT")
DBNAME = os.getenv("DBNAME")



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


def fetch_data(search_term=None, brand_filter=None, ml_as_sp_filter=None, serie_filter=None): # ADD serie_filter
  conn = None
  cursor = None
  data = []
  try:
    conn = get_db()
    cursor = conn.cursor()

    sql_query = f"""
      select
        *
      from
        single_album
        join series on single_album.series_id = series.id
    """

    where_clauses = []
    query_params = []

    if search_term:
      search_pattern = f"%{search_term}%"
      where_clauses.append("(title ilike %s OR serie_name ilike %s OR brand ilike %s)")
      query_params.extend([search_pattern, search_pattern, search_pattern])
      
    if brand_filter:
      where_clauses.append("brand = %s")
      query_params.append(brand_filter)

    if ml_as_sp_filter:
      where_clauses.append("brand in %s")
      query_params.append(ml_as_sp_filter)

    if serie_filter:
      where_clauses.append("serie_name = %s")
      query_params.append(serie_filter)

    # Combine WHERE clauses if any exist
    if where_clauses:
      sql_query += " where " + " and ".join(where_clauses)

    sql_query += """
      order by
        release_date desc
      limit
        5
    """

    print(f"DEBUG SQL Query: {sql_query}")
    print(f"DEBUG Query Params: {query_params}")

    cursor.execute(sql_query, query_params)
    data = cursor.fetchall()

  except Exception as e:
    print(f"Error fetching data from DB: {e}")
    return {"error": str(e)}
  finally:
    if cursor:
      cursor.close()
  return data



@app.route('/')
def index():
  init_data = fetch_data()
  print(init_data)
  return render_template('index.html', data=init_data)

@app.route('/765as')
def imas(): 
  as_init_data = fetch_data(ml_as_sp_filter=('as', 'ml_as'))
  return render_template('imas.html', data=as_init_data)

@app.route('/cg')
def cg():
  cg_init_data = fetch_data(brand_filter='cg')
  return render_template('cg.html', data=cg_init_data)

@app.route('/ml')
def ml():
  ml_init_data = fetch_data(ml_as_sp_filter=('ml', 'ml_as'))
  return render_template('ml.html', data=ml_init_data)

@app.route('/m')
def m():
  m_init_data = fetch_data(brand_filter='m')
  return render_template('m.html', data=m_init_data)

@app.route('/sc')
def sc():
  sc_init_data = fetch_data(brand_filter='sc')
  return render_template('sc.html', data=sc_init_data)

@app.route('/gkms')
def gkms():
  gkms_init_data = fetch_data(brand_filter='gkms')
  return render_template('gkms.html', data=gkms_init_data)

if __name__ == '__main__':
  app.run(debug=True)