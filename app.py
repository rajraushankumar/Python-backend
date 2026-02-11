from flask import Flask, render_template, request
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "data.json"

# Ensure data.json exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)


@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        now = datetime.now()

        new_user = {
            "first_name": request.form["first_name"],
            "middle_name": request.form["middle_name"],
            "last_name": request.form["last_name"],
            "phone": request.form["phone"],
            "email": request.form["email"],
            "password": request.form["password"],
            "registration_date": now.strftime("%d-%m-%Y"),
            "registration_time": now.strftime("%H:%M:%S")
        }

        # Read existing users
        with open(DATA_FILE, "r") as f:
            users = json.load(f)

        # Add new user
        users.append(new_user)

        # Save back to JSON
        with open(DATA_FILE, "w") as f:
            json.dump(users, f, indent=4)

        return render_template("success.html", user=new_user)

    return render_template("index.html")


@app.route("/users")
def users():
    with open(DATA_FILE, "r") as f:
        users = json.load(f)

    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)
