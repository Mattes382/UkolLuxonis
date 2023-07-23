from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_data_from_database():
    connection = psycopg2.connect(
        host="postgres",
        port=5432,
        user="postgres",
        password="yourpassword",
        database="sreality"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT title, image_url FROM scraped_data")
    data = cursor.fetchall()
    connection.close()
    return data

@app.route('/')
def index():
    data = get_data_from_database()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
