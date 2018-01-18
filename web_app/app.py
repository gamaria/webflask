from flask import  Flask

def create_app():
    app = Flask(__name__)


    @app.route('/halo')
    def index():
         return 'Hallo  flask'




    @app.route('/about')
    def about():
        return 'Hallo  i am about'



    return app
