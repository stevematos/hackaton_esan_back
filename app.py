# compose_flask/app.py

from mvc import create_app

if __name__ == "__main__":
    main = create_app()
    main.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    main.run(host="0.0.0.0", debug=True)