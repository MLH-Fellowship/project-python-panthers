import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *

import datetime
from playhouse.shortcuts import model_to_dict
import re
load_dotenv('.env')
app = Flask(__name__)

# Below for testing

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
    )

# mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), 
# user=os.getenv("MYSQL_USER"),
# password=os.getenv("MYSQL_PASSWORD"), 
# host=os.getenv("MYSQL_HOST"),
# port=3306)

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb
mydb.connect()
mydb.create_tables([TimelinePost])


@app.route('/')
def index():
    return render_template('/main/index.html', title="Python Panthers Portfolio", url=os.getenv("URL"))

@app.route('/hobbies-josh')
def hobbiesJosh():
    return render_template('/hobbies.html', person = "Josh's Hobbies", hobby1 = "Video Games", hobby1des = "Josh likes to play video games like Lost Ark.", img1 = "./static/img/Lost Ark.png", hobby2 = "Sneakers", hobby2des = "He's also into sneakers. One of his favorites is the Jordan 3 Red Cemment shown below.", img2 = "./static/img/Jordan3.jpg" , hobby3 = "PC Builds", hobby3des = "Additionally, he also likes to research computer components and put them together. Below is a picture of the insides of a PC he be built for his parents with one of his brothers.", img3 = "./static/img/Pc build.jpg" , url=os.getenv("URL"))

@app.route('/hobbies-jul')
def hobbiesJuli():
    return render_template('/hobbies.html', person = "Juli's Hobbies", hobby1 = "Skiing", hobby1des = "One of Juli's hobbies is skiing." , img1 = "./static/img/Woman Skiing.jpg" , hobby2 = "Hiking", hobby2des = "Another one of Juli's hobbies is hiking.", img2 = "./static/img/Woman Hiking.jpg" , hobby3 = "Kdrama", hobby3des = "On top of that Juli likes to watch Kdrama as well." , img3 = "./static/img/Kdrama.png",  url=os.getenv("URL"))


@app.route('/hobbies-maansi')
def hobbiesMaansi():
    return render_template('/hobbies.html', person = "Maansi's Hobbies", hobby1 = "Cooking", hobby1des = "One of the things Maansi likes to do is cook." , img1 = "./static/img/Cooking.webp" , hobby2 = "Painting", hobby2des = "Another thing Maansi likes to do is create paintings." , img2 = "./static/img/Painting.jpg" , hobby3 = "Stranger Things", hobby3des = "Lastly, Maansi likes to watch shows like Stranger Things.", img3 = "/static/img/Stranger Things.webp" ,  url=os.getenv("URL"))




@app.route('/work-josh')
def workJosh():
    return render_template('work.html', company ="Cooper Safety Supply", role = "Warehouse Production Assistant", task = " He was responsible for assisting in production based tasks around the warehouse. These tasks included but were not limited to unpacking and packing up items, staging hard hats and other gear for production, heat pressing logos onto gloves, creating boxes to store items, and labeling items for shipping and loading them unto vehicles.",  url=os.getenv("URL"))

@app.route('/work-jul')
def workJuli():
    return render_template('work.html', company = "Stocate", role = "Full Stack Developer Volunteer", task = "- Frontend development based on React, code gosted on Github, web server running on Google cloud.", task2 = "- Took part in stocate.com project, a sustainability focused online browsing platform responsible for implementation and testing.", url=os.getenv("URL"))

@app.route('/work-maansi')
def workMaansi():
    return render_template('work.html', company = "Atlas Digital",role = "Tech Consultant", task = "Developed an open source project in Python to predict housing prices with about 90% accuracy using machine learning.", url=os.getenv("URL"))





@app.route('/jul-travel')
def julTravel():
    return render_template('/juliette/jul-travel.html', url=os.getenv("URL"))

@app.route('/maansi-travel')
def manTravel():
    return render_template('/maansi/maansi-travel.html', url=os.getenv("URL"))

@app.route('/joshua-travel')
def joshTravel():
    return render_template('/joshua/josh-travel.html', url=os.getenv("URL"))




@app.route('/jul-education')
def julEducation():
    return render_template('education.html', uni="McGill University", fact="My school just celebrated its bicentennial", pic1='/img/mcgill1.jpg',pic2='img/mcgill.jpeg', map="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2796.2627839218294!2d-73.57933978516613!3d45.50478843875644!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cc91a46510f9635%3A0xdde4da9200a4ae74!2sMcGill%20University!5e0!3m2!1sen!2sca!4v1654372237772!5m2!1sen!2sca",url=os.getenv("URL"))

@app.route('/josh-education')
def joshEducation():
    return render_template('education.html', uni="Metropolitan State University", fact="For my first 2 years of college I attended North Hennepin Community College", pic1='/img/metro-state1.jpg',pic2='img/metro-state2.jpg', map="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3357.5282368703533!2d-93.07554216879792!3d44.95721633625194!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87f7d561be333d1b%3A0xc6e9943893ee45fb!2sMetropolitan%20State%20University!5e0!3m2!1sen!2sca!4v1654398613843!5m2!1sen!2sca",url=os.getenv("URL"))

@app.route('/maansi-education')
def manEducation():
    return render_template('education.html', uni="University of Michigan", fact="I went to Novi High School in Novi, MI", pic1='/img/u-mich.jpg',pic2='img/u-mich2.jpg', map="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2952.0224758585864!2d-83.74041278454628!3d42.278043579192584!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x883cae38e7de1701%3A0x5ba14e5178e997e3!2sUniversity%20of%20Michigan!5e0!3m2!1sen!2sca!4v1654400474561!5m2!1sen!2sca",url=os.getenv("URL"))

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    
    if "name" not in request.form:
        return "Invalid name", 400
    else:
        name = request.form['name']
        if name == "":
            return "Invalid name", 400

    if "content" not in request.form:
        return "Invalid content", 400
    else:
        content = request.form['content']
        if content == "":
            return "Invalid content", 400

    if "email" not in request.form:
        return "Invalid email", 400
    else:
        email = request.form['email']
        if email == "" or not re.match(r"[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z]+", email):
            return "Invalid email", 400
    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in 
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")
