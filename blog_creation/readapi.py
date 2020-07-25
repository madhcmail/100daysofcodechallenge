from flask import Flask, request, jsonify
from program import db, app, Blogpost
from flask_sqlalchemy import SQLAlchemy


@app.route('/getposts', methods=['GET'])
def getPosts():
    query_results = Blogpost.query.all()

    posts = []
    for post in query_results:
        posts.append({'id':post.id, 'title':post.title, 'subtitle':post.sub_title,'author':post.author,
                      'date_posted': post.date_posted,'content': post.content })
    return jsonify({'Posts':posts})


if __name__ == '__main__':
    app.run(debug=True)

