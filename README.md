# house-energy-api
An API for getting potential energy savings for housing. Note, this is a very Q&D fix to deal with a last minute change in the data supplied. The data is also in a bit of crazy format, so we've normalised it a bit, and fixed the field names to be a bit more software-friendly. 

By default, this API servers on port 5008 but this can be changed using env variable NRG_PORT - e.g.

    export NRG_PORT=5008
    
To run this, you need to pip install all the imports listed in requirements.txt then run:

    python nrg.py

A typical query would be:

    127.0.0.1:5008/building?uprn=10090470558&uprn=10003317419

If you want to take a walk on the wild side, we can also return the flat, denormalised stuff:

    127.0.0.1:5008/building_denormalised?uprn=10090470558&uprn=10003317419


OpenAPI docs are at:

    127.0.0.1:5008/docs

(that's from localhost, obviously). You can keep adding UPRNS, but of course the data is going to get bigger and bigger

copyright Telicent Ltd 2023, all rights reserved