"""
.. module:: insect_batchoutput
   :synopsis: A useful module indeed.
"""

import Queue
import csv
import logging
from collections import OrderedDict
from threading import Thread

from django.views.decorators.http import require_POST

import insect_model
import insect_tables

logger = logging.getLogger("InsectBatchOutput")

chemical_name=[]
b_species=[]
m_species=[]
bw_quail=[]
bw_duck=[]
bwb_other=[]
bw_rat=[]
bwm_other=[]
avian_ld50=[]
mammalian_ld50=[]
sol=[]
aw_bird=[]
mineau=[]
aw_mamm=[]
noaec_d=[]
noaec_q=[]
noaec_o=[]
noael=[]
Species_of_the_bird_NOAEC_CHOICES=[]
noaec=[]

######Pre-defined outputs########
dose_bird_out = []
dose_mamm_out = []
at_bird_out = []
at_mamm_out = []
det_out = []
act_out = []
acute_bird_out = []
acuconb_out = []
acute_mamm_out = []
acuconm_out = []
chron_bird_out = []
chronconb_out = []
chron_mamm_out = []
chronconm_out = []

jid_all = []
jid_batch = []
insect_all = []
all_threads = []
out_html_all = {}
job_q = Queue.Queue()
thread_count = 10


def html_table(row_inp_all):
    while True:
        row_inp_temp_all = row_inp_all.get()
        if row_inp_temp_all is None:
            break
        else:
            row_inp = row_inp_temp_all[0]
            iter = row_inp_temp_all[1]

            logger.info("iteration: " + str(iter))
            chemical_name.append(str(row_inp[0]))
            b_species.append(float(row_inp[1]))
            m_species.append(float(row_inp[2]))
            bw_quail.append(float(row_inp[3]))
            bw_duck.append(float(row_inp[4]))
            bwb_other.append(float(row_inp[5])) 
            bw_rat.append(float(row_inp[6]))
            bwm_other.append(float(row_inp[7]))
            sol.append(float(row_inp[8]))
            avian_ld50.append(float(row_inp[9])) 
            mammalian_ld50.append(float(row_inp[10]))
            aw_bird.append(float(row_inp[11]))
            mineau.append(float(row_inp[12]))
            aw_mamm.append(float(row_inp[13]))
            noaec_d.append(float(row_inp[14]))
            noaec_q.append(float(row_inp[15]))
            noaec_o.append(float(row_inp[16]))
            noael.append(float(row_inp[17]))
            Species_of_the_bird_NOAEC_CHOICES.append(str(row_inp[18]))
            if Species_of_the_bird_NOAEC_CHOICES[iter] == '1':
                noaec.append(float(row_inp[14]))
            elif Species_of_the_bird_NOAEC_CHOICES[iter] == '2':
                noaec.append(float(row_inp[15]))
            elif Species_of_the_bird_NOAEC_CHOICES[iter] == '3':
                noaec.append(float(row_inp[16]))

            logger.info(chemical_name)
            logger.info(b_species)
            logger.info(m_species)
            logger.info(bw_quail)
            logger.info(bw_duck)
            logger.info(bwb_other)
            logger.info(bw_rat)
            logger.info(bwm_other)
            logger.info(sol)
            logger.info(avian_ld50)
            logger.info(mammalian_ld50)
            logger.info(aw_bird)
            logger.info(mineau)
            logger.info(aw_mamm)
            logger.info(noaec_d)
            logger.info(noaec_q)
            logger.info(noaec_o)
            logger.info(noael)
            logger.info(Species_of_the_bird_NOAEC_CHOICES)

            insect_obj = insect_model.insect(True,True,'batch',chemical_name[iter], b_species[iter], m_species[iter], bw_quail[iter],
                            bw_duck[iter], bwb_other[iter], bw_rat[iter], bwm_other[iter], sol[iter], avian_ld50[iter],
                            mammalian_ld50[iter], aw_bird[iter], mineau[iter], aw_mamm[iter], noaec_d[iter], noaec_q[iter], noaec_o[iter], Species_of_the_bird_NOAEC_CHOICES[iter], noael[iter])

            dose_bird_out.append(insect_obj.dose_bird_out)
            dose_mamm_out.append(insect_obj.dose_mamm_out)
            at_bird_out.append(insect_obj.at_bird_out)
            at_mamm_out.append(insect_obj.at_mamm_out)
            det_out.append(insect_obj.det_out)
            act_out.append(insect_obj.act_out)
            acute_bird_out.append(insect_obj.acute_bird_out)
            acuconb_out.append(insect_obj.acuconb_out)
            acute_mamm_out.append(insect_obj.acute_mamm_out)
            acuconm_out.append(insect_obj.acuconm_out)
            chron_bird_out.append(insect_obj.chron_bird_out)
            chronconb_out.append(insect_obj.chronconb_out)
            chron_mamm_out.append(insect_obj.chron_mamm_out)
            chronconm_out.append(insect_obj.chronconm_out)

            jid_all.append(insect_obj.jid)
            insect_all.append(insect_obj)    
            if iter == 0:
                jid_batch.append(insect_obj.jid)

            batch_header = """
                <div class="out_">
                    <br><H3>Batch Calculation of Iteration %s:</H3>
                </div>
                """%(iter + 1)

            out_html_temp = batch_header + insect_tables.table_all(insect_obj)
            out_html_all[iter]=out_html_temp

def loop_html(thefile):
    reader = csv.reader(thefile.file.read().splitlines())
    header = reader.next()
    # logger.info(header)
    i=0
    iter_html=""
    for row in reader:
        job_q.put([row, i])
        i=i+1

    all_threads = [Thread(target=html_table, args=(job_q, )) for j in range(thread_count)]
    for x in all_threads:
        x.start()
    for x in all_threads:
        job_q.put(None)
    for x in all_threads:
        x.join()

    html_timestamp = insect_tables.timestamp("", jid_batch[0])
    out_html_all_sort = OrderedDict(sorted(out_html_all.items()))
    sum_html = insect_tables.table_all_sum(insect_tables.sumheadings, insect_tables.tmpl, bw_quail,bw_duck,bwb_other,bw_rat,bwm_other,sol,
                    avian_ld50,mammalian_ld50,aw_bird,mineau,aw_mamm,noaec,noael,
                    dose_bird_out, dose_mamm_out, at_bird_out, 
                    at_mamm_out, det_out, act_out, acute_bird_out, acute_mamm_out, 
                    chron_bird_out, chron_mamm_out)

    return html_timestamp + sum_html + "".join(out_html_all_sort.values())


@require_POST
def insectBatchOutputPage(request):
    thefile = request.FILES['upfile']
    iter_html=loop_html(thefile)

    return iter_html, insect_all, jid_batch