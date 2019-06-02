========
Surimisp
========

Introduction
============

Surimisp is an indicator of compromise checker for Suricata and MISP. It fetches
IOC list from MISP and check them against Suricata events.

Installation
============

You can install dependcies via ::

 pip install -r requirements.txt

Then you can install via ::

 python setup.py install


Usage
=====

First edit `surimisp.conf` to add your MISP API key and adjust address
of your MISP instance.

You may also need to setup define one instance.

Then you can start `surimisp` via ::

 surimisp -c surimisp.conf

