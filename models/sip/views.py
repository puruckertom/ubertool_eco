"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
# How model name appears on web page
header = 'SIP'

#model description html for description page
description = '<p>The SIP model is designed to estimate chemical exposure from ' \
              'drinking water alone in birds and mammals.  Dietary, dermal and ' \
              'respiratory pathways are not considered in this model and cannot ' \
              'be ruled out as additional sources of exposure.  For purposes of ' \
              'risk assessment, it is assumed that 100% of daily water needs are ' \
              'achieved through drinking water and that these needs are equivalent ' \
              'to the daily water flux rate.  The upper bound of exposure is ' \
              'estimated through the use of an allometric equation in daily water ' \
              'intake rate determination (units in mg/kg ? bw).  The equation also ' \
              'considers chemical water solubility.  Acute toxicity values are adjusted ' \
              'using LD<sub>50</sub> values while chronic toxicity is adjusted through ' \
              'NOAEC studies in birds and NOAEL data in mammals.  To determine whether ' \
              'drinking water poses a chemical risk to the study animal, users examine ' \
              'ratios of upper bound exposure estimates relative to either adjusted ' \
              'LD<sub>50</sub>, NOAEC or NOAEL values.</p>'
