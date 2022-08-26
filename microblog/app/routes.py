from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user={'username':'Edson'} #mock user

    posts=[ #mock posts
        {
            'author':{'username':'João'},
            'body':'belo dia!'
        },
        {
            'author':{'username':'Susan'},
            'body':'O filme dos vingadores foi incrivel!!'
        }
    ]

    return render_template("index.html", title='Home',user=user, posts=posts)