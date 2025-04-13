# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_wtf.file import FileAllowed

# Custom validator to check if file is an image
def validate_image(form, field):
    if field.data:
        if not field.data.filename.endswith('.jpg') and not field.data.filename.endswith('.png'):
            raise ValidationError('Only JPG and PNG images are allowed.')

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[InputRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[InputRequired()])
    poster = FileField('Movie Poster', validators=[InputRequired(), FileAllowed(['jpg', 'png']), validate_image])
