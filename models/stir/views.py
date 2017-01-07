"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
# How model name appears on web page
header = 'STIR'

#model description html for description page
description = '<p>The STIR model was developed as a screening model to estimate ' \
              'inhalation risk of chemicals to birds and mammals.  Chemical ' \
              'specific physical properties are required for executing the model.  ' \
              'Vapor phase and droplet-spray exposure risks are estimated in STIR ' \
              'and then compared to avian inhalation or mammalian inhalation and ' \
              'oral toxicity data.  Inhalation exposure routes addressed by the model ' \
              'include directly applied spray, volatilization of residues on plant ' \
              'canopy and volatilization of residues in soil.</p>' \
              '<p>The exposure estimates are based on the type of application (i.e., ' \
              'air or ground spray, granules, seed treatments) and the quantity of a ' \
              'specified chemical that is to be applied to a field.  The screening tool ' \
              'calculates the theoretical maximum pure product air concentration at ' \
              'standard temperature and pressure based on vapor pressure and molecular ' \
              'weight. STIR also calculates inhalation rates and inhalation dose as a ' \
              'function of saturated air concentration, inhalation rate and animal ' \
              'weight. Toxicity endpoints are estimated using adjusted LD<sub>50</sub> ' \
              'values. Model results are presented as a ratio of the inhalation exposure ' \
              'dose to toxicity.  To determine if inhalation exposure to a particular ' \
              'chemical warrants further investigation, ratios are compared to threshold ' \
              'values.</p>' \
              '<img src = \"/static_qed/images/stir_figure1.gif\" alt=\"STIR Model\">'
