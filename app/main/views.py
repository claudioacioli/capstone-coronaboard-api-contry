from . import main as app_main


@app_main.route('/')
def index():
    return '/api/v0/'


