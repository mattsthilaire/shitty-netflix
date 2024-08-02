from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import generate_csrf, CSRFProtect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash


from db import db
from models import Users, Movies
from scripts.fill_db import add_movies

app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shitty_netflix.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
csrf = CSRFProtect(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = Users(username=form.username.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created.", "Success")
        return redirect(url_for("login"))
    return render_template("auth/register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash("You have been logged in.", "Success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessful. Please check username and password.", "danger")
    return render_template("auth/login.html", title="Login", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/")
def home():
    movies = Movies.query.all()
    return render_template("index.html", movies=movies)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/watch_movie/movie<movie_id>")
@login_required
def watch_movie(movie_id):
    movie = Movies.query.get_or_404(movie_id)
    if not movie:
        return "Movie not found", 404

    return render_template("watch_movie.html", movie=movie)


@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        title = request.form["title"]
        s3_url = request.form["s3_url"]
        image_url = request.form["image_url"]
        description = request.form["description"]

        new_movie = Movies(
            title=title, url=s3_url, image_url=image_url, description=description
        )
        db.session.add(new_movie)
        db.session.commit()

        flash("Movie added!", "success")
        return redirect(url_for("home"))

    csrf_token = generate_csrf()
    return render_template("add_movie.html", csrf_token=csrf_token)


# This just deals with the fact we have a local DB for now
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
