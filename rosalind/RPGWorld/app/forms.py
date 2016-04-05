from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required

class DnevnikForm(Form):
    default_form = "None"
    openid = TextAreaField('Text', validators = [Required()], default = "")
    #remember_me = BooleanField('remember_me', default = False)
    def change_def(self, text):
        self.default_form = text
        print self.default_form

class TrenForm(Form):
    default_form = "None"
    openid = TextAreaField('Text', validators = [Required()], default = "")
    #remember_me = BooleanField('remember_me', default = False)
    def change_def(self, text):
        self.default_form = text
        print self.default_form
