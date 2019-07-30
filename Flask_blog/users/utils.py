import os
import binascii
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from Flask_blog import mail

def save_picture(form_picture):
    random_hex = binascii.b2a_hex(os.urandom(15))
    root_ext = os.path.split(form_picture.filename)
    f_ext = root_ext[1]
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='jadaungeetanjali24@gmail.com', recipients=[user.email])
    msg.body = "To reset your password visit the following link: {}. If you didn't make this request then simply ignore this email and no changes will be made".format({url_for('users.reset_token', token=token, _external=True)})
    mail.send(msg)


