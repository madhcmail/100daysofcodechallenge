from flask import Flask, request, jsonify
from program import db, app, Blogpost
from datetime import datetime
import json
from flask_sqlalchemy import SQLAlchemy



@app.route('/getposts', methods=['GET'])
def getPosts():
    query_results = Blogpost.query.all()

    posts = []
    for post in query_results:
        posts.append({'id':post.id, 'title':post.title, 'subtitle':post.sub_title,'author':post.author,
                      'date_posted': post.date_posted,'content': post.content })
    return jsonify({'Posts':posts})


@app.route('/addposts', methods=['POST'])
def addposts():

    data = request.get_json()

    for post in data:
     # new_post = Blogpost(title = request.json['title'],sub_title = request.json['sub_title'],
     #                   author = request.json['author'],date_posted = datetime.now() ,
      #                  content= request.json['content'])'''
        new_post = Blogpost(title=post['title'], sub_title=post['subtitle'], author=post['author'],
                            date_posted=datetime.now(), content=post['content'])

        db.session.add(new_post)
        db.session.commit()


@app.route('/postjson', methods=['POST'])
def postjson():
    print("started reading Json file")
    with open('mul_postdata.json', "r") as read_file:
        print("Converting JSON encoded data into Python dictionary")
        data = json.load(read_file)
        print(data)
    for post in data['posts']:
        print(post)
        new_post = Blogpost(title=post['title'], sub_title=post['sub_title'], author=post['author'],
                            date_posted=datetime.now(), content=post['content'])
        db.session.add(new_post)
        db.session.commit()


@app.route('/lang<int:id>', methods = ['DELETE'])
def removeOne(id):

    return "successful"



if __name__ == '__main__':
    app.run(debug=True)

