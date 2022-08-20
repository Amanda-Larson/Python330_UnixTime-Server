import os
from flask import Flask, render_template, request, redirect, url_for
import time as t

app = Flask(__name__)


@app.route('/')
def get_time():
    time = int(t.time())
    unix_time = f"In unix time, the time is now {time}."
    return unix_time


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
