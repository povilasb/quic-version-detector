==========
Change Log
==========

All notable changes to this project will be documented in this file.
This project adheres to `Semantic Versioning <http://semver.org/>`_.

[0.2.0] - 2016-07-08
====================

Added
-----

* Request timeout. Version detector won't wait for response forever anymore.

Changed
-------

* Use asyncio to send UDP requests.
* Send multiple QUIC queries - should improve the possibility to get a response.

[0.1.1] - 2016-05-31
====================

Added
-----

* Initial working version.
