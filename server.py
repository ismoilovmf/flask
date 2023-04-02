from hashlib import md5
from adv import get_app
from views import UserView, AdvView, helloworld

app = get_app()


class ApiException(Exception):

    def __init__(self, status_code: int, description):
        self.status_code = status_code
        self.description = description


def hash_password(password: str):
    return md5(password.encode()).hexdigest()


app.add_url_rule('/hello/', view_func=helloworld, methods=['get'])
app.add_url_rule('/user/', view_func=UserView.as_view('users_create'), methods=['POST'])
app.add_url_rule('/user/<int:user_id>/', view_func=UserView.as_view('users'), methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/advertisement/', view_func=AdvView.as_view('advertisements_create'), methods=['POST'])
app.add_url_rule('/advertisement/<int:adv_id>/', view_func=AdvView.as_view('advertisements'), methods=['GET', 'DELETE'])


if __name__ == '__main__':
    app.run()
