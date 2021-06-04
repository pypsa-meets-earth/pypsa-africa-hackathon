..
  SPDX-FileCopyrightText: 2021 The PyPSA meets Africa authors

  SPDX-License-Identifier: CC-BY-4.0

.. _installation:

##########################################
Contributing
##########################################

Contributions are welcome, and they are greatly appreciated! 
Every little bit helps, and credit will always be given. 

You can contribute on the code side in many ways:

- submit feedback,
- add new features,
- report bugs, 
- fix bugs, 
- implement a new cluster/cloud comuptation backend,
- write documentation

But we also have non-code related activities. 
If you are interested in these then have a look at the `project structure <https://pypsa-meets-africa.readthedocs.io/en/latest/project_structure_and_credits.html>`_ & click on the 'leader' position.
A pdf file will show up, introducing you to other activities in the roam of HR, finance to outreach.


.. _deps:

Code work packages
====================


In the code team we are working on 6 different work packages:
- WP1. Demand modelling
- WP2. Conventional generator modelling
- WP3. RES modelling
- WP4. Land coverage constraint modelling
- WP5. Network and substation modelling
- WP6. Data creation and validation

A conference paper describing each of the work packages in more detail is coming end of June 2021. You can write max.parzen(@ed.ac.uk) to receive a non-published preprint version.


.. _deps:

Possible contributions during the prototype development
=========================================================


You can join the work package development. Some examples of open tasks are:
- WP1. Implement GEGIS which applies a machine learning approach based on existing electricity demand time-seriesdata, population densities and spatially resolved income data
- WP1. Investigate how different demand timeseries could include the state of energy access
- WP2. Support powerplant matching activities to create a rich generator capacity dataset
- WP2. Implement LISFLOOD to add hydro-timerseries
- WP3. Set up Atlite for Africa to create renewable timeseries
- WP3. Add different concentrated solar power (CSP) designs to Atlite
- WP4. Assess how Atlite needs to be adjusted to constraint maximal installable renewable potential. For instance, it may be forbidden to install power plants in protective areas such as national parks or to build wind plants in cities
- WP5. Support creating a network topology by applying `various methods <https://github.com/pypsa-meets-africa/pypsa-africa/discussions/15>`_
- WP6. Contribute to the AI satellite image detection for energy asset recognition such `applied for detecting HV lines, substations <https://github.com/pypsa-meets-africa/pypsa-africa/discussions/13>`_ and power plants

.. image:: image/africa_osm_map.jpeg
  :width: 400
  :alt: Africa map


After the prototype development (or during with less priority)
----------------------------------------------------------------


- WP1. Improve and validate GEGIS in different country context
- WP2. Improve and validate LISFLOOD in different country context
- WP3. Investigate how and in what quality existing renewable capacities are included
- WP3. Add marine energy to Atlite
- WP4. Validate and extend Atlite capabilities
- WP5. Develop a heuristic to investigate if new east-west or north-west interconnectors within Africa are viable


.. _deps:

Example case studies after the prototype development 
=====================================================

Perform studies:
- **Long-term capacity expansion planning.** Explore long-term capacity expansion with different renewable energy deployments and different network constraints e.g. business-as-usual, least-cost, RE sub-optimally deployed in other areas/zones to assist just transition
- **Interconnectivity study.** Analysis on improved interconnectivity between African nations or improved interconnectivity between pool.
- **Energy storage study.** Value of short-duration vs long-duration storage in any country that is most appropriate. Could be interesting in any country where high variable renewable energy penetration may already be or is becoming part of the future energy mix.
- **Hydrogen economy.** Potentials of establishing an hydrogen economy in a future energy system. 
- **Energy access.** The impact on changing demand in Africa. Connecting islanded grids to the energy system - a cost and benefit analysis. 
- ...

After linking PyPSA-Africa with PyPSA-Eur/PyPSA-Eur-Sec
---------------------------------------------------------

- **Intercontinental energy planning study.** The value of collaboration between the EU and the African energy system.
- **Sector coupling.** The benefits of sector coupling in Africa.
- **Electric Vehicles.** Opportunities and pathways to integrate electric vehicles in Africa.
- ...



