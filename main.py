from flask import Flask, render_template, redirect, url_for
import requests
from post import Post

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_list = []
for post in posts:
    post_obj = Post(int(post["id"]), post["title"],post["subtitle"],post["body"])
    post_list.append(post_obj)

app = Flask(__name__)

@app.route('/blog')
def home():
    return render_template("index.html", data=post_list)

@app.route('/post/<int:index>')
def post_blog(index):
    requested_post = None
    for item in post_list:
       if item.post_id == index:
           requested_post = item 
    return render_template('post.html', post=requested_post)
    
if __name__ == "__main__":
    app.run(debug=True)
