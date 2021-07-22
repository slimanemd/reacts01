
def webhook():
    import git
    import os

    repo = git.Repo('/home/slimanemd/reacts01')
    repo.remotes.origin.pull('main')

    app_loader = "/var/www/slimanemd_pythonanywhere_com_wsgi.py"
    os.system("touch " + app_loader)

    msg = "Updated site version successfully oh"
    return msg, 200


webhook()