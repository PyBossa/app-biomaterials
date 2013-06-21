PyBossa Biomaterials Application
================================

Why?
----
As researchers, we are developing new materials for targeted drug delivery and tissue engineering.

How?
----
We create materials comprised of proteins through genetic engineering and molecular biology. While we use the structural elements found in natural proteins, we stitch them together in ways not found in nature thereby generating new protein materials.

How you can help
----------------
We need you to characterize these new materials. For example, you might identify their size, shape and amount.

Will your help make a difference?
---------------------------------

Absolutely! The size, shape and amount of the newly created materials that you have identified are essential. In short, you will help to cure cancers, treat osteoarthritis, and fabricate new tissues!


This application has three files:

*  createTasks.py: for creating the application in PyBossa, and fill it with some tasks.
*  template.html: the view for every task and deal with the data of the answers.
*  tutorial.html: a simple tutorial for the volunteers.

![alt screenshot](http://i.imgur.com/7JNQ9di.png)

Testing the application
=======================

You need to install the pybossa-client first (use a virtualenv):

```bash
    $ pip install pybossa-client
```
Then, you can follow the next steps:

*  Create an account in PyBossa
*  Copy under your account profile your API-KEY
*  Run python createTasks.py -u http://crowdcrafting.org -k API-KEY
*  Open with your browser the Applications section and choose the biomaterials app. 
This will open the presenter for this application.

Documentation
=============

We recommend that you read the section: [Build with PyBossa](http://docs.pybossa.com/en/latest/build_with_pybossa.html) and follow the [step by step tutorial](http://docs.pybossa.com/en/latest/user/tutorial.html).

**NOTE**: This application usses the [pybossa-client](https://pypi.python.org/pypi/pybossa-client) in order to simplify the development of the application and its usage. Check the [documentation](http://pythonhosted.org/pybossa-client/).


LICENSE
=======

Please, see the COPYING file.


Acknowledgments
===============
The thumbnail has been created using a tile from a dataset supplied by Jin K.
Montclare, PhD (Associate Professor, Chemical and Biomolecular Engineering, Polytechnic Institute of New York University).
