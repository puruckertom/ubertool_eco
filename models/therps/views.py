"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
# How model name appears on web page
header = 'T-HERPS'

#model description html for description page
description = '<p>Terrestrial Herpetofaunal Exposure Residue Program Simulation ' \
              '(T-HERPS) is designed to estimate dietary exposure and risk to ' \
              'terrestrial-phase amphibians and reptiles from pesticide use.  ' \
              'Historically, risk assessments for terrestrial-phase amphibians ' \
              'and reptiles have been estimated from models using avian toxicity ' \
              'data.  T-HERPS was developed to more accurately estimate amphibian ' \
              'and reptile exposure risk by including lower metabolic rates and ' \
              'dietary requirements that are associated with poikilothermic organisms.  ' \
              'When terrestrial-phase amphibian or reptile data is unavailable, avian ' \
              'toxicity data can be used in T-HERPS although output estimates should be ' \
              'interpreted cautiously.</p>' \
              '<p>An allometric function in T-HERPS allows for food intake to be ' \
              'estimated from the body size of the study animal.  The associated equation ' \
              'is based on food ingestion rates of an iguanid lizard, an insectivorous ' \
              'reptile with dietary habits similar to the California red-legged frog, and ' \
              'therefore should not be used for strictly herbivorous reptiles and amphibians.  ' \
              'For species that consume larger prey, such as other amphibians, reptiles or small ' \
              'mammals, alternative methods for determining EECs are included in T-HERPS.</p>' \
              '<p>Food intake estimates are provided in units of kg-diet/day by size class ' \
              '(small, medium, large).  Daily doses of pesticides to the study animal are ' \
              'given in units of mg/kg - bw by size class and food type.  Using the daily ' \
              'dose estimates, T-HERPS calculates the mass of the pesticide potentially ' \
              'consumed for EEC determinations.  Input estimates of food water content are ' \
              'required for calculation of pesticide intake.</p>'
