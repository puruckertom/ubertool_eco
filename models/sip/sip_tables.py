"""
.. module:: sip_tables
   :synopsis: A useful module indeed.
"""

import numpy
from django.template import Context, Template
from django.utils.safestring import mark_safe
import logging
import time
import datetime

logger = logging.getLogger("SipTables")

def getheaderpvu():
	headings = ["Parameter", "Value", "Units"]
	return headings

def getheaderpvr():
	headings = ["Parameter", "Acute", "Chronic","Units"]
	return headings

def getheaderpvrqaqc():
    headings = ["Parameter", "Acute", "Acute-Expected", "Chronic", "Chronic-Expected","Units"]
    return headings

def getheadersum():
    headings = ["Parameter", "Mean", "Std", "Min", "Max", "Unit"]
    return headings

def gethtmlrowsfromcols(data, headings):
    columns = [data[heading] for heading in headings]

    # get the length of the longest column
    max_len = len(max(columns, key=len))

    for col in columns:
        # padding the short columns with None
        col += [None,] * (max_len - len(col))

    # Then rotate the structure...
    rows = [[col[i] for col in columns] for i in range(max_len)]
    return rows

def getdjtemplate():
    dj_template ="""
    <table class="out_">
    {# headings #}
        <tr>
        {% for heading in headings %}
            <th>{{ heading }}</th>
        {% endfor %}
        </tr>
    {# data #}
    {% for row in data %}
    <tr>
        {% for val in row %}
        <td>{{ val|default:'' }}</td>
        {% endfor %}
    </tr>
    {% endfor %}
    </table>
    """
    return dj_template

def gett1data(sip_obj):
    data = { 
        "Parameter": ['Chemical Name',mark_safe('Solubility (in water @25&deg;C)'),mark_safe('Mammalian LD<sub>50</sub>'),mark_safe('Body weight of mammalian species (LD<sub>50</sub>)'),'Mammalian NOAEL', 'Body weight of mammalian species (NOAEL)',mark_safe('Avian LD<sub>50</sub>'),'Body Weight of Tested Bird','Mineau Scaling Factor','Mallard duck NOAEC','Northern bobwhite quail NOAEC','NOAEC for other bird species','Body weight of other avian species','NOAEC for 2nd other bird species','Body weight of 2nd other avian species'],
        "Value": [sip_obj.chemical_name,sip_obj.solubility,sip_obj.ld50_mammal_water,sip_obj.bodyweight_tested_mammal,sip_obj.noael_mammal_water,sip_obj.noael_bodyweight_tested_mammal,sip_obj.ld50_avian_water,sip_obj.bodyweight_tested_bird,sip_obj.mineau_scaling_factor,sip_obj.noaec_duck,sip_obj.noaec_quail,sip_obj.noaec_bird_other_1,sip_obj.bodyweight_bird_other_1,sip_obj.noaec_bird_other_2,sip_obj.bodyweight_bird_other_2],
        "Units": ['','mg/L','mg/kg-bw','g','mg/kg-bw','g','mg/kg-bw','g','','mg/kg-diet','mg/kg-diet','mg/kg-diet','g','mg/kg-diet','g'],
    }
    return data

def gett2data(sip_obj):
    data = { 
        "Parameter": ['Upper Bound Exposure', 'Adjusted Toxicity Value', 'Ratio of Exposure to Toxicity', 'Conclusion',],
        "Acute": ['%g' % sip_obj.dose_mamm_out, '%g' % sip_obj.at_mamm_out, '%g' % sip_obj.acute_mamm_out, '%s' % sip_obj.acuconm_out,],
        "Chronic": ['%g' % sip_obj.dose_mamm_out, '%g' % sip_obj.act_out, '%g' % sip_obj.chron_mamm_out, '%s' % sip_obj.chronconm_out,],
        "Units": ['mg/kg-bw', 'mg/kg-bw', '', '',],
    }
    return data

