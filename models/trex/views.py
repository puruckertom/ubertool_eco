"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
# How model name appears on web page
header = 'T-REX 1.5.2'

#model description html for description page
description = '<p>This spreadsheet-based model calculates the residues on ' \
              'avian and mammalian food items (e.g., short or tall grass, ' \
              'seeds, insects, etc) along with the dissipation rate of a ' \
              'chemical applied to foliar surfaces (for single or multiple ' \
              'applications) in order to estimate acute and reproductive ' \
              'risk quotients.  T-REX offers two unique advantages over similar ' \
              'models: 1) the relative body weight of the animal under assessment, ' \
              'as compared to the test animal, is used to adjust acute and chronic ' \
              'toxicity values and 2) risk quotients are calculated for granular ' \
              'applications and seed treatments.  Output for both avian and mammalian ' \
              'diet- and dose-based EEC and RQs are based on upper bound and mean ' \
              'Kenaga values.</p>' \
              '<p>T-REX users enter specified endpoint data obtained from avian or ' \
              'mammal acute oral LD<sub>50</sub>, acute dietary LC<sub>50</sub>, or ' \
              'reproductive NOAEC/L toxicity studies to calculate risk quotients.  ' \
              'Users must also choose a test species from a drop-down menu.  For avian ' \
              'models, bobwhite quail and mallard duck data is commonly used.  If the ' \
              'body weight of a different test species is known, the user can choose ' \
              '\"other\" from the drop-down menu.  For mammalian models, the \"other\" ' \
              'option is not currently available, therefore, test species other than ' \
              'laboratory rats must be done by hand. </p>' \
              '<p>Estimates of LD<sub>50</sub> ft<sup>-2</sup> risk index values can be ' \
              'generated in T-REX for granular formations and row, banded and in-furrow ' \
              'applications.  An adjusted LD<sub>50</sub> toxicity value and EEC are used ' \
              'for the LD<sub>50</sub> ft<sup>-2</sup> calculation which is then compared ' \
              'to a specific level of concern (LOC).</p>'
