from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

movies = []

class MovieNames(Resource):
    def get(self, name) 
        for movie in movies:
            if movie['name'] == name:
                return movie
        return {'name':None}

    def post(self, name):
        movie = {'name':name}
        movies.append(movie)
        return movie

    def delete(self, name):
        for ind,movie in enumerate(movies):
            if movie['name'] == name:
                deleted_movie = movies.pop(ind)
                return {'note':'delete success'}

class AllMovies(Resource):
    def get(self):
        return {'movies':movies}

api.add_resource(MovieNames, '/movie/<string:name>')
api.add_resource(AllMovies, '/movies')


if __name__ == '__main__':
  app.run(debug=True)
 