def gett2dataqaqc(sip_obj):
    data = { 
        "Parameter": ['Upper Bound Exposure', 'Adjusted Toxicity Value', 'Ratio of Exposure to Toxicity', 'Conclusion',],
        "Acute": ['%g' % sip_obj.dose_mamm_out, '%g' % sip_obj.at_mamm_out, '%g' % sip_obj.acute_mamm_out, '%s' % sip_obj.acuconm_out,],
        "Acute-Expected": ['%g' % sip_obj.dose_mamm_exp,'%g' % sip_obj.at_mamm_exp,'%g' % sip_obj.acute_mamm_exp,'%s' % sip_obj.acuconm_exp,],
        "Chronic": ['%g' % sip_obj.dose_mamm_out, '%g' % sip_obj.act_out, '%g' % sip_obj.chron_mamm_out, '%s' % sip_obj.chronconm_out,],
        "Chronic-Expected": ['%g' % sip_obj.dose_mamm_exp,'%g' % sip_obj.act_exp,'%g' % sip_obj.chron_mamm_exp,'%s' % sip_obj.chronconm_exp,],
        "Units": ['mg/kg-bw', 'mg/kg-bw', '', '',],
    }
    return data

def gett3data(sip_obj):
    data = { 
        "Parameter": ['Upper Bound Exposure', 'Adjusted Toxicity Value', 'Ratio of Exposure to Toxicity', 'Conclusion',],
        "Acute": ['%g' % sip_obj.dose_bird_out, '%g' % sip_obj.at_bird_out,'%g' % sip_obj.acute_bird_out, '%s' % sip_obj.acuconb_out,],
        "Chronic": ['%g' % sip_obj.dose_bird_out, '%g' % sip_obj.det_out,'%g' % sip_obj.chron_bird_out, '%s' % sip_obj.chronconb_out,],
        "Units": ['mg/kg-bw', 'mg/kg-bw', '', '',],
    }
    return data

def gett3dataqaqc(sip_obj):
    data = { 
        "Parameter": ['Upper Bound Exposure', 'Adjusted Toxicity Value', 'Ratio of Exposure to Toxicity', 'Conclusion',],
        "Acute": ['%g' % sip_obj.dose_bird_out, '%g' % sip_obj.at_bird_out,'%g' % sip_obj.acute_bird_out, '%s' % sip_obj.acuconb_out,],
        "Acute-Expected": ['%g' % sip_obj.dose_bird_exp, '%g' % sip_obj.at_bird_exp, '%g' % sip_obj.acute_bird_exp, '%s' % sip_obj.acuconb_exp,],
        "Chronic": ['%g' % sip_obj.dose_bird_out, '%g' % sip_obj.det_out,'%g' % sip_obj.chron_bird_out, '%s' % sip_obj.chronconb_out,],
        "Chronic-Expected": ['%g' % sip_obj.dose_bird_exp,'%g' % sip_obj.det_exp,'%g' % sip_obj.chron_bird_exp,'%s' % sip_obj.chronconb_exp,],
        "Units": ['mg/kg-bw', 'mg/kg-bw', '', '',],
    }
    return data

