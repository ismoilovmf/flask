from hashlib import md5
from flask import request
from flask.views import MethodView
from flask import jsonify
from sqlalchemy.exc import IntegrityError
from exceptions import ApiException
from models import Session, User, Adv, get_user, get_adv
from schema import CreateUser, PatchUser, CreateAdv, PatchAdv
from validate import validate


def helloworld():
    return 'Hello World!'


def hash_password(password: str):
    return md5(password.encode()).hexdigest()


class UserView(MethodView):
    def get(self, user_id):
        with Session() as session:
            user = get_user(user_id, session)
            if not user:
                raise ApiException(404, 'user not found')
            # print(f'{user} = ')
            return jsonify({
                'id': user.id,
                'email': user.email
            })

    def post(self):
        with Session() as session:
            json_data = request.json
            json_data = validate(json_data, CreateUser)
            json_data['password'] = hash_password(json_data['password'])
            new_user = User(**json_data)
            session.add(new_user)
            try:
                session.commit()
            except IntegrityError as er:
                raise ApiException(409, 'user already exists')
            return jsonify({'id': new_user.id, 'email': new_user.email})

    def delete(self, user_id):
        with Session() as session:
            user = get_user(user_id, session)
            session.delete(user)
            session.commit()
            return jsonify({'status': 'deleted'})


class AdvView(MethodView):

    def get(self, adv_id):
        with Session() as session:
            adv = get_adv(adv_id, session)
            return jsonify({
                'id': adv.id,
                'title': adv.title,
                'description': adv.description,
                'user_id': adv.user_id,
            })

    def post(self):
        with Session() as session:
            json_data = request.json
            json_data = validate(json_data, CreateAdv)
            adv = Adv(**json_data)
            session.add(adv)
            try:
                session.commit()
            except IntegrityError as er:
                print(er)
                raise ApiException(409, 'advertisements already exists')
            return jsonify({
                'title': adv.title,
                'description': adv.description,
                'user_id': adv.user_id,
            })

    def delete(self, adv_id):
        with Session() as session:
            adv = session.query(Adv).get(adv_id)
            session.delete(adv)
            session.commit()
            return jsonify({'status': 'deleted'})
