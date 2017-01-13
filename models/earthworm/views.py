"""
.. module:: views
   :synopsis: A useful module indeed.
"""

#these should be in templates
batch = '<p>Will be back soon...</p>'

qaqc = '<p>Will be back soon..</p>'

#model algorithm html for algorithm page
algorithm = '<p>For any particular environmental phase (e.g., water, soil, air, or biota) there ' \
            'is a corresponding \"fugacity capacity\" with units of mol/m<sup>3</sup>-Pa and is denoted ' \
            'by Z. The relationship between fugacity, fugacity capacity and chemical concentration (C) ' \
            'is defined by Equation 1.' \
            '</p>' \
            '<p>Equation 1. <img src = \"/static_qed/images/latex/earthworm/earthworm_image1.png\" ' \
            'alt=\"earthworm_1\"></p>' \
            '<p>' \
            'Fugacity capacities for a given chemical are calculated for the phases of interest as ' \
            'part of the exposure point estimation methodology (Mackay and Paterson 1981). The following ' \
            'calculations of fugacity capacity for water (Z<sub>W</sub>, soil (Z<sub>S</sub>) and ' \
            'earthworms (Z<sub>E</sub>) (Equation 2-4) require several chemical-specific parameters and ' \
            'assumptions of system temperature (25 &#8451;) and steady state equilibrium. Parameter values ' \
            'relevant to Equations 2-4 are defined in Table 1.</p>' \
            '<p>Equation 2. <img src = \"/static_qed/images/latex/earthworm/earthworm_image2.png\" ' \
            'alt=\"earthworm_2\"></p>' \
            '<p>Equation 3. <img src = \"/static_qed/images/latex/earthworm/earthworm_image3.png\" ' \
            'alt=\"earthworm_3\"></p>' \
            '<p>Equation 4. <img src = \"/static_qed/images/latex/earthworm/earthworm_image4.png\" ' \
            'alt=\"earthworm_4\"></p>' \
            '<p>Fugacity capacities for a given chemical are caculated for the phases of interest as part ' \
            'of the exposure point concentration estimation methodology. By definition, the ratio between Z ' \
            'values of different phases (compartments) equals the partitioning coefficient (for example, see ' \
            'Equation 5).' \
            '</p>' \
            '<p>Equation 5. <img src = \"/static_qed/images/latex/earthworm/earthworm_image5.png\" alt=\"earthworm_5\"></p>' \
            '<p>In this approach, it is assumed that a pesticide partitions between the soil, the (pore) water and the ' \
            'air contained within the soil of the treatment site. It is assumed that earthworms dwelling within the soil ' \
            'are exposed to a pesticide via ingestion of contaminated soil and pore-water (Belfroid et. al 1994). The ' \
            'concentration of a pesticide in earthworm tissues can be calculated according to Equation 6. The parameters of ' \
            'Equation 6 are defined in Table 1.' \
            '</p>' \
            '<p>Equation 6. <img src = \"/static_qed/images/latex/earthworm/earthworm_image6.png\" alt=\"earthworm_6\"></p>' \
            '<p>' \
            'Equation 6 can be redefined using equations 2-4 as follows in Equation 7. Equation 7 is used to calculate ' \
            'the concentration of a pesticide in earthworms inhabiting the soil of treatment sites.' \
            '</p>' \
            '<p>Equation 7. <img src = \"/static_qed/images/latex/earthworm/earthworm_image7.png\" alt=\"earthworm_7\"></p>' \
            '<p>L can be based on the lipid content of earthworms, which was assumed to be 0.01 (Cobb et al. 1995). The ' \
            'resulting C<sub>E</sub> value is in units of mol/m<sup>3</sup>. This value is converted to units of g/kg ' \
            'using Equation 8. The density of the earthworm (&#961;<sub>E</sub>) is assumed to be 1000kg/m<sup>3</sup> ' \
            '(equivalent to density of water). The resulting concentration of pesticide in earthworms denotes in ' \
            '(C<sub>E</sub><sup>*</sup>) of Equation 8.' \
            '</p><p>Equation 8. <img src = \"/static_qed/images/latex/earthworm/earthworm_image8.png\" alt=\"earthworm_8\"></p>' \
            '<p>Table 1. Summary of parameters relevant to earthworm fugacity model.</p>' \
            '<table border=\"1\">' \
            '<tr>' \
            '<th>Symbol</th>' \
            '<th>Definition</th>' \
            '<th>Units</th>' \
            '</tr>' \
            '<tr>' \
            '<td>C<SUB>E</SUB></td>' \
            '<td>Chemical concentration in earthworm tissue</td>' \
            '<td>mol/m<SUP>3</SUP></td>' \
            '</tr>' \
            '<tr>' \
            '<td>C<SUB>E</SUB><SUP>*</SUP></td>' \
            '<td>Chemical concentration in earthworm tissue</td>' \
            '<td>k/kg</td>' \
            '</tr>' \
            '<tr>' \
            '<td>C<SUB>S</SUB></td>' \
            '<td>Chemical concentration in soil</td>' \
            '<td>mol/m<SUP>3</SUP></td>' \
            '</tr>' \
            '<tr>' \
            '<td>C<SUB>W</SUB></td>' \
            '<td>Chemical concentration in pore water of soil</td>' \
            '<td>mol/m<SUP>3</SUP></td>' \
            '</tr><tr>' \
            '<td>H</td>' \
            '<td>Henry\'s Law constant</td>' \
            '<td>m<SUP>3</SUP>-Pa/mol</td>' \
            '</tr>' \
            '<tr>' \
            '<td>K<SUB>d</SUB></td>' \
            '<td>Soil partitioning coefficient</td>' \
            '<td>cm<SUP>3</SUP>/g</td>' \
            '</tr>' \
            '<tr>' \
            '<td>K<SUB>OW</SUB></td>' \
            '<td>Octanol to water partition coefficient</td>' \
            '<td>none</td>' \
            '</tr>' \
            '<tr>' \
            '<td>L</td>' \
            '<td>Lipid fraction of earthworm</td>' \
            '<td>none</td>' \
            '</tr>' \
            '<tr>' \
            '<td>MW</td>' \
            '<td>molecular weight of chemical</td>' \
            '<td>g/mol</td>' \
            '</tr>' \
            '<tr>' \
            '<td>Z<SUB>E</SUB></td>' \
            '<td>Fugacity capacity of pesticide in earthworms</td>' \
            '<td>mol/m<SUP>3</SUP>-Pa</td>' \
            '</tr>' \
            '<tr>' \
            '<td>Z<SUB>S</SUB></td>' \
            '<td>Fugacity capacity of pesticide in soil</td>' \
            '<td>mol/m<SUP>3</SUP>-Pa</td>' \
            '</tr>' \
            '<tr>' \
            '<td>Z<SUB>W</SUB></td>' \
            '<td>Fugacity capacity of pesticide in (pore) water</td>' \
            '<td>mol/m<SUP>3</SUP>-Pa</td>' \
            '</tr>' \
            '<tr>' \
            '<td>&#961;<sub>E</sub></td>' \
            '<td>Density of earthworm</td>' \
            '<td>kg/m<SUP>3</SUP></td>' \
            '</tr>' \
            '<tr><td>&#961;<sub>S</sub></td><td>Bulk density of soil</td>' \
            '<td>g/cm<SUP>3</SUP></td>' \
            '</tr>' \
            '</table>'

#model description html for description page
description = '<p>Earthworm Fugacity Modeling is a simple fugacity approach was employed ' \
              'to estimate pesticides concentrations in earthworms. Fugacity is most often r' \
              'egarded as the \"escaping tendency\" of a chemical from a particular phase. ' \
              'Fugacity has units of presure, generally pascals (Pa), and can be related ' \
              'to phase concentratons.</p>' \
              '<p>The T-REX model (USEPA 2008) is useful for assessing exposures of ' \
              'terrestrial animals to pesticide residues on foliar surfaces of crops ' \
              'and seeds. The model cannot be used to assess pesticide exposures to ' \
              'terrestrial animals resulting from consumption of earthworms contaminated ' \
              'with pesticide mass present in the soil of the application site. In order ' \
              'to explore the potential exposures of mammals to pesticides present in the ' \
              'soil and earthworms present on the treatment site, a simple fugacity approach ' \
              'was employed to estimate pesticides concentrations in earthworms. </p>'

# How model name appears on web page
header = 'Earthworm'

history = '<p>User History</p>'

references = '<p> Current github source code:' \
             '</p>' \
             '<ul class=\"bullet\">' \
             '<li><a href=\"http://github.com/quanted/ubertool_app/tree/master/models/earthworm\">ubertool_app on GitHub' \
             '</a></li>' \
             '<li><a href=\"http://github.com/quanted/ubertool/tree/master/ubertool/earthworm\"> ubertool on GitHub' \
             '</a></li>' \
             '</ul>' \
             '<p>' \
             'Belfroid, A., M. Sikkenk, W. Seinen, K.V. Gestel, J. Hermens. 1994. The toxicokinetic behavior of ' \
             'chlorobenzenes in earthworm (<i>Eisenia andrei</i>) experiments in soil. Environ. Toxicol. Chem. 13: 93-99.' \
             '</p>' \
             '<p>Cobb, G.P., E.H. Hol, P.W. Allen, J.A Gagne, R.J. Kendall. 1995. Uptake, metabolism, and toxicity of ' \
             'terbufos in the earthworm (<i>Lumbricus terrestris</i>) exposed to COUNTER-15G in artificial soils. ' \
             'Environ. Toxicol. Chem. 14(2): 279-285.' \
             '</p>' \
             '<p>' \
             'Mackay, D. and S. Paterson. 1981. Calculating fugacity. Environ. Sci. Technol. 15: 1006-1014.' \
             '</p>' \
             '<p>' \
             'USEPA. 2008. User\'s Guide: T-REX Version 1.4.1 (Terrestrial Residue Exposure model). United States ' \
             'Environmental Protection Agency. Environmental Fate and Effects Division.' \
             '</p>'