def gettsumdata(bodyweight_quail,bodyweight_duck,bodyweight_bird_other,bodyweight_rat,bodyweight_tested_mammal_other,solubility,
                    avian_ld50,mammalian_ld50,mineau_scaling_factor,noael_avian_water,noael_mammal_water):
    data = { 
        "Parameter": ['BW Quail', 'BW Duck', 'BW Bird Other', 'BW Rat', 'BW Mammal Other', 'Avian LD50', 'Mammalian LD50', 
                    'Solubility','AW Bird' , 'Mineau', 'NOAEC','NOAEL'],
        "Mean": ['%g' % numpy.mean(bodyweight_quail),'%g' % numpy.mean(bodyweight_duck),'%g' % numpy.mean(bodyweight_bird_other), '%g' % numpy.mean(bodyweight_rat), 
                 '%g' % numpy.mean(bodyweight_tested_mammal_other), '%g' % numpy.mean(solubility), '%g' % numpy.mean(avian_ld50), '%g' % numpy.mean(mammalian_ld50),
                 '%g' % numpy.mean(mineau_scaling_factor),
                 '%g' % numpy.mean(noael_avian_water), '%g' % numpy.mean(noael_mammal_water),],
        "Std": ['%g' % numpy.std(bodyweight_quail),'%g' % numpy.std(bodyweight_duck),'%g' % numpy.std(bodyweight_bird_other), '%g' % numpy.std(bodyweight_rat), 
                '%g' % numpy.std(bodyweight_tested_mammal_other), '%g' % numpy.std(solubility), '%g' % numpy.std(avian_ld50), '%g' % numpy.std(mammalian_ld50),
                 '%g' % numpy.std(mineau_scaling_factor),
                 '%g' % numpy.std(noael_avian_water),'%g' % numpy.std(noael_mammal_water),],
        "Min": ['%g' % numpy.min(bodyweight_quail),'%g' % numpy.min(bodyweight_duck),'%g' % numpy.min(bodyweight_bird_other), '%g' % numpy.min(bodyweight_rat), 
                '%g' % numpy.min(bodyweight_tested_mammal_other), '%g' % numpy.min(solubility), '%g' % numpy.min(avian_ld50), '%g' % numpy.min(mammalian_ld50),
                 '%g' % numpy.min(mineau_scaling_factor),
                 '%g' % numpy.min(noael_avian_water),'%g' % numpy.min(noael_mammal_water),],
         "Max": ['%g' % numpy.max(bodyweight_quail),'%g' % numpy.max(bodyweight_duck),'%g' % numpy.max(bodyweight_bird_other), '%g' % numpy.max(bodyweight_rat), 
                '%g' % numpy.max(bodyweight_tested_mammal_other), '%g' % numpy.max(solubility), '%g' % numpy.max(avian_ld50), '%g' % numpy.max(mammalian_ld50),
                 '%g' % numpy.max(mineau_scaling_factor),
                 '%g' % numpy.max(noael_avian_water),'%g' % numpy.max(noael_mammal_water),],
        "Unit": ['g', 'g', 'g', 'g', 'g','mg/kg-bw', 'mg/kg-bw', 'mg/L','g', '', 'g','mg/kg-diet', 'mg/kg-bw',],
    }
    return data

def gettsumdata_out(dose_bird_out, dose_mamm_out, at_bird_out, 
                    at_mamm_out, det_out, act_out, acute_bird_out, acute_mamm_out, 
                    chron_bird_out, chron_mamm_out):
    data = {
        "Parameter": ['Upper Bound Exposure - Avian', 'Upper Bound Exposure - Mammalian',
                    'Adjusted Toxicity Value (Acute) - Avian',
                    'Adjusted Toxicity Value (Acute) - Mammalian',
                    'Adjusted Toxicity Value (Chronic) - Avian',
                    'Adjusted Toxicity Value (Chronic) - Mammalian',
                    'Ratio of Exposure to Toxicity (Acute) - Avian',
                    'Ratio of Exposure to Toxicity (Acute) - Mammalian',
                    'Ratio of Exposure to Toxicity (Chronic) - Avian',
                    'Ratio of Exposure to Toxicity (Chronic) - Mammalian',],

        "Mean": [
                 '%g' % numpy.mean(dose_bird_out), '%g' % numpy.mean(dose_mamm_out), '%g' % numpy.mean(at_bird_out),
                 '%g' % numpy.mean(at_mamm_out), '%g' % numpy.mean(act_out), '%g' % numpy.mean(det_out),
                 '%g' % numpy.mean(acute_bird_out), '%g' % numpy.mean(acute_mamm_out),
                 '%g' % numpy.mean(chron_bird_out), '%g' % numpy.mean(chron_mamm_out),],

        "Std": ['%g' % numpy.std(dose_bird_out), '%g' % numpy.std(dose_mamm_out), '%g' % numpy.std(at_bird_out),
                '%g' % numpy.std(at_mamm_out), '%g' % numpy.std(act_out), '%g' % numpy.std(det_out),
                '%g' % numpy.std(acute_bird_out), '%g' % numpy.std(acute_mamm_out),
                '%g' % numpy.std(chron_bird_out), '%g' % numpy.std(chron_mamm_out),],

        "Min": ['%g' % numpy.min(dose_bird_out), '%g' % numpy.min(dose_mamm_out), '%g' % numpy.min(at_bird_out),
                '%g' % numpy.min(at_mamm_out), '%g' % numpy.min(act_out), '%g' % numpy.min(det_out),
                '%g' % numpy.min(acute_bird_out), '%g' % numpy.min(acute_mamm_out),
                '%g' % numpy.min(chron_bird_out), '%g' % numpy.min(chron_mamm_out),],

         "Max": ['%g' % numpy.max(dose_bird_out), '%g' % numpy.min(dose_mamm_out), '%g' % numpy.min(at_bird_out),
                '%g' % numpy.max(at_mamm_out), '%g' % numpy.max(act_out), '%g' % numpy.min(det_out),
                '%g' % numpy.max(acute_bird_out), '%g' % numpy.min(acute_mamm_out),
                '%g' % numpy.max(chron_bird_out), '%g' % numpy.max(chron_mamm_out),],

        "Unit": ['mg/kg-bw', 'mg/kg-bw','mg/kg-bw', 'mg/kg-bw', 'mg/kg-bw', 'mg/kg-bw', '','', '', '',],
    }
    return data


