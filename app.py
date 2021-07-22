# flask
from flask import Flask, render_template
import os

# app
static_path = "/static"  #os.getenv('APP_STATIC_PATH') or
app = Flask(__name__ , static_url_path= static_path)

# home
@app.route('/')
def index():
    return render_template("index.html")

# ===========================================================================
# webhook


@app.route("/update_server", methods=['POST'])
def webhook():
    import git
    import os

    repo = git.Repo('/home/slimane/mysite/reacts01')
    repo.remotes.origin.pull('main')

    app_loader = "/var/www/slimane_pythonanywhere_com_wsgi.py"
    os.system("touch " + app_loader)

    msg = "Updated site version successfully ok"
    return msg, 200


# ==================================================================================================
# main


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
