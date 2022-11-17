from django import forms
from tempus_dominus.widgets import DateTimePicker

from web.models import Journal, Thought, Sport, SportType, Food, HealReasons, ProsCons, ForTheBetterLife, Measurements

DateTimePickerOptions = {
    "options":{
            "useCurrent": True,
            "collapse": False,
    },
    "attrs": {
        "append": "fa fa-calendar",
        "input_toggle": False,
        "icon_toggle": True,
    },
}




class JournalForm(forms.ModelForm):
    ocurred_at = forms.DateTimeField(widget=DateTimePicker(**DateTimePickerOptions))

    class Meta:
        model = Journal
        fields = (
            "ocurred_at",
            "number_of_times",
            "situation_emotion",
            "afterwards_feeling",
        )
        labels = {"situation_emotion": "Situation/Emotion", "afterwards_feeling": "Afterwards Feeling"}


class ThoughtForm(forms.ModelForm):
    ocurred_at = forms.DateTimeField(widget=DateTimePicker(**DateTimePickerOptions))

    class Meta:
        model = Thought
        fields = ("ocurred_at", "journal", "thought")
        labels = {"thought": "Thought", "journal": "Associated Journal (Optional)"}


class SportForm(forms.ModelForm):
    ocurred_at = forms.DateTimeField(widget=DateTimePicker(**DateTimePickerOptions))

    class Meta:
        model = Sport
        fields = ("ocurred_at", "sport", "duration")
        labels = {"sport": "Sport", "duration": "Duration (minutes)"}


class SportTypeForm(forms.ModelForm):
    class Meta:
        model = SportType
        fields = ("name",)
        labels = {"name": "Sport"}


class FoodForm(forms.ModelForm):
    ocurred_at = forms.DateTimeField(widget=DateTimePicker(**DateTimePickerOptions))

    class Meta:
        model = Food
        fields = ("ocurred_at", "meal", "food", "amount")


class HealReasonsForm(forms.ModelForm):
    class Meta:
        model = HealReasons
        fields = ("reason", )


class ProsConsForm(forms.ModelForm):
    class Meta:
        model = ProsCons
        fields = ("type", "text")


class ForTheBetterLifeForm(forms.ModelForm):
    class Meta:
        model = ForTheBetterLife
        fields = ("text", )


class MeasurementsForm(forms.ModelForm):
    ocurred_at = forms.DateTimeField(widget=DateTimePicker(**DateTimePickerOptions))

    class Meta:
        model = Measurements
        fields = ("ocurred_at", "weight", "height")
