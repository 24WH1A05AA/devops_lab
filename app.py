
from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        db = mysql.connector.connect(
            host="localhost",
            user="flaskuser",
            password="1234",
            database="eventdb"
        )

        cur = db.cursor()
        cur.execute(
            "INSERT INTO users VALUES (%s, %s)",
            (name, email)
        )
        db.commit()
        db.close()

        return "Registration Successful!"

    return """
    <h2>Event Registration Form</h2>
    <form method="POST">
        Name: <input name="name"><br><br>
        Email: <input name="email"><br><br>
        <input type="submit" value="Register">
    </form>
    """

app.run(debug=True)

mysql -u root -p

CREATE DATABASE eventdb;

USE eventdb;

CREATE TABLE users (
    name VARCHAR(50),
    email VARCHAR(50)
);

python app.py


git --version

sudo apt purge git -y

sudo apt autoremove -y

sudo apt update

sudo apt install git -y

git --version

git config --global user.name "Your Name"

git config --global user.email "your_email@gmail.com"

git config --list




from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Docker Container is Running Successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]


docker build -t my-flask-app .

docker run -d -p 8080:5000 --name mycontainer my-flask-app




package com.example.prac1;
import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication
@RestController
public class Prac1Application {
    
    public static void main(String[] args) {
		SpringApplication.run(Prac1Application.class, args);
	}
    @GetMapping("/")
    public String home(){
        return "Hello";
    }


    @GetMapping("/home")
    public String second(){
        return "Hello  second ";
    }
}

Feature: Javascript script

  Scenario: Addition
    * def add = function(a,b) { return a+b }
    * match add(10,20) == 30

  Scenario: Subtraction
    * def sub = function(a,b) { return a-b }
    * match sub(20,10) == 10
