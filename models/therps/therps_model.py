"""
.. module:: therps_model
   :synopsis: A useful module indeed.
"""

import logging
from REST import auth_s3, rest_funcs
logger = logging.getLogger('therps model')
import json
import os
import requests

# Set HTTP header
http_headers = auth_s3.setHTTPHeaders()
url_part1 = os.environ['UBERTOOL_REST_SERVER']


#food intake for birds
class therps(object):
    def __init__(self, run_type, chem_name, use, formu_name, a_i, h_l, n_a, i_a, a_r, avian_ld50, avian_lc50, avian_NOAEC, avian_NOAEL, 
                 Species_of_the_tested_bird_avian_ld50, Species_of_the_tested_bird_avian_lc50, Species_of_the_tested_bird_avian_NOAEC, Species_of_the_tested_bird_avian_NOAEL,
                 bw_avian_ld50, bw_avian_lc50, bw_avian_NOAEC, bw_avian_NOAEL,
                 mineau_scaling_factor, bw_herp_a_sm, bw_herp_a_md, bw_herp_a_lg, wp_herp_a_sm, wp_herp_a_md, 
                 wp_herp_a_lg, c_mamm_a, c_herp_a):
        self.jid = rest_funcs.gen_jid()
        self.run_type = run_type
        self.chem_name = chem_name
        self.use = use
        self.formu_name = formu_name
        self.a_i = a_i
        self.a_i_disp = 100*a_i
        self.h_l = h_l
        self.n_a = n_a
        self.i_a = i_a
        self.a_r = a_r
        self.avian_ld50 = avian_ld50
        self.avian_lc50 = avian_lc50
        self.avian_NOAEC = avian_NOAEC
        self.avian_NOAEL = avian_NOAEL
        self.Species_of_the_tested_bird_avian_ld50=Species_of_the_tested_bird_avian_ld50
        self.Species_of_the_tested_bird_avian_lc50=Species_of_the_tested_bird_avian_lc50
        self.Species_of_the_tested_bird_avian_NOAEC=Species_of_the_tested_bird_avian_NOAEC
        self.Species_of_the_tested_bird_avian_NOAEL=Species_of_the_tested_bird_avian_NOAEL
        self.bw_avian_ld50=bw_avian_ld50
        self.bw_avian_lc50=bw_avian_lc50
        self.bw_avian_NOAEC=bw_avian_NOAEC
        self.bw_avian_NOAEL=bw_avian_NOAEL
        self.mineau_scaling_factor = mineau_scaling_factor
        self.bw_herp_a_sm = bw_herp_a_sm
        self.bw_herp_a_md = bw_herp_a_md
        self.bw_herp_a_lg = bw_herp_a_lg
        self.wp_herp_a_sm = wp_herp_a_sm
        self.wp_herp_a_md = wp_herp_a_md
        self.wp_herp_a_lg = wp_herp_a_lg
        self.c_mamm_a = c_mamm_a
        self.c_herp_a = c_herp_a

        all_dic = {"chem_name":chem_name, "use":use, "formu_name":formu_name, "a_i":a_i, "h_l":h_l, "n_a":n_a, "i_a":i_a, "a_r":a_r, "avian_ld50":avian_ld50, "avian_lc50":avian_lc50, 
                   "avian_NOAEC":avian_NOAEC, "avian_NOAEL":avian_NOAEL, "Species_of_the_tested_bird_avian_ld50":Species_of_the_tested_bird_avian_ld50, "Species_of_the_tested_bird_avian_lc50":Species_of_the_tested_bird_avian_lc50, 
                   "Species_of_the_tested_bird_avian_NOAEC":Species_of_the_tested_bird_avian_NOAEC, "Species_of_the_tested_bird_avian_NOAEL":Species_of_the_tested_bird_avian_NOAEL, "bw_avian_ld50":bw_avian_ld50, 
                   "bw_avian_lc50":bw_avian_lc50, "bw_avian_NOAEC":bw_avian_NOAEC, "bw_avian_NOAEL":bw_avian_NOAEL, "mineau_scaling_factor":mineau_scaling_factor, "bw_herp_a_sm":bw_herp_a_sm, "bw_herp_a_md":bw_herp_a_md, 
                   "bw_herp_a_lg":bw_herp_a_lg, "wp_herp_a_sm":wp_herp_a_sm, "wp_herp_a_md":wp_herp_a_md, "wp_herp_a_lg":wp_herp_a_lg, "c_mamm_a":c_mamm_a, "c_herp_a":c_herp_a}
        data = json.dumps(all_dic)

        self.jid = rest_funcs.gen_jid()
        url=url_part1 + '/therps/' + self.jid 
        response = requests.post(url, data=data, headers=http_headers, timeout=60)
        output_val = json.loads(response.content, cls=rest_funcs.NumPyDecoder)['result']
        output_val_uni=json.loads(output_val, cls=rest_funcs.NumPyDecoder)
        for key, value in output_val_uni.items():
            setattr(self, key, value)