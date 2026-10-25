from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/profile")
def profile():
    return render_template("profile.html", title="Profile")

@app.route("/works")
def works():
    return render_template("works.html", title="Works")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html", title="Contacts")

@app.route("/uppercase")
def uppercase():
    return render_template("uppercase.html", title="To Uppercase")

@app.route("/circle")
def circle():
    return render_template("circle.html", title="Area of a Circle")

@app.route("/triangle")
def triangle():
    return render_template("triangle.html", title="Area of a Triangle")

@app.route("/linked-list")
def linked_list():
    return render_template("linked_list.html", title="Linked List Operations")


@app.route("/infix-postfix")
def infix_postfix():
    return render_template("infix_postfix.html", title="Infix to Postfix")


@app.route("/stack")
def stack():
    return render_template("stack.html", title="Stack Operations")


@app.route("/queue-deque")
def queue_deque():
    return render_template("queue_deque.html", title="Queues and Deques")


if __name__ == "__main__":
    app.run(debug=True)
