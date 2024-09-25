from app import app

if __name__ == '__main__':
    host = app.config['HOST']
    port = app.config['PORT']
    app.run(host=host, port=port, debug=True)
