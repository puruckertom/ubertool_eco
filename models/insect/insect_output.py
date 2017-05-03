"""
.. module:: insect_output
   :synopsis: A useful module indeed.
"""

from django.views.decorators.http import require_POST


@require_POST
def insectOutputPage(request):
    import insect_model

    chemical_name = request.POST.get('chemical_name')
   # select_receptor = request.POST.get('select_receptor')
   # bw_bird = request.POST.get('body_weight_of_bird')
   # bw_mamm = request.POST.get('body_weight_of_mammal')
    sol = request.POST.get('solubility')
    ld50_a = request.POST.get('ld50_a')
    ld50_m = request.POST.get('ld50_m')
    aw_bird = request.POST.get('aw_bird')
    # tw_bird = request.POST.get('body_weight_of_the_tested_bird')
    aw_mamm = request.POST.get('aw_mamm')
    # tw_mamm = request.POST.get('body_weight_of_the_tested_mammal')
    mineau = request.POST.get('mineau_scaling_factor')
    noael = request.POST.get('NOAEL')
    noaec_d = request.POST.get('NOAEC_d')
    noaec_q = request.POST.get('NOAEC_q')
    noaec_o = request.POST.get('NOAEC_o')
    # noaec_o2 = request.POST.get('NOAEC_o2')
    Species_of_the_bird_NOAEC_CHOICES = request.POST.get('NOAEC_species')
    bw_quail = request.POST.get('bw_quail')
    bw_duck = request.POST.get('bw_duck')
    bwb_other = request.POST.get('bwb_other')
    bw_rat = request.POST.get('bw_rat')
    bwm_other = request.POST.get('bwm_other')
    b_species = request.POST.get('b_species')
    m_species = request.POST.get('m_species')

    insect_obj = insect_model.insect(True,True,'single',chemical_name, b_species, m_species, bw_quail, bw_duck, bwb_other, bw_rat, bwm_other, sol, ld50_a, ld50_m, aw_bird, mineau, aw_mamm, noaec_d, noaec_q, noaec_o, Species_of_the_bird_NOAEC_CHOICES, noael)

    return insect_obj