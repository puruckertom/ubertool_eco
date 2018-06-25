"""
.. module:: leslie_probit_parameters
   :synopsis: A useful module indeed.
"""
from django import forms
from django.utils.safestring import mark_safe
from pram_app.models.forms import validation


app_target_choices=(('Short Grass','Short Grass'),('Tall Grass','Tall Grass'))
S_select = (('', 'Please choose'), ('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'))


class Leslie_probit_Chemical(forms.Form):
    animal_name = forms.CharField(widget=forms.Textarea (attrs={'cols': 17, 'rows': 2}), initial='C. dubia')    
    chemical_name = forms.CharField(widget=forms.Textarea (attrs={'cols': 17, 'rows': 2}), initial='Spinosad')
    app_target = forms.ChoiceField(required=True, choices=app_target_choices, initial='Short Grass')
    ai = forms.FloatField(required=True, label='% a.i. (%)', initial=41.9)
    hl = forms.FloatField(required=True, label='Chemical half life (days)',initial=2)
    sol = forms.FloatField(required=True, label=mark_safe('Solubility (in water @25&deg;C; mg/L)'), initial=70)
    t = forms.FloatField(required=True, label='Simulation durations (days)',initial=10)


class Leslie_probit_DoseResponse(forms.Form):
    b = forms.FloatField(required=True, label=mark_safe('Probit dose response slope (b)'), initial=4.5)
    test_species = forms.CharField(widget=forms.Textarea (attrs={'cols': 17, 'rows': 1}), label='Tested animal', initial='Quail')
    ld50_test = forms.FloatField(required=True, label=mark_safe('LD<sub>50</sub> of tested animal (mg/kg-bw)'),initial=783)

    bw_test=forms.FloatField(required=True, label='Body weight of the tested animal (g)', initial=178)
    ass_species = forms.CharField(widget=forms.Textarea (attrs={'cols': 17, 'rows': 1}), label='Assessed animal', initial='Turkey')
    bw_ass = forms.FloatField(required=True, label='Body weight of assessed animal (g)', initial=20)
    mineau_scaling_factor = forms.FloatField(required=True, label='Mineau scaling factor', initial=1.15)


class Leslie_probit_LeslieMatrix(forms.Form):
    c = forms.FloatField(required=True,label=mark_safe('Intensity of the density dependence (&#947;)'),initial=0.00548)   
    s = forms.ChoiceField(required=True,choices=S_select, label='Number of age class', initial='Please choose')


# Combined Form Classes for Validation
class Leslie_ProbitInp(Leslie_probit_Chemical, Leslie_probit_DoseResponse, Leslie_probit_LeslieMatrix):
    pass
