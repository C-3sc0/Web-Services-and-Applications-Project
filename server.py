from flask import Flask, request, jsonify, render_template, session
from config import secret_key as cfg
import mysql.connector
import requests


app = Flask(__name__)
app.secret_key = cfg['flask'] # user can choose his own secret key

# Connect to MySQL server without specifying a database
cnx = mysql.connector.connect(user=cfg['user'], password=cfg['password'],
                              host=cfg['host'])
cursor = cnx.cursor()

# Function to create database and table
def create_database_table():
    try:
        # Create the database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS WishlistDB")

        # Switch to the created database
        cursor.execute("USE WishlistDB")

        # Create movie table if it does not exist
        cursor.execute("CREATE TABLE IF NOT EXISTS movie ("
                       "id INT PRIMARY KEY, "
                       "title VARCHAR(255), "
                       "overview TEXT, "
                       "vote DECIMAL(3,1)"
                       ")")
        
        cursor.execute("CREATE TABLE IF NOT EXISTS tvShow ("
                       "id INT PRIMARY KEY, "
                       "name VARCHAR(255), "
                       "overview TEXT, "
                       "vote DECIMAL(3,1)"
                       ")")        

        cnx.commit()
    except mysql.connector.Error as err:
        print(f"Failed creating database or table: {err}")

create_database_table()

