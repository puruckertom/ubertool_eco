"""
.. module:: agdrift_tables
   :synopsis: A useful module indeed.
"""

import numpy
# import django
from django.template import Context, Template
from django.utils.safestring import mark_safe
import agdrift_model, agdrift_parameters
import time
import datetime
import logging
from django.template.loader import render_to_string

logger = logging.getLogger("AgdriftTables")


def getheaderpvu():
    headings = ["Parameter", "Value"]
    return headings


def getheaderpvr():
    headings = ["Parameter", "Value"]
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
        col += [None, ] * (max_len - len(col))

    # Then rotate the structure...
    rows = [[col[i] for col in columns] for i in range(max_len)]
    return rows


def getdjtemplate():
    dj_template = """
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


def gett1data(agdrift_obj):
    # general inputs
    data = {
        "Parameter": ['Assessment type', 'Application method', 'Aquatic Body Type', 'Drop size', 'Scenario',
                      'Scenario Type', 'Application rate', 'Calculation Input',],
        "Value": [agdrift_obj.ecosystem_type, agdrift_obj.application_method, agdrift_obj.aquatic_body_type,
                  agdrift_obj.drop_size, agdrift_obj.out_sim_scenario_chk, agdrift_obj.out_sim_scenario_id,
                  agdrift_obj.application_rate, agdrift_obj.calculation_input,],
    }
    return data


def gett2data(agdrift_obj):
    if(agdrift_obj.aquatic_body_type == 'EPA Defined Pond'):
        width = agdrift_obj.out_default_width
        length = agdrift_obj.out_default_length
        depth = agdrift_obj.out_default_pond_depth
    elif(agdrift_obj.aquatic_body_type == 'User Defined Pond'):
        width = agdrift_obj.user_pond_width
        length = 'NA'
        depth = agdrift_obj.user_pond_depth
    #'EPA Defined Pond', 'User Defined Pond', 'EPA Defined Wetland', 'User Defined Wetland'
    elif(agdrift_obj.aquatic_body_type == 'EPA Defined Wetland'):
        width = agdrift_obj.out_default_width
        length = agdrift_obj.out_default_length
        depth = agdrift_obj.out_default_wetland_depth
    elif(agdrift_obj.aquatic_body_type == 'User Defined Wetland'):
        width = agdrift_obj.user_pond_width
        length = 'NA'
        depth = agdrift_obj.user_pond_depth
    else:
        width = 'NA'
        depth = 'NA'

    data = {
        "Parameter": ['Downwind distance (feet)', 'Width (feet)', 'Length (feet)', 'Depth (feet)',],
        "Value": [agdrift_obj.downwind_distance, width, length, depth, ],
    }
    return data


def gett3data(agdrift_obj):
    data = {
        "Parameter": ['Assessment type', 'Application method', 'Aquatic Body Type', 'Drop size', 'Scenario', ],
        "Value": [agdrift_obj.ecosystem_type, agdrift_obj.application_method, agdrift_obj.aquatic_body_type,
                  agdrift_obj.drop_size, agdrift_obj.out_sim_scenario_chk, ],
    }
    return data


def gett4data(agdrift_obj):
    data = {
        "Parameter": ['Assessment type', 'Application method', 'Aquatic Body Type', 'Drop size', 'Scenario', ],
        "Value": [agdrift_obj.ecosystem_type, agdrift_obj.application_method, agdrift_obj.aquatic_body_type,
                  agdrift_obj.drop_size, agdrift_obj.out_sim_scenario_chk, ],
    }
    return data


# def gett2data(agdrift_obj):
#    data = { 
#        "Parameter": ['Distance', 'Spray drift fraction',],
#        "Value": [agdrift_obj.results[0], agdrift_obj.results[1],],
#    }
#    return data
def gett5data(agdrift_obj):
    logger.info(vars(agdrift_obj))
    data = {
        "Parameter": ['Spray drift fraction of applied', 'Initial Average Deposition (g/ha)',
                      'Initial Average Deposition (lb/ac)', 'Initial Average Concentration (ng/L)',
                      'Initial Average Deposition (mg/cm2)', 'Distance to Point or Waterbody (ft)', ],
        # "Value": ['%.3f' % agdrift_obj.out_init_avg_dep_foa,'%.3f' % agdrift_obj.out_avg_dep_gha,'%.3f' % agdrift_obj.out_avg_dep_lbac, '%.3f' % agdrift_obj.out_deposition_ngl, '%.3f' % agdrift_obj.out_avg_field_dep_mgcm,],
        "Value": ['%.5f' % agdrift_obj.out_avg_dep_foa, '%.5f' % agdrift_obj.out_avg_dep_gha,
                  '%.5f' % agdrift_obj.out_avg_dep_lbac, '%.5f' % agdrift_obj.out_avg_waterconc_ngl,
                  '%.5f' % agdrift_obj.out_avg_field_dep_mgcm, '%.d' % int(agdrift_obj.downwind_distance), ],
    }
    return data


pvuheadings = getheaderpvu()
pvrheadings = getheaderpvr()
# pvrheadingsqaqc = getheaderpvrqaqc()
sumheadings = getheadersum()
djtemplate = getdjtemplate()
tmpl = Template(djtemplate)


def table_all(agdrift_obj):
    html_all = table_1(agdrift_obj)
    html_all = html_all + table_2(agdrift_obj)
    #html_all = html_all + table_3(agdrift_obj)
    #html_all = html_all + table_4(agdrift_obj)
    html_all = html_all + table_5(agdrift_obj)
    # html_all = html_all + table_3(agdrift_obj)
    # html_all = html_all + render_to_string('agdrift-output-jqplot.html', {'chart_num':1}) #agdrift_obj.loop_indx
    return html_all


def timestamp(agdrift_obj="", batch_jid=""):
    # ts = time.time()
    # st = datetime.datetime.fromtimestamp(ts).strftime('%A, %Y-%B-%d %H:%M:%S')
    if agdrift_obj:
        st = datetime.datetime.strptime(agdrift_obj.jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    else:
        st = datetime.datetime.strptime(batch_jid, '%Y%m%d%H%M%S%f').strftime('%A, %Y-%B-%d %H:%M:%S')
    html = """
    <div class="out_">
    <b>Agdrift Version 0.1 (Beta)<br>
    """
    html = html + st
    html = html + " (EST)</b>"
    html = html + """
    </div>"""
    return html


def table_1(agdrift_obj):
    html = """
        <H3 class="out_1 collapsible" id="section1"><span></span>User Inputs</H3>
        <div class="out_">
            <H4 class="out_1 collapsible" id="section1"><span></span>Application and Chemical Information</H4>
                <div class="out_ container_output">
        """
    t1data = gett1data(agdrift_obj)
    t1rows = gethtmlrowsfromcols(t1data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t1rows, headings=pvuheadings)))
    html = html + """
                </div>
        </div>
        """
    return html


def table_2(agdrift_obj):
    html = """
        <H4 class="out_2 collapsible" id="section2"><span></span>Aquatic Body Information</H4>
            <div class="out_ container_output">
        """
    t2data = gett2data(agdrift_obj)
    t2rows = gethtmlrowsfromcols(t2data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t2rows, headings=pvuheadings)))
    html = html + """
            </div>
        """
    return html


def table_3(agdrift_obj):
    html = """
        <H4 class="out_3 collapsible" id="section2"><span></span>Model Output</H4>
            <div class="out_ container_output">
        """
    t3data = gett3data(agdrift_obj)
    t3rows = gethtmlrowsfromcols(t3data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t3rows, headings=pvuheadings)))
    html = html + """
            </div>
        """
    return html


def table_4(agdrift_obj):
    html = """
    <H4 class="out_4 collapsible" id="section2"><span></span>Model Output</H4>
        <div class="out_ container_output">
    """
    t4data = gett4data(agdrift_obj)
    t4rows = gethtmlrowsfromcols(t4data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t4rows, headings=pvuheadings)))
    html = html + """
        </div>
    """
    return html


def table_5(agdrift_obj):
    html = """
    <H4 class="out_5 collapsible" id="section2"><span></span>Model Output</H4>
        <div class="out_ container_output">
    """
    t5data = gett5data(agdrift_obj)
    t5rows = gethtmlrowsfromcols(t5data, pvuheadings)
    html = html + tmpl.render(Context(dict(data=t5rows, headings=pvuheadings)))
    html = html + """
        </div>
    """
    return html


def table_6(agdrift_obj):
    html = """
        <table style="display:none;">
            <tr>
                <td>distance</td>
                <td id="distance%s">%s</td>
            </tr>
            <tr>
                <td>deposition</td>
                <td id="deposition%s">%s</td>
            </tr>
        </table>
        <br>
        <h3 class="out_6 collapsible" id="section2"><span></span>Results</h3>
            <H4 class="out_6 collapsible" id="section3"><span></span>Plot of spray drift</H4>
                <div class="out_"></div>
        """ % (1, agdrift_obj.out_x, 1, agdrift_obj.out_express_y)  # agdrift_obj.loop_indx

    # t2data = gett2data(agdrift_obj)
    # t2rows = gethtmlrowsfromcols(t2data,pvrheadings)
    # html = html + tmpl.render(Context(dict(data=t2rows, headings=pvuheadings)))
    # html = html + """
    #         </div>
    # """
    return html
