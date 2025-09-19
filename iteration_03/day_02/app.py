from flask import Flask, jsonify, request, render_template, redirect, url_for 
import requests
import json
import os
from user import User
app = Flask(__name__)

# JSON file path
JSON_FILE = "user_data.json"

def save_user_to_json(user_data):
    try:
        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                users_data = json.load(f)
    
        
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(users_data, f, ensure_ascii=False, indent=2)
        
        return True
    except Exception as e:
        print(f"Error saving to JSON: {e}")
        return False

def load_users_from_json():
    try:
        if os.path.exists(JSON_FILE):
            with open(JSON_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    except Exception as e:
        print(f"Error loading from JSON: {e}")
        return []

user_html = """
    <h1>User App</h1>
        <form action="/user" method="get">
        <label>Enter name:</label>
        <input type="text" name="name">
        <label>Enter age:</label>
        <input type="text" name="age">
        <label>Enter hobbies:</label>
        <input type="text" name="hobbies">
        <button type="submit">Get User</button>
    </form>
"""

show_html = """
    <h1>Show App</h1>
    <p>Hello, {name}! You are {age} years old.</p>
    <p>Your hobbies are {hobbies}.</p>
    <br>
    <form action="/save_user" method="post" style="display: inline;">
        <input type="hidden" name="name" value="{name}">
        <input type="hidden" name="age" value="{age}">
        <input type="hidden" name="hobbies" value="{hobbies}">
        <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Save to JSON</button>
    </form>
    <br><br>
    <button type="Back To Form">    <a href="/home">Back to Form</a>
    <button type="View All Users">  <a href="/view_users">View All Users</a>
    <br><br>
    <p style="color: green;">{save_message}</p>
"""


@app.route("/home")
def home():
    return user_html

@app.route("/user")
def user():
    name = request.args.get("name")
    age = request.args.get("age")
    hobbies = request.args.get("hobbies")
    if name and age and hobbies:
        return show_html.format(name=name, age=age, hobbies=hobbies, save_message="")
    else:
        return user_html

@app.route("/save_user", methods=["POST"])
def save_user():
    name = request.form.get("name")
    age = request.form.get("age")
    hobbies = request.form.get("hobbies")
    
    if name and age and hobbies:
        user_data = {
            "name": name,
            "age": age,
            "hobbies": hobbies
        }
        
        if save_user_to_json(user_data):
            save_message = f"User '{name}' saved successfully to JSON!"
        else:
            save_message = "Error saving user data to JSON."
        
        return show_html.format(name=name, age=age, hobbies=hobbies, save_message=save_message)
    else:
        return "Error: Missing user data"

@app.route("/view_users")
def view_users():
    users = load_users_from_json()
    
    if not users:
        return """
        <h1>All Users</h1>
        <p>No users saved yet.</p>
        <a href="/home">Back to Form</a>
        """
    
    users_html = "<h1>All Users</h1><ul>"
    for user in users:
        users_html += f"<li><strong>{user['name']}</strong> - Age: {user['age']}, Hobbies: {user['hobbies']}</li>"
    users_html += "</ul><a href='/home'>Back to Form</a>"
    
    return users_html

@app.route("/show/<name>/<age>/<hobbies>")
def show(name, age, hobbies):
    return show_html.format(name=name, age=age, hobbies=hobbies, save_message="")

if __name__ == "__main__":
    app.run(debug=True)
