from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, InputRequired
from wtforms import StringField, SelectField, TextAreaField, PasswordField, DecimalField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask import render_template, request, redirect, url_for, flash

class userLogin(FlaskForm):
    username=StringField('username', validators=[DataRequired()])
    password=PasswordField('password', validators=[DataRequired()])

class userRegistration(FlaskForm):
    username=StringField('username', validators=[DataRequired()])
    password=StringField('password', validators=[DataRequired()])
    firstName=StringField('firstname', validators=[DataRequired()])
    lastName=StringField('lastname', validators=[DataRequired()])
    email=StringField('email', validators=[DataRequired(),Email()])
    location=StringField('location',validators=[DataRequired()]) 
    biography=TextAreaField('biography',validators=[DataRequired()]) 
    userPhoto=FileField('upload_photo',validators=[FileRequired(),FileAllowed(["jpg","png","Images only!"])])

class carSearch(FlaskForm):
    searchByMake = StringField('Make', validators=[InputRequired()])
    searchByModel = StringField('Model', validators=[InputRequired()])

class CarDetails(FlaskForm):
    make = StringField('Make', validators=[InputRequired()])
    model = StringField('Model', validators=[InputRequired()])
    colour = StringField('Colour', validators=[InputRequired()])
    year = StringField('Year', validators=[InputRequired()])
    price = DecimalField('Price',places=2, validators=[InputRequired()])
    carType=SelectField('Car Type' ,choices=[('SUV','SUV'),('Sports Car','Sports Car'),('Sedan','Sedan'),('Coupe','Coupe')])
    transmission=SelectField('Transmission' ,choices=[('Automatic','Automatic'),('Manual','Manual')])
    description= TextAreaField('Description', validators=[DataRequired()])
    carPhoto=FileField('Upload Photo',validators=[FileRequired(),FileAllowed(["jpg","png","Images only!")])