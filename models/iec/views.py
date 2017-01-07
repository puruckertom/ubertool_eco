"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
# How model name appears on web page
header = 'IEC'

#model description html for description page
description = '<p>IECV1.1 (Individual Effect Chance Model Version 1.1) estimates potential ' \
              'effects at an individual level. Generally, available toxicity data provides ' \
              'an LC<sub>50</sub> or an EC<sub>50</sub>, (the concentration at which 50% ' \
              'of the test population exhibits the designated endpoint, usually mortality).  ' \
              'The Agency uses the probit dose response relationship as a tool for deriving ' \
              'the probability of effects on a single individual.  The individual effects ' \
              'probability associated with the acute RQ is based on the mean estimate of ' \
              'the probit dose response slope and an assumption that that probit model is ' \
              'appropriate for the data set.  In some cases, probit is not the appropriate ' \
              'model for the data, and EFED has low confidence in extrapolations from these ' \
              'types of data sets.  In addition to a single effects probability estimate ' \
              'based on the mean, upper, and lower estimates of the effects probability are ' \
              'also provided to account for variance in the slope, if available.  The upper ' \
              'and lower bounds of the effects probability are based on available information ' \
              'on the 95% confidence interval of the slope.  </p>'
