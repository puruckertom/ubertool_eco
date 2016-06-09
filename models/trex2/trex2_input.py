"""
.. module:: trex2_input
   :synopsis: A useful module indeed.
"""

from django.template.loader import render_to_string


def trex2_input_page(request, model='', header='', form_data=None):
    import trex2_parameters

    html = render_to_string('04uberinput_jquery.html', {'model': model})
    html += render_to_string('04uberinput_start_tabbed_drupal.html', {
        'MODEL': model,
        'TITLE': header})
    html += render_to_string('04uberinput_tabbed_nav.html', {
        'nav_dict': {
            'class_name': ['Chemical', 'Avian', 'Mammal'],
            'tab_label': ['Chemical', 'Avian', 'Mammal']
        }
    })
    html += """<br><table class="input_table tab tab_Chemical">"""
    html += str(trex2_parameters.trexInp_chem(form_data))
    html += """</table><table class="input_table tab tab_Application tab_Chemical">
                                <tr><th colspan="2" scope="col"><label for="id_noa">Number of Applications:</label></th>
                                    <td colspan="3" scope="col"><select name="noa" id="id_noa">
                                        <option value="1">1</option><option value="2">2</option><option value="3" selected>3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option><option value="10">10</option><option value="11">11</option><option value="12">12</option><option value="13">13</option><option value="14">14</option><option value="15">15</option><option value="16">16</option><option value="17">17</option><option value="18">18</option><option value="19">19</option><option value="20">20</option><option value="21">21</option><option value="22">22</option><option value="23">23</option><option value="24">24</option><option value="25">25</option><option value="26">26</option><option value="27">27</option><option value="28">28</option><option value="29">29</option><option value="30">30</option></select>
                                    </td>
                                </tr>
                                <tr id="noa_header">
                                    <th width="18%">App#</th>
                                    <th width="18%" id="rate_head">Rate (lb ai/acre)</th>
                                    <th width="18%">Day of Application</th>
                                </tr>
                                <tr class="tab_noa1">
                                    <td><input name="jm1" type="text" size="5" value="1"/></td>
                                    <td><input type="text" size="5" name="rate1" id="id_rate1" value="4"/></td>
                                    <td><input type="text" size="5" name="day1" id="id_day1" value="0" /></td>
                                </tr>"""
    html += """</table><table class="input_table tab tab_Avian" style="display:none">"""
    html += str(trex2_parameters.trexInp_bird(form_data))
    html += """</table><table class="input_table tab tab_Mammal" style="display:none">"""
    html += str(trex2_parameters.trexInp_mammal(form_data))
    html += render_to_string('04uberinput_tabbed_end_drupal.html', {})
    html += render_to_string('04ubertext_end_drupal.html', {})
    # Check if tooltips dictionary exists
    # try:
    #     import trex2_tooltips
    #     hasattr(trex2_tooltips, 'tooltips')
    #     tooltips = trex2_tooltips.tooltips
    # except:
    #     tooltips = {}
    # html += render_to_string('05ubertext_tooltips_right.html', {'tooltips': tooltips})

    return html
