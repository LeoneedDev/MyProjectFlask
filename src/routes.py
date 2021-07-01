from src import api
from flask_restful import Resource


class FilmListApi(Resource):
    def get(self, uuid=None):
        if not uuid:
            films = db.session.query(Film).all()
            return [f.to_dict() for f in films], 200
        film = db.session.query(Film).filter_by(uuid=uuid).first()
        if not film:
            return ',404'
        return film.to_dict(),200

    def post(self):
        film_json = request.json
        if not film_json:
            return {'message': 'Wrong data'}, 400
        try:
            film = Film(
                title=film_json['title'],
                release_date=datetime.strptime(film_json['release_date'], '%B %d, %Y'),

            )

    def put(self):
        pass

    def delete(self):
        pass


class ActorListApi(Resource):
    def get(self, uuid=None):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


api.add_resource(Smoke, '/smoke', strict_slashes=False)
api.add_resource(FilmListApi, '/films/<uuid>', strict_slashes=False)
