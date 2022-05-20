from django.forms import ModelForm
from .models import Skills, Value_skill, Skill


# class SkillForm(ModelForm):
#     class Meta:
#         model = Value_skill
#         fields = ['to_tag_skill', 'value',]


class AddSkill(ModelForm):
    class Meta:
        model = Skill
        fields = ['tag_skill',]




class SkillForm(ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})