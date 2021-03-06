"""Application entry point"""

from app import connexion_app, db

# Done here to avoid circular import
connexion_app.add_api("specs.yaml")

# expose global WSGI application object
application = connexion_app.app


if __name__ == '__main__':
    # with application.app_context():
    #     db.create_all()
    application.run(host='0.0.0.0', port=8000)
