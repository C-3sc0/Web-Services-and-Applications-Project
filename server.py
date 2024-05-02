from flask import Flask, request, jsonify, render_template, session
from config import secret_key as cfg


app = Flask(__name__)
app.secret_key = cfg['flask']

@app.route('/')
def project():
    return render_template('project.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/movie")
def movie_db():
    return render_template("movie.html")

@app.route("/add_delete_wish-list", methods=["POST", "DELETE"])
def wishlist():
    movie = request.get_json() 
    wishlist = session.get('wishlist', [])
    movie_id = movie.get('id')

    if request.method == 'POST':
        # Check if the movie is already in the wishlist
        if movie_id not in [item['id'] for item in wishlist]:
            wishlist.append(movie)
            session['wishlist'] = wishlist
            return jsonify({"message": "Movie added to wishlist"}), 200
        else:
            return jsonify({"message": "Failed to add movie to wishlist"}), 400
    elif request.method == 'DELETE':
        # Check if the movie is in the wishlist
        for i, item in enumerate(wishlist):
            if item['id'] == movie_id:
                del wishlist[i]
                session['wishlist'] = wishlist
                return jsonify({"message": "Movie deleted from wishlist"}), 200
        return jsonify({"message": "Movie not found in wishlist"}), 400
    
@app.route("/wish-list")
def wish_list():
    return render_template("wish-list.html")

@app.route("/get-wishlist", methods=["GET"])
def get_wishlist():
    wishlist = session.get('wishlist', [])
    #return jsonify(wishlist), 200
    return jsonify({"wishlist": wishlist}), 200

@app.route("/update_wishlist/<int:id>", methods=["PUT"])
def update_wishlist(id):
    if not request.is_json:
        return jsonify({"message": "Invalid request: not JSON"}), 400
    

    movie = request.get_json()
    wishlist = session.get('wishlist', [])
    print(wishlist)


    movie_id = movie.get('id')
    movie_title = movie.get('title')
    movie_poster_path = movie.get('poster_path')

    if not all([movie_title, movie_poster_path]):
        return jsonify({"message": "Invalid request: missing fields"}), 400

    for item in wishlist:
        if item['id'] == id:
            # Update the movie details
            item['id'] = movie_id
            item['title'] = movie_title
            item['poster_path'] = movie_poster_path
            session['wishlist'] = wishlist
            #print(item['title'], "\n\n\n\n")
            #print(item['poster_path'], "\n\n\n\n")
            return jsonify({"message": "Movie updated in wishlist"}), 200

    return jsonify({"message": "Movie not found in wishlist"}), 404


@app.route("/tv-show")
def tv_show_db():
    return render_template("tv-show.html")

#@app.route("/documentation")
#def doc():
#    return render_template("documentation.html")

#@app.route("/inquery")
#def inquery():
#    name = request.args["name"]
#    return request.args
#
#@app.route("/inbody", methods=["POST"])
#def inbody():
#    name = request.json["name"]
#    age = request.json["age"]
#    #print (request.json)
#    return f"you are {name} and aged {age} {type(age)}"
#
#@app.route('/user')
#def getuser():
#    user={
#        'name': "andrew",
#        'age' : 21
#    }
#    return jsonify(user)

if __name__ == "__main__":
    app.run(debug = True)