pvuheadings = getheaderpvu()
pvrheadings = getheaderpvr()
pvrheadingsqaqc = getheaderpvrqaqc()
sumheadings = getheadersum()
djtemplate = getdjtemplate()
tmpl = Template(djtemplate)

def table_all(sip_obj):
    html_all = table_1(sip_obj)      
    html_all = html_all + table_2(sip_obj)
    html_all = html_all + table_3(sip_obj)
    return html_all

def table_all_qaqc(sip_obj):
    html_all = table_1(sip_obj)
    html_all = html_all + table_2_qaqc(sip_obj)
    html_all = html_all + table_3_qaqc(sip_obj)
    return html_all

def timestamp(sip_obj="", batch_jid=""):
    if sip_obj:
        st = datetime.datetime.strptime(sip_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    else:
        st = datetime.datetime.strptime(batch_jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    html="""
    <div class="out_">
        <b>SIP <a href="http://www.epa.gov/oppefed1/models/terrestrial/sip/sip_user_guide.html">Version 1.0</a> (Beta)<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html

def table_1(sip_obj):
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section2"><span></span>Application and Chemical Information</H4>
                <div class="out_ container_output">
        """
        t1data = gett1data(sip_obj)
        t1rows = gethtmlrowsfromcols(t1data,pvuheadings)
        html = html + tmpl.render(Context(dict(data=t1rows, headings=pvuheadings)))
        html = html + """
                </div>
        </div>
        """
        return html

def table_2(sip_obj):
        html = """
        <br>
        <H3 class="out_1 collapsible" id="section3"><span></span>SIP Output</H3>
        <div class="out_1">
            <H4 class="out_1 collapsible" id="section4"><span></span>Mammalian Results</H4>
                <div class="out_ container_output">
        """
        t2data = gett2data(sip_obj)
        t2rows = gethtmlrowsfromcols(t2data,pvrheadings)
        html = html + tmpl.render(Context(dict(data=t2rows, headings=pvrheadings)))
        html = html + """
                </div>
        """
        return html  

def table_2_qaqc(sip_obj):
        html = """
        <br>
        <H3 class="out_1 collapsible" id="section3"><span></span>SIP Output</H3>
        <div class="out_1">
            <H4 class="out_1 collapsible" id="section4"><span></span>Mammalian Results</H4>
                <div class="out_ container_output">
        """
        t2data = gett2dataqaqc(sip_obj)
        t2rows = gethtmlrowsfromcols(t2data,pvrheadingsqaqc)
        html = html + tmpl.render(Context(dict(data=t2rows, headings=pvrheadingsqaqc)))
        html = html + """
                </div>
        """
        return html  

def table_3(sip_obj):
        html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Avian Results</H4>
                <div class="out_ container_output">
        """
        t3data = gett3data(sip_obj)
        t3rows = gethtmlrowsfromcols(t3data,pvrheadings)
        html = html + tmpl.render(Context(dict(data=t3rows, headings=pvrheadings)))
        html = html + """
                </div>
        </div>
        """
        return html

def table_3_qaqc(sip_obj):
        html = """
            <H4 class="out_1 collapsible" id="section4"><span></span>Avian Results</H4>
                <div class="out_ container_output">
        """
        t3data = gett3dataqaqc(sip_obj)
        t3rows = gethtmlrowsfromcols(t3data,pvrheadingsqaqc)
        html = html + tmpl.render(Context(dict(data=t3rows, headings=pvrheadingsqaqc)))
        html = html + """
                </div>
        </div>
        """
        return html


def table_all_sum(sumheadings, tmpl, bodyweight_quail,bodyweight_duck,bodyweight_bird_other,bodyweight_rat,bodyweight_tested_mammal_other,solubility,
                    avian_ld50,mammalian_ld50,mineau_scaling_factor,noael_avian_water,noael_mammal_water,
                    dose_bird_out, dose_mamm_out, at_bird_out, 
                    at_mamm_out, det_out, act_out, acute_bird_out, acute_mamm_out, 
                    chron_bird_out, chron_mamm_out):
    html_all_sum = table_sum_input(sumheadings, tmpl, bodyweight_quail,bodyweight_duck,bodyweight_bird_other,bodyweight_rat,bodyweight_tested_mammal_other,solubility,
                    avian_ld50,mammalian_ld50,mineau_scaling_factor,noael_avian_water,noael_mammal_water)
    html_all_sum += table_sum_output(sumheadings,tmpl,dose_bird_out,dose_mamm_out,at_bird_out, 
                    at_mamm_out,det_out,act_out,acute_bird_out,acute_mamm_out,chron_bird_out,chron_mamm_out)
    return html_all_sum

def table_sum_input(sumheadings, tmpl, bodyweight_quail,bodyweight_duck,bodyweight_bird_other,bodyweight_rat,bodyweight_tested_mammal_other,solubility,
                    avian_ld50,mammalian_ld50,mineau_scaling_factor,noael_avian_water,noael_mammal_water):
        html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>Summary Statistics</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section4"><span></span>Batch Inputs</H4>
                <div class="out_ container_output">
        """
        tsuminputdata = gettsumdata(bodyweight_quail,bodyweight_duck,bodyweight_bird_other,bodyweight_rat,bodyweight_tested_mammal_other,solubility,avian_ld50,mammalian_ld50,mineau_scaling_factor,noael_avian_water,noael_mammal_water)
        tsuminputrows = gethtmlrowsfromcols(tsuminputdata, sumheadings)
        html = html + tmpl.render(Context(dict(data=tsuminputrows, headings=sumheadings)))
        html = html + """
                </div>
        """
        return html

def table_sum_output(sumheadings, tmpl, dose_bird_out, dose_mamm_out, at_bird_out, 
                    at_mamm_out, det_out, act_out, acute_bird_out, acute_mamm_out, 
                    chron_bird_out, chron_mamm_out):
        html = """
        <br>
            <H4 class="out_1 collapsible" id="section3"><span></span>SIP Outputs</H4>
                <div class="out_ container_output">
        """
        tsumoutputdata = gettsumdata_out(dose_bird_out, dose_mamm_out, at_bird_out, 
                    at_mamm_out, det_out, act_out, acute_bird_out, acute_mamm_out, 
                    chron_bird_out, chron_mamm_out)
        tsumoutputrows = gethtmlrowsfromcols(tsumoutputdata, sumheadings)
        html = html + tmpl.render(Context(dict(data=tsumoutputrows, headings=sumheadings)))
        html = html + """
                </div>
        </div>
        """
        return html

