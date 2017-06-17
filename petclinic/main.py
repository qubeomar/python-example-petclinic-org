from petclinic import app

from flask import url_for, request, session, redirect, render_template, send_from_directory

import sys, traceback

@app.route('/')
def home():
    return app.send_static_file('home.html')

"""
    return render_template(
        '/petclinic/home.html'
        )
    return send_from_directory(
        'templates', '/petclinic/home.html'
        )
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
