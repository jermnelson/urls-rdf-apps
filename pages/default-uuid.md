title: Default UUID for URIs
published: 2017-04-06
order: 1

Since about 2012 or so, my preferred practice for generating URIs
in bibliographic and linked-data applications is to use a combination 
of a base URL followed by a random or pseudo-random universally unique 
identifier or UUID.

## Colorado College Knowledge Graph

<pre>
&lt;http://catalog.coloradocollege.edu/6dc97f06-7080-11e6-ae7e-005056c00008&gt; a schema:EducationalEvent ;
    rdfs:label "Academic Year 2016-2017"@en ;
    schema:endDate "2017-05-22T07:00:00" ;
    schema:startDate "2016-08-29T06:00:00" ;
    cc_info:graduation [ rdfs:label "Summer 2017"@en ;
            rdf:value "2017-07" ],
        [ rdfs:label "Fall 2016"@en ;
            rdf:value "2016-12" ],
        [ rdfs:label "Spring 2017"@en ;
            rdf:value "2017-05" ] .
</pre>

## Colorado Alliance BIBCAT Project
In the first build-measure-learn (BML) iteration of the Colorado Alliance of 
Research Libraries BIBCAT project, BIBFRAME Instance IRI were generated using
a base URL of `http://bibcat.coalliance.org/` followed by a UUID using the
default `uuid.uuid1` Python method for generating a UUID from the hardware
address of the machine running the module and a random sequence number.

<pre>&gt;&gt;&gt; import uuid
&gt;&gt;&gt; print(uuid.uuid1())
942de50a-29f8-11e7-b1d6-005056c00008
</pre>

## In Fedora Commons
The digital preservation project [Fedora](http://fedorarepository.org/) uses
UUIDs extensively for URLs that are used to store datastreams and metadata. A possible use with
MARC cataloged object in Fedora would be to provide a value for subfield u in a [MARC 856](http://www.loc.gov/marc/bibliographic/bd856.html)
field.

Although the default URL minter in Fedora uses UUIDs, a [Custom URL minter](https://wiki.duraspace.org/display/FEDORA471/Configuring+an+External+PID+Minter)
can be be created that generates URLs from a specific pattern.

![Fedora Repository Container Object](/static/img/fedora-container.png)
