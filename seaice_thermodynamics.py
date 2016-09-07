"""A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.
"""

# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

# --------------------------------------------------------------------
# CONTACT
#
# Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = '<NEED CONTACT>'

# --------------------------------------------------------------------
# AUTHORS
#
# Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = '<NEED AUTHORS>'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# PROCESS: DESCRIPTION
#
# Scientific context of the process
# --------------------------------------------------------------------
DESCRIPTION = 'Characteristics of sea ice thermodynamics processes'

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# Sets of details for the process
# --------------------------------------------------------------------
DETAILS = OrderedDict()

DETAILS['budget'] = (
    'str', '0.1',
    'Information required to close the thermodynamics budget')

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES
#
# Sets of discrete portions of the process
# --------------------------------------------------------------------
SUB_PROCESSES = OrderedDict()

SUB_PROCESSES['thermo_processes'] = {
    'description': 'Information about basal heat flux and brine inclusions',
    'details': ['details'],
}

SUB_PROCESSES['snow_processes'] = {
    'description': 'Snow processes in sea ice thermodynamics',
    'details': ['process_type'],
}

SUB_PROCESSES['vertical_heat_diffusion'] = {
    'description': 'Characteristics of vertical heat diffusion in sea ice.',
    'details': ['details'],
}

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES DETAILS
#
# Sets of details for the sub processes
# --------------------------------------------------------------------
SUB_PROCESS_DETAILS = OrderedDict()

SUB_PROCESS_DETAILS['thermo_processes:details'] = {
    'description': 'Information about basal heat flux and brine inclusions',
    'properties': [
        ('brine_inclusion_method', 'ENUM:thermo_brine_types', '0.1',
         'Method by which basal heat flux is handled'),
        ('basal_heat_flux', 'str', '0.1',
        'Method by which basal heat flux is handled'),
        ('brine_inclusions', 'str', '0.1',
         'Method by which brine inclusions are handled')
    ]
}

SUB_PROCESS_DETAILS['snow_processes:process_type'] = {
    'description': '<NEEDS DESCRIPTION>',
    'properties': [
        ('process_type', 'ENUM:snow_process_types', '1.N', 
             'Snow processes in sea ice thermodynamics')
    ]
}

SUB_PROCESS_DETAILS['vertical_heat_diffusion:details'] = {
    'description': 'Characteristics of vertical heat diffusion in sea ice.',
    'properties': [
        ('num_of_layers', 'int', '1.1',
         'Number of layers used for vertical heat diffusion'),
        ('regular_grid', 'bool', '0.1',
         'If multiple layers, are they regularly distributed?'),
        ('based_on_semtner', 'bool', '1.1',
         'Is method based on semtner 1976?')
    ]
}

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['thermo_brine_types'] = {
    'description': 'Brine Inclusion Methodology',
    'is_open': True,
    'members': [
        ('None', 'No brine inclusions included in sea ice thermodynamics'),
        ('Heat Reservoir', 'Brine inclusions treated as a heat reservoir'),
        ('Thermal Fixed Salinity', 'Thermal properties depend on S-T (with fixed salinity)'),
        ('Thermal Varying Salinity', 'Thermal properties depend on S-T (with varying salinity'),
    ]
}

ENUMERATIONS['snow_process_types'] = {
    'description': 'Types of snow processes',
    'is_open': True,
    'members': [
        ('single-layered heat diffusion', None),
        ('multi-layered heat diffusion', None),
        ('snow aging scheme', None),
        ('snow ice scheme', None),
    ]
}
