"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
# How model name appears on web page
header = 'TerrPlant'

#model description html for description page
description = '<p>TerrPLANT provides screening level estimates of exposure to terrestrial plants ' \
              'from single pesticide applications through runoff or drift.  Monocots and dicots ' \
              'found in dry or semi-aquatic habitats can be evaluated using this model.  Exposure ' \
              'estimates can be generated for both listed and non-listed species using TerrPLANT.</p>' \
              '<p>Both dry and semi-aquatic exposure estimates include conceptual models with a ' \
              'target area that is adjacent to a non-target area.  Dry area estimates are determined ' \
              'using pesticide amounts received in the non-target area through sheet runoff from a ' \
              'target area equal in size.  Semi-aquatic estimates are based on pesticide amounts in ' \
              'channel runoff from a target area that is 10 times larger than the non-target area.</p>' \
              '<p>The TerrPLANT model assumes that 1% of the mass of liquid pesticides applied ' \
              'per acre will runoff to the non-target area, 5% for aerial pesticides and 0% for ' \
              'granular applications.  Toxicity of pesticides to non-listed species is based on ' \
              'EC<sub>25</sub> values for the most sensitive monocots and dicots tested.  For ' \
              'listed species, corresponding NOAEC or EC<sub>05</sub> values are used to determine ' \
              'toxicity.  RQ values are generated through comparisons with adverse effects ' \
              'levels measured in seedling emergence studies.</p>'
