from django import forms
from django.forms import ModelForm
from .models import Genre, GameGenre, Anime, Book, Game, MovieTV, Backlog, BacklogItem, STATUS
from django.contrib.auth.models import User


#class BacklogItemGameUpdateForm(ModelForm):
#    class Meta:
#        model = BacklogItem
#        fields = ["game", "order", "status"]
#
#    #def clean(self):
#    #    order = self.cleaned_data.get("order")
#    #    plan = self.instance.plan
#    #    if BacklogItem.objects.filter(order=order).filter(plan=plan).exists():
#    #        raise forms.ValidationError("This order already exists, please try another")
#
#
##class BacklogItemAnimeUpdateForm(ModelForm):
##    class Meta:
##        model = BacklogItem
##        fields = ["anime", "order", "status"]
##
##    def clean(self):
##        order = self.cleaned_data.get("order")
##        plan = self.instance.plan
##        if BacklogItem.objects.filter(order=order).filter(plan=plan).exists():
##            raise forms.ValidationError("This order already exists, please try another")
#
#
#class BacklogItemMovieTVUpdateForm(ModelForm):
#    class Meta:
#        model = BacklogItem
#        fields = ["movie_tv", "order", "status"]
#
#    def clean(self):
#        order = self.cleaned_data.get("order")
#        plan = self.instance.plan
#        if BacklogItem.objects.filter(order=order).filter(plan=plan).exists():
#            raise forms.ValidationError("This order already exists, please try another")
#
#
#class BacklogItemBookUpdateForm(ModelForm):
#    class Meta:
#        model = BacklogItem
#        fields = ["book", "order", "status"]
#
#    def clean(self):
#        order = self.cleaned_data.get("order")
#        plan = self.instance.plan
#        if BacklogItem.objects.filter(order=order).filter(plan=plan).exists():
#            raise forms.ValidationError("This order already exists, please try another")

