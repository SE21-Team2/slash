from flask import Flask # for hosting endpoint

from user import user_bp
from search import search_bp
from wishlist import wishlist_bp

#import db

'''
        db.query(
            'INSERT INTO pinned_messages (guild_id, author_id, tag, description) VALUES (%s, %s, %s, %s)',
            (ctx.guild.id, author.id, tagname, description)
        )
'''

app = Flask(__name__)

app.register_blueprint(user_bp)
app.register_blueprint(search_bp)
app.register_blueprint(wishlist_bp)

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()