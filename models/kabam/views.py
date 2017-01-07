"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
# How model name appears on web page
header = 'KABAM'

#model description html for description page
description = '<p>K<sub>ow</sub> (based) Aquatic BioAccumulation Model (KABAM) ' \
              'links hydrophobic organic pesticide bioaccumulation in aquatic ' \
              'components of a food web to terrestrial exposure in birds and ' \
              'mammals.  Given the dual ecosystem emphasis, KABAM is divided ' \
              'into two portions: 1) an aquatic bioaccumulation model and 2) ' \
              'a terrestrial risk component.  The bioaccumulation model is based ' \
              'off of a widely accepted model by Arnot and Gobas (2004) developed to ' \
              'evaluate PCB and select pesticide transfer through Great Lakes ecosystems.  ' \
              'Dietary and respiratory exposures are estimated using a pesticide\'s ' \
              'octanol-water partition coefficient (KOW).  The terrestrial risk component ' \
              'follows EPA\'s TREX model.  KABAM spans all trophic levels from aquatic ' \
              'primary producers and consumers to aquatic and terrestrial predators ' \
              '(Figure 1).</p>' \
              '<p>To use KABAM effectively, a pesticide must adhere to all 3 of the ' \
              'following characteristics:</p>' \
              '<ul class=\"bullet\">' \
              '<li>Be chemically non-ionic and organic</li>' \
              '<li>Log KOW; range = 4 - 8</li>' \
              '<li>Can reach aquatic habitats</li>' \
              '</ul>'
