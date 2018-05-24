# coding=utf8
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from ..models import Role, User
from flask_wtf.file import FileField, FileRequired, FileAllowed
from ..import photos


class DownloadForm(FlaskForm):
    class_name = SelectField(u"课程", choices=[(u'组网工程', u'组网工程'), (u'网络安全', u'网络安全'), ('linux', 'linux')])
    test_num = SelectField(u'实验号', choices=[(u'实验一', u'实验一'), (u'实验二', u'实验二'), (u'实验三', u'实验三'), (u'实验四', u'实验四'), (u'实验五', u'实验五'),
                                             (u'实验六', u'实验六'), (u'实验七', u'实验七'), (u'实验八', u'实验八'), (u'实验九', u'实验九'), (u'实验十', u'实验十')])

    submit = SubmitField(u'查看')


class UploadForm(FlaskForm):
    class_name = SelectField(u"课程", choices=[(u'组网工程', u'组网工程'), (u'网络安全', u'网络安全'), ('linux', 'linux')])
    test_num = SelectField(u'实验号', choices=[(u'实验一', u'实验一'), (u'实验二', u'实验二'), (u'实验三', u'实验三'), (u'实验四', u'实验四'),
                                             (u'实验五', u'实验五'), (u'实验六', u'实验六'), (u'实验七', u'实验七'), (u'实验八', u'实验八'), (u'实验九', u'实验九'),
                                             (u'实验十', u'实验十')])
    stu_id = StringField(u'学号', validators=[Length(0, 12)])
    stu_name = StringField(u'姓名', validators=[Length(0, 12)])
    photo = FileField('File', validators=[
        FileAllowed(photos, 'just file'),
        FileRequired('no file !')])
    submit = SubmitField(u'提交')


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class PostForm(FlaskForm):
    body = PageDownField("What's on your mind?", validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    body = StringField('Enter your comment', validators=[Required()])
    submit = SubmitField('Submit')
