from django import forms
from contests.models import Djoin

class JoinFrom(forms.ModelForm):
    class Meta:
        model=Djoin
        fields=['team_name','leader_pname','second_pname','second_pname','third_pname','fourth_pname','fifth_pname','whats_num','email','pay_ss','team_logo']
        labels={
            'team_name':'Team Name*',
            'leader_pname':'Team Leader Name / First Player*',
            'second_pname':'Second Player Name*',
            'third_pname':'Third Player Name*',
            'fourth_pname':'Fourth Player Name*',
            'fifth_pname':'Fifth Player Name*',
            'whats_num':'WhatsApp Number*',
            'email':'Email ID',
            'pay_ss':'Payment Bill Screensort*',
            'team_logo':'Team Logo Image',
        }
        widgets={
            'team_name':forms.TextInput(attrs={'class':'form-control','placeholder':'your team name'}),
            'leader_pname':forms.TextInput(attrs={'class':'form-control','placeholder':'your team leader name'}),
            'second_pname':forms.TextInput(attrs={'class':'form-control','placeholder':'your 2nd player name'}),
            'third_pname':forms.TextInput(attrs={'class':'form-control','placeholder':'your 3rd player name'}),
            'fourth_pname':forms.TextInput(attrs={'class':'form-control','placeholder':'your 4th player name'}),
            'fifth_pname':forms.TextInput(attrs={'class':'form-control','placeholder':'your 5th player name'}),
            'whats_num':forms.TextInput(attrs={'class':'form-control','placeholder':'your whatsapp number','pattern':'^\d{10}$'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'your email id'}),
        }