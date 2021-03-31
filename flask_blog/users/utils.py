import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flask_blog import mail
from flask import current_app

def save_pictures(form_pictures):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_pictures.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile', picture_fn)

    output_size = (125, 125)
    img = Image.open(form_pictures)
    img.thumbnail(output_size)
    img.save(picture_path)

    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='shaileshsachan1997@gmail.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request simply ignore this email and no changes will be made
'''
    mail.send(msg)