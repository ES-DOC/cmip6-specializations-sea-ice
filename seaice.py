"""A realm sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.
"""

# --------------------------------------------------------------------
# CONTACT
#
# Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Ruth Petrie'

# --------------------------------------------------------------------
# AUTHORS
#
# Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Ruth Petrie, Bryan Lawrence, David Hassell'

# --------------------------------------------------------------------
# CONTRIBUTORS
#
# Set to realm specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = '&lt;NEED CONTRIBUTORS&gt;'

# --------------------------------------------------------------------
# CHANGE HISTORY
#
# Set to list: (version, date, comment, who).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
	("0.1.0", "2016-05-24", "Initialised", "David Hassell"),
	("0.1.1", "2016-09-28", "Modified seaice_grid", "Ruth Petrie"),
	("0.1.1", "2016-09-28", "Added seaice_key_properties.py as a copy from ocean MUST update for sea ice", "Ruth Petrie")	
     ]

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# REALM: DESCRIPTION
#
# Scientific context of this scientific realm
# --------------------------------------------------------------------
DESCRIPTION = 'Sea-ice realm specialization'

# --------------------------------------------------------------------
# REALM: REALM
#
# Canonical name for the domain of this scientific realm
# --------------------------------------------------------------------
REALM = 'seaice'

# --------------------------------------------------------------------
# REALM: GRID
#
# The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'seaice_grid'

# --------------------------------------------------------------------
# REALM: KEY PROPERTIES
#
# Key properties for the domain which differ from model defaults
# (grid, timestep etc)
# --------------------------------------------------------------------
KEY_PROPERTIES = 'seaice_key_properties'

# --------------------------------------------------------------------
# REALM: PROCESSES
#
# Processes simulated within the realm
# --------------------------------------------------------------------
PROCESSES = [
    'seaice_dynamics',
    'seaice_thermodynamics',
    'seaice_radiative_processes',
]
