import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # rows = db.execute("SELECT price, stock FROM purchase JOIN users on users.id = purchase.id WHERE users.id = ?", session["user_id"])
    rows = db.execute("SELECT price, stock, amount FROM transactions JOIN users on users.id = transactions.user_id WHERE users.id = ? AND buy_sell = 'buy' AND active = 'yes'", session["user_id"])
    return render_template("index.html", rows = rows)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():

    if request.method == "GET":
        return render_template("buy.html")

    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("must enter a valid symbol", 403)

        shares = int(request.form.get("shares"))
        if shares < 0:
            return apology("please enter a positive number", 403)

        quote = lookup(symbol)["price"]

        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        remaining_cash = rows[0]["cash"]

        if remaining_cash < shares * quote:
            return apology("you must have enough of money on your account", 403)

        else:
            # db.execute("INSERT INTO purchase (price, stock) VALUES (?, ?)", quote, symbol)
            db.execute("INSERT INTO transactions (price, stock, amount, buy_sell, active, user_id) VALUES (?, ?, ?, ?, ?, ?)", quote, symbol, 1, "buy", "yes", session["user_id"])
            return redirect("/")





@app.route("/history")
@login_required
def history():
    rows = db.execute("SELECT price, stock, amount, buy_sell, timestamp FROM transactions JOIN users on users.id = transactions.user_id WHERE users.id = ?", session["user_id"])
    return render_template("history.html", rows = rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        try:
            symbol = request.form.get("symbol")
            quote = lookup(symbol)
            return render_template("quoted.html", symbol=symbol, quote=quote['price'])
        except:
            return apology("incorrect stock name or undefined error", 403)

    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 403)

        # ensure user isn't already registered
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) == 1:
            return apology("user already exists", 403)

        # add user to the DB
        else:
            password_hashed = generate_password_hash(request.form.get("password"))
            rows = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), password_hashed)

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        stocks = db.execute("SELECT stock FROM transactions JOIN users ON users.id = transactions.user_id WHERE users.id = ? AND buy_sell = 'buy' AND active = 'yes'", session["user_id"])
        return render_template("sell.html", stocks = stocks)

    if request.method == "POST":
        stock = request.form.get("stocks")
        print(stock)
        print(type(stock))
        if not stock:
            return apology("must enter a valid stock", 403)

        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        remaining_cash = rows[0]["cash"]

        # try:
            # db.execute("DELETE FROM purchase WHERE stock = ?", stock)
            # db.execute("DELETE FROM purchase WHERE stock = ?", stock)
        quote = lookup(stock)
        db.execute("UPDATE transactions SET active = 'no' WHERE stock = ?", quote['symbol'])
        db.execute("INSERT INTO transactions (price, stock, amount, buy_sell, active, user_id) VALUES (?, ?, ?, ?, ?, ?)", quote['price'], stock, 1, "sell", 'no', session["user_id"])
        rows = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        remaining_cash = rows[0]["cash"] - quote['price']
        print("remaining: ", remaining_cash)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", remaining_cash, session["user_id"])
        return redirect("/")
        # except:
        #     return apology("there was an unspecified error", 403)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
