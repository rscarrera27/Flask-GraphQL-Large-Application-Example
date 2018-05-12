from app import create_app
from config.dev import Config

if __name__ == '__main__':
    app = create_app(Config)

    app.run(**Config.RUN_SETTING)