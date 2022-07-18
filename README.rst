a tool to convert json to xml

-------

Usage
-----
Install with pip:

    pip install json2xml


use Json2Xml class to convert json to xml


.. code:: python

    from json2xml import Json2Xml
    d={
            "name": "John",
            "age": 30,
            "cars": [{"name": "Ford"}],
            "family": "johnson",
        }
    result = json2xml(d)
    print(result)

.. code:: xml

    <name>John</name>
    <age>30</age>
    <cars>
        <name>Ford</name>
    </cars>
    <family>johnson</family>

"""


License
-------

json2xml is released under the MIT License. See the bundled `LICENSE`_ file
for details.
