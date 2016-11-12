import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import numpy as np
import cgi
import cgitb
cgitb.enable()
import logging
import sys
sys.path.append("../utils")
import utils.json_utils
sys.path.append("../agdrift")
sys.path.append("../trex")
from agdrift import agdrift_model,agdrift_tables
from agdrift_trex import agdrift_trex_tables
from trex2 import trex2_model,trex2_tables
from uber import uber_lib
from django.template import Context, Template
from django.utils import simplejson
import logging
import rest_funcs

logger = logging.getLogger('trex Model')

def merge(ob1, ob2):
    """
    an object's __dict__ contains all its 
    attributes, methods, docstrings, etc.
    """
    ob1.__dict__.update(ob2.__dict__)
    return ob1
# merge the two class instances into one instance

class agdrift_trexOutputPage(webapp.RequestHandler):
    def post(self):        
        form = cgi.FieldStorage()   
        #print form
       # args={}
        #for keys in form:
        #    args[keys]=form.getvalue(keys)
        drop_size = form.getvalue('drop_size')
        ecosystem_type = form.getvalue('ecosystem_type')
        application_method = form.getvalue('application_method')
        boom_height = form.getvalue('boom_height')
        orchard_type = form.getvalue('orchard_type')
        # application_rate = form.getvalue('application_rate')
        aquatic_type = form.getvalue('aquatic_type')
        distance = form.getvalue('distance')
        calculation_input = form.getvalue('calculation_input')

        # init_avg_dep_foa = form.getvalue('init_avg_dep_foa')
        # avg_depo_gha = form.getvalue('avg_depo_gha')
        # avg_depo_lbac = form.getvalue('avg_depo_lbac')
        # deposition_ngL = form.getvalue('deposition_ngL')
        # deposition_mgcm = form.getvalue('deposition_mgcm')
        # nasae = form.getvalue('nasae')
        # y = form.getvalue('y')
        # x = form.getvalue('x')
        # express_y = form.getvalue('express_y')

        chem_name = form.getvalue('chemical_name')
        use = form.getvalue('Use')
        formu_name = form.getvalue('Formulated_product_name')
        a_i = form.getvalue('percent_ai')
        # print a_i
        a_i = float(a_i)/100
        Application_type = form.getvalue('Application_type')
        seed_crop = float(form.getvalue('seed_crop'))
        seed_crop_v = form.getvalue('seed_crop_v')
        p_i = form.getvalue('percent_incorporated')
        p_i = float(p_i)/100
        seed_treatment_formulation_name = form.getvalue('seed_treatment_formulation_name')
        den = form.getvalue('density_of_product')
        den = float(den)
        m_s_r_p = form.getvalue('maximum_seedling_rate_per_use')
        m_s_r_p = float(m_s_r_p)
        r_s = form.getvalue('row_sp') 
        r_s=float(r_s)
        b_w = form.getvalue('bandwidth')   #convert to ft
        b_w = float(b_w)/12

        if Application_type=='Seed Treatment':
           n_a = 1
        else:
           n_a = float(form.getvalue('noa'))
        
        rate_out = []
        day_out = [0]
        for i in range(int(n_a)):
           j=i+1
           rate_temp = form.getvalue('rate'+str(j))
           rate_out.append(float(rate_temp))
           # day_temp = float(form.getvalue('day'+str(j)))
           # day_out.append(day_temp)  
        h_l = form.getvalue('Foliar_dissipation_half_life')
        ld50_bird = form.getvalue('avian_ld50')
        lc50_bird = form.getvalue('avian_lc50')
        NOAEC_bird = float(form.getvalue('avian_NOAEC'))
        try:
            NOAEL_bird = float(form.getvalue('avian_NOAEL'))
        except:
            NOAEL_bird = 'N/A'
        aw_bird_sm = form.getvalue('body_weight_of_the_assessed_bird_small')
        aw_bird_sm = float(aw_bird_sm)  
        aw_bird_md = form.getvalue('body_weight_of_the_assessed_bird_medium')
        aw_bird_md = float(aw_bird_md) 
        aw_bird_lg = form.getvalue('body_weight_of_the_assessed_bird_large')
        aw_bird_lg = float(aw_bird_lg)       
        
        Species_of_the_tested_bird_avian_ld50 = form.getvalue('Species_of_the_tested_bird_avian_ld50')
        Species_of_the_tested_bird_avian_lc50 = form.getvalue('Species_of_the_tested_bird_avian_lc50')
        Species_of_the_tested_bird_avian_NOAEC = form.getvalue('Species_of_the_tested_bird_avian_NOAEC')
        Species_of_the_tested_bird_avian_NOAEL = form.getvalue('Species_of_the_tested_bird_avian_NOAEL')

        tw_bird_ld50 = float(form.getvalue('bw_avian_ld50'))
        tw_bird_lc50 = float(form.getvalue('bw_avian_lc50'))
        tw_bird_NOAEC = float(form.getvalue('bw_avian_NOAEC'))
        tw_bird_NOAEL = float(form.getvalue('bw_avian_NOAEL'))

        x = form.getvalue('mineau_scaling_factor')
        ld50_mamm = form.getvalue('mammalian_ld50')
        try:
            lc50_mamm = float(form.getvalue('mammalian_lc50'))
        except:
            lc50_mamm = 'N/A'
        NOAEC_mamm = form.getvalue('mammalian_NOAEC')
        NOAEC_mamm = float(NOAEC_mamm)
        NOAEL_mamm = form.getvalue('mammalian_NOAEL')

        aw_mamm_sm = form.getvalue('body_weight_of_the_assessed_mammal_small')
        aw_mamm_sm = float(aw_mamm_sm)  
        aw_mamm_md = form.getvalue('body_weight_of_the_assessed_mammal_medium')
        aw_mamm_md = float(aw_mamm_md) 
        aw_mamm_lg = form.getvalue('body_weight_of_the_assessed_mammal_large')
        aw_mamm_lg = float(aw_mamm_lg)               
        tw_mamm = form.getvalue('body_weight_of_the_tested_mammal')
        tw_mamm = float(tw_mamm) 

        agdrift_obj = agdrift_model.agdrift(True, True, 'single', drop_size, ecosystem_type, application_method, boom_height, orchard_type, rate_out[0], distance, aquatic_type, calculation_input, None)
        x_agdrif=agdrift_obj.x
        trex_obj = trex2_model.trex2('single', chem_name, use, formu_name, a_i, Application_type, seed_treatment_formulation_name, seed_crop, seed_crop_v, r_s, b_w, p_i, den, h_l, n_a, [agdrift_obj.init_avg_dep_foa*i for i in rate_out], day_out,
                                     ld50_bird, lc50_bird, NOAEC_bird, NOAEL_bird, aw_bird_sm, aw_bird_md, aw_bird_lg, 
                                     Species_of_the_tested_bird_avian_ld50, Species_of_the_tested_bird_avian_lc50, Species_of_the_tested_bird_avian_NOAEC, Species_of_the_tested_bird_avian_NOAEL,
                                     tw_bird_ld50, tw_bird_lc50, tw_bird_NOAEC, tw_bird_NOAEL, x, ld50_mamm, lc50_mamm, NOAEC_mamm, NOAEL_mamm, aw_mamm_sm, aw_mamm_md, aw_mamm_lg, tw_mamm,
                                     m_s_r_p)

        # templatepath = os.path.dirname(__file__) + '/../templates/'
        # ChkCookie = self.request.cookies.get("ubercookie")
        # html = uber_lib.SkinChk(ChkCookie, "AgDrift-TREX Output")
        # html = html + template.render(templatepath + '02uberintroblock_wmodellinks.html', {'model':'agdrift_trex','page':'output'})
        # html = html + template.render (templatepath + '03ubertext_links_left.html', {})                
        # html = html + template.render(templatepath + '04uberoutput_start.html', {
        #         'model':'agdrift_trex', 
        #         'model_attributes':'AgDrift-T-Rex Output'})

        # html = html + agdrift_trex_tables.timestamp(agdrift_obj)
        # html = html + agdrift_tables.table_all(agdrift_obj)
        # html = html + trex2_tables.table_all(trex_obj)[0]
        # html = html + template.render(templatepath + 'agdrift-output-jqplot_header.html', {})
        # html = html + template.render(templatepath + 'export.html', {})
        # html = html + template.render(templatepath + '04uberoutput_end.html', {})
        # html = html + template.render(templatepath + '06uberfooter.html', {'links': ''})



        #Note: If you need to rebuild the output page based on saved class, 
        #variables named x_agdrif and x_trex in the class agdrift_trex_obj
        #are x in their own instance (agdrift_obj.x, trex_obj.x).
        agdrift_trex_obj = merge(agdrift_obj, trex_obj)
        agdrift_trex_obj.x_agdrif=x_agdrif
        agdrift_trex_obj.x_trex=trex_obj.x
        logging.info(vars(agdrift_trex_obj))
        rest_funcs.save_dic(html, agdrift_trex_obj.__dict__, "agdrift_trex", "single")
        self.response.out.write(html)
          
app = webapp.WSGIApplication([('/.*', agdrift_trexOutputPage)], debug=True)
        
def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()

