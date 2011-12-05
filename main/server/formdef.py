from django import forms
from django.core.exceptions import ValidationError
from main.server import const
import string

P_TITLE, P_CONTENT, P_TAG = 'Post title', 'Post content', 'tag1'

def validate_integer(value):
    try:
        int(value)
    except (ValueError, TypeError), e:
        raise ValidationError('')

def valid_tag(text):
    "Validates form input for tags"
    
    if not(text):
        raise ValidationError('Please enter at least one tag')

    if text == P_TAG:
        raise ValidationError('Please change the default tag')
    
    words = text.split()
    if len(words) > 5:
        raise ValidationError('You have too many tags, please use at most five tags')
    
    for word in words:
        if len(word) < 3:
            raise ValidationError("Tag '%s' is too short, use at least 3 characters" % word)
        if len(word) > 16:
            raise ValidationError("Tag '%s' is too long, use no more than 16 characters" % word)

def valid_title(text):
    "Validates form input for title"
    if text == P_TITLE:
        raise ValidationError('Please change the default title.')
    if len(text) < 5 :
        raise ValidationError('Your title appears to be shorter than the minimum of five characters.')
    if len(text) > 100 :
        raise ValidationError('Your title appears to be longer than the maximum of 100 characters.')

def valid_content(text):
    "Validates form input for content"
    if not(text.strip()):
        raise ValidationError('Content appears to be whitespace')
    if text == P_CONTENT:
        raise ValidationError('Please change the default content')
    if len(text) < 15 :
        raise ValidationError('Your content appears to be shorter than the minimum of fifteen characters.')
    if len(text) > 5000 :
        raise ValidationError('Your content  appears to be longer than the maximum of five thousand characters.')
  
class PostForm(forms.Form):
    """
    A form representing a new question
    """
    error_css_class = 'error'
    required_css_class = 'required'

    title = forms.CharField(max_length=250,  initial=P_TITLE, validators=[ valid_title ],
        widget=forms.TextInput(attrs={'style':'width:700px;'}))
    
    content = forms.CharField(max_length=5000, initial=P_CONTENT, validators=[ valid_content ], 
        widget=forms.Textarea(attrs={'cols':'80', 'rows':'15', 'id':'editor'}))

    tag_string = forms.CharField(max_length=250,  initial=P_TAG, validators=[ valid_tag ], 
        widget=forms.TextInput(attrs={'style':'width:700px;'}))
    
    post_type = forms.ChoiceField(choices=const.POST_TYPES[:1])

class ContentForm(forms.Form):
    """
    A form representing the body of simpler content answer/comment
    """
    content  = forms.CharField(max_length=5000, validators=[ valid_content ],
        widget=forms.Textarea(attrs={'cols':'80', 'rows':'15', 'id':'editor'}))

