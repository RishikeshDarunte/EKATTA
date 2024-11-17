from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length):
    alpha_count = length * 50 // 100
    num_count = length * 30 // 100
    special_count = length - (alpha_count + num_count)
    
    alphabets = random.choices(string.ascii_letters, k=alpha_count)
    numbers = random.choices(string.digits, k=num_count)
    specials = random.choices("@#$%&*", k=special_count)
    
    password_list = alphabets + numbers + specials
    random.shuffle(password_list)
    
    return ''.join(password_list)

@app.route("/", methods=["GET", "POST"])
def home():
    password = None
    if request.method == "POST":
        try:
            length = int(request.form["length"])
            if length < 5:
                password = "Password length must be at least 5."
            else:
                password = generate_password(length)
        except ValueError:
            password = "Please enter a valid number."
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
