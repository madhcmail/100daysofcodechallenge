from flask import Flask, request, jsonify
from program import db, app, Blogpost
from datetime import datetime
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

    return "successful"



if __name__ == '__main__':
    app.run(debug=True)

