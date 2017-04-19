"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():

    answer = request.args.get("yesno")

    if answer == "no":
        return render_template("goodbye.html")

    return render_template("game.html")


@app.route('/madlib', methods=["POST", "GET"])
def show_madlib():

    # person = request.args.get("person")
    # color = request.args.get("color")
    # adjectives = request.args.getlist("adjective")
    # noun = request.args.get("noun")

    person = request.form.get("person")
    color = request.form.get("color")
    adjectives = request.form.getlist("adjective")
    noun = request.form.get("noun")

    # if the method is POST, return this:
    if request.method =="POST":
      return render_template(choice(["madlibs.html", "madlibs2.html"]),
                             person=person,
                             color=color,
                             adjectives=adjectives,
                             noun=noun)
    else:  # else, return some nice message saying to go to /game first
      return render_template("method-error.html")

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
