from django import forms 
from .models import Product
from .models import Comment
class SearchForm(forms.Form): 
    query = forms.CharField( 
        label='検索キーワード', 
        max_length=100, 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': '検索したい曲やアーティストを入力'})    
    ) 
 
class ProductForm(forms.ModelForm): 
    class Meta: 
        model = Product 
        fields = ['title', 'artist', 'album','youtube','apple_music','category','image_url','release_date']
        labels = {
            'title': '曲名',
            'artist': 'アーティスト',  
            'album' : 'アルバム',
            'youtube' : 'YouTubeのURL',
            'apple_music' : 'Apple MusicのURL',
            'category':'ジャンル',
            'image_url':'写真のURL',
            'release_date':'リリース日',
        }
        
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'コメント',
        }
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'この曲を聴いて思ったことなどを書いてみよう！',  # プレースホルダーの追加
                'rows': 3,  # テキストエリアの行数を指定
            }),
        }