import hashlib
from api.decorators import logger_gunicorn
from api.extensions import db
from api.user.models import User
from flask import abort, current_app as app



class UserService:

    @classmethod
    @logger_gunicorn
    def create(cls, request):
        app.logger.info('Creating user')

        user_dto = request.get_json()
        first_name = user_dto.get('first_name')
        last_name = user_dto.get('last_name')
        password = user_dto.get('password')
        login = user_dto.get('login')
        email = user_dto.get('email')

        if not first_name \
                or not last_name\
                or not password\
                or not login\
                or not password\
                or not email:
            abort(400)

        # if cls.find_by_login(login):
        #     abort(412)

        try:
            user = User(first_name,
                        last_name,
                        email,
                        login,
                        hashlib.sha224(password.encode('utf-8')).hexdigest())

            db.session.add(user)
            db.session.commit()

            return dict(id=user.id,
                        first_name=user.first_name,
                        last_name=user.last_name,
                        email=user.email,
                        login=user.login)

        except Exception as e:
            app.logger.error("Error: ", e)
            db.session.rollback()
            abort(400)

    @staticmethod
    @logger_gunicorn
    def find_all(page=1):
        app.logger.info('Finding all users')
        return [dict(id=u.id,
                     first_name=u.first_name,
                     last_name=u.last_name,
                     email=u.email,
                     login=u.login,
                     password=u.password
                     ) for u in User.query.paginate(page, 10).items]

    @staticmethod
    @logger_gunicorn
    def update(request, id):
        app.logger.info('Update user with id: %s', id)
        user_dto = request.get_json()
        first_name = user_dto.get('first_name')
        last_name = user_dto.get('last_name')
        password = user_dto.get('password')
        login = user_dto.get('login')
        email = user_dto.get('email')

        user = User.query.filter_by(id=id).first()

        if not user:
            abort(404)

        if not first_name \
                or not last_name\
                or not password\
                or not login\
                or not password\
                or not email:
            abort(400)

        user.first_name = first_name
        user.last_name = last_name
        user.password = hashlib.sha224(password.encode('utf-8')).hexdigest()
        user.email = email

        db.session.add(user)
        db.session.commit()

        return dict(id=user.id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    password=user.password,
                    login=user.login,
                    email=user.email)

    @staticmethod
    @logger_gunicorn
    def find_one(id):
        app.logger.info('Find user with id: %s', id)
        u = User.query.filter_by(id=id).first()

        if not u:
            abort(404)

        return dict(id=u.id,
                    first_name=u.first_name,
                    last_name=u.last_name,
                    password=u.password,
                    login=u.login,
                    email=u.email)
    
    @classmethod
    @logger_gunicorn
    def find_by_login(cls, login):
        app.logger.info('Finding user with login: %s', login)
        u = User.query.filter_by(login=login).first()

        if not u:
            return None

        return dict(id=u.id,
                    first_name=u.first_name,
                    last_name=u.last_name,
                    password=u.password,
                    login=u.login,
                    email=u.email)