@app.route('/')
def project():
    return render_template('project.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/movie")
def movie_db():
    return render_template("movie.html")

@app.route("/wish-list/<int:id>", methods=["GET", "POST", "DELETE"])
def wishlist(id):
    try:
        # Fetch the wishlist from the session
        wishlist = session.get('wishlist', [])

        if request.method == 'GET':
            # Return the movie details based on the provided ID
            movie = next((item for item in wishlist if item['id'] == id), None)
            if movie:
                return jsonify({"movie": movie}), 200
            else:
                return jsonify({"message": "Movie not found in wishlist"}), 404

        # Add a new movie to the wishlist
        elif request.method == 'POST':
            movie = request.get_json()
            movie_id = movie.get('id')
            add_movie = ("INSERT INTO movie "
                         "(id, title, overview, vote) "
                         "VALUES (%s, %s, %s, %s)")
            movie_data = (movie['id'], movie['title'], movie['overview'], movie['vote_average'])
            cursor.execute(add_movie, movie_data)
            wishlist.append(movie)
            session['wishlist'] = wishlist
            cnx.commit()
            return jsonify({"message": "Movie added to wishlist", "movie": movie}), 200

        # Delete the movie from the wishlist table
        elif request.method == 'DELETE':
            deleted_movie = next((item for item in wishlist if item['id'] == id), None)
            if deleted_movie:
                delete_movie_from_wishlist = ("DELETE FROM movie WHERE id = %s")
                cursor.execute(delete_movie_from_wishlist, (id,))
                cnx.commit()
                wishlist = [item for item in wishlist if item['id'] != id]
                session['wishlist'] = wishlist
                return jsonify({"message": "Movie deleted from wishlist"}), 200
            else:
                return jsonify({"message": "Movie not found in wishlist"}), 404

    except Exception as e:
        # Handle exceptions appropriately
        return jsonify({"message": str(e)}), 500


@app.route("/wish-list")
def wish_list():
    get_movie = ("SELECT * FROM movie")
    get_show = ("SELECT * FROM tvShow")
    cursor.execute(get_movie)
    movies = cursor.fetchall()
    cursor.execute(get_show)
    tv_show = cursor.fetchall()
    print(movies, tv_show)
    return render_template("wish-list.html", movies=movies, tv_show=tv_show)

@app.route("/get-wishlist", methods=["GET"])
def get_wishlist():
    wishlist = session.get('wishlist', [])
    return jsonify({"wishlist": wishlist}), 200

# Update the movie in the database
@app.route("/wish-list/<int:id>", methods=["PUT"])
def update_wishlist(id):
    try:
        if not request.is_json:
            return jsonify({"message": "Invalid request: not JSON"}), 400

        movie = request.get_json()
        movie_id = movie.get('id')
        movie_title = movie.get('title')
        movie_poster_path = movie.get('poster_path')
        vote_average = movie.get('vote_average')
        movie_overview = movie.get('overview')
        wishlist = session.get('wishlist', [])

        if not all([movie_id, movie_title, movie_poster_path]):
            return jsonify({"message": "Invalid request: missing fields"}), 400

        update_movie_query = ("UPDATE movie "
                              "SET id = %s, title = %s, overview = %s, vote = %s "
                              "WHERE id = %s")
        movie_data = (movie_id, movie_title, movie_overview, vote_average, id)
        cursor.execute(update_movie_query, movie_data)
        cnx.commit()

        for item in wishlist:
            if item['id'] == id:
                item['id'] = movie_id
                item['title'] = movie_title
                item['poster_path'] = movie_poster_path
                item['overview'] = movie_overview
                item['vote_average'] = vote_average
                session['wishlist'] = wishlist
                print(item['overview'] , item['vote_average'])
                return jsonify({"message": "Movie updated in wishlist", "updated_movie": item}), 200

        return jsonify({"message": "Movie not found in wishlist"}), 404
    except mysql.connector.Error as err:
        return jsonify({"message": f"Failed to update movie in wishlist: {err}"}), 400
    except Exception as e:
        print("Error:", e)
        return jsonify({"message": "An error occurred"}), 500


# Flask app for Tv Show Database
@app.route("/tv-show")
def tv_show_db():
    return render_template("tv-show.html")

@app.route("/get_tvshow_wishlist", methods=["GET"])
def get_show_wishlist():
    tvShowwishlist = session.get('tvShowwishlist', [])
    return jsonify({"tvShowwishlist": tvShowwishlist}), 200


@app.route("/wish-list/tv-show/<int:id>", methods=["GET", "POST", "DELETE"])
def tvshow_wishlist(id):
    try:
        tvShowwishlist = session.get('tvShowwishlist', [])

        if request.method == 'GET':
            tvshow = next((item for item in tvShowwishlist if item['id'] == id), None)
            if tvshow:
                return jsonify({"tvshow": tvshow}), 200
            else:
                return jsonify({"message": "Tv Show not found in wishlist"}), 404
    
        elif request.method == 'POST':
            tv_show = request.get_json() 
            tvshow_id = tv_show.get('id')
            add_tv_show = ("INSERT INTO tvShow "
                         "(id, name, overview, vote) "
                         "VALUES (%s, %s, %s, %s)")
            tv_show_data = (tv_show['id'], tv_show['name'], tv_show['overview'], tv_show['vote_average'])
            cursor.execute(add_tv_show, tv_show_data)
            tvShowwishlist.append(tv_show)
            session['tvShowwishlist'] = tvShowwishlist
            cnx.commit()
            return jsonify({"message": "Tv show added to wishlist", "tv_show":tv_show}), 200

        elif request.method == 'DELETE':
            delete_tv_show_from_wishlist = ("DELETE FROM tvShow WHERE id = %s")
            cursor.execute(delete_tv_show_from_wishlist, (id,))
            cnx.commit()

            deleted_tv_show = next((item for item in tvShowwishlist if item['id'] == id), None)
            tvShowwishlist = [item for item in tvShowwishlist if item['id'] != id]
            session['tvShowwishlist'] = tvShowwishlist
            if deleted_tv_show:
                return jsonify({"message": "Tv Show deleted from wishlist", "movie": deleted_tv_show}), 200
            else:
                return jsonify({"message": "Tv Show  not found in wishlist"}), 404
    except Exception as e:
        print("Error:", e)
        return jsonify({"message": "An error occurred"}), 500

@app.route("/update_tv_show_wishlist/<int:id>", methods=["PUT"])
def update_tv_show_wishlist(id):
    try:
        if not request.is_json:
            return jsonify({"message": "Invalid request: not JSON"}), 400

        tv_show = request.get_json()
        tv_show_id = tv_show.get('id')
        tv_show_title = tv_show.get('name')
        tv_show_poster_path = tv_show.get('poster_path')
        tv_show_vote_average = tv_show.get('vote_average')
        tv_show_overview = tv_show.get('overview')
        tvShowwishlist = session.get('tvShowwishlist', [])

        if not all([tv_show_title, tv_show_poster_path]):
            return jsonify({"message": "Invalid request: missing fields"}), 400

        update_tv_show = ("UPDATE tvShow "
                              "SET id = %s, name = %s, overview = %s, vote = %s "
                              "WHERE id = %s")
        tv_show_data = (tv_show_id, tv_show_title, tv_show_overview, tv_show_vote_average, id)
        cursor.execute(update_tv_show, tv_show_data)
        cnx.commit()
    
        for item in tvShowwishlist:
            if item['id'] == id:
                item['id'] = tv_show_id
                item['name'] = tv_show_title
                item['poster_path'] = tv_show_poster_path
                item['overview'] = tv_show_overview
                item['vote_average'] = tv_show_vote_average
                session['tvShowwishlist'] = tvShowwishlist
                print(item['overview'] , item['vote_average'])
                return jsonify({"message": "Tv Show updated in wishlist", "update_tv_show": item}), 200
        return jsonify({"message": "Tv Show not found in wishlist"}), 404
    except mysql.connector.Error as err:
        return jsonify({"message": f"Failed to update movie in wishlist: {err}"}), 400
    except Exception as e:
        print("Error:", e)
        return jsonify({"message": "An error occurred"}), 500

@app.route("/documentation")
def doc():
    return render_template("documentation.html")

if __name__ == "__main__":
    app.run(debug = True)