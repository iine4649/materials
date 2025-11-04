from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)
name = "Shunsuke Honjo"
my_age = 18
hobbies = ["ROS Programming", "Control Theory", "Machine Learning", "Robotics", "Computer Vision"]
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    phone = "123-wompp-wompp"
    email = "shunsuke20070602honjo@gmail.com"
    return render_template("contact.html",name=name, phone=phone, email=email)

@app.route("/about")
def about():
    return render_template("about.html",name=name,age=my_age,hobbies=hobbies)

@app.route("/tennis")
def tennis():
    return render_template("tennis.html")

@app.route("/check_voting_eligibility", methods=["POST"])
def check_voting_eligibility():
    try:
        age = int(request.form.get("age", 0))
        
        if age >= 18:
            eligibility_message = f"You are eligible to vote!"
        else:
            eligibility_message = f"You are {age} years old. You need to be at least 18 years old to vote."
        
        return render_template("about.html", 
                             name=name, 
                             age=my_age, 
                             hobbies=hobbies, 
                             eligibility_message=eligibility_message,
                             submitted_age=age)
    except ValueError:
        return render_template("about.html", 
                             name=name, 
                             age=my_age, 
                             hobbies=hobbies, 
                             eligibility_message="Please enter a valid age.")

app.run(debug=True)