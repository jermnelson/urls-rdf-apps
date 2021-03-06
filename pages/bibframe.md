title: BIBFRAME URLs from MARC
published: 2017-04-26
order: 0

Comparing the difference Library of Congress's MARC-to-BIBFRAME uses MARC
records to build out URLs has slightly changed between BIBFRAME 1.0 and the
2016 release of BIBFRAME 2.0. In each vocabulary version, the main tool uses
the MARC 001 field to generate URLs for all of the associated RDF Entities.

## Example MARC Record

<pre>
=LDR  00826nam  2200265Ia 4500
=001  13759163
=005  19860621153607.0
=008  860621s1918\\\\xx\\\\\\\\\\\\000\0\eng\d
=035  \\$a.b1000001x$btsco$c-
=035  \\$a(CoCC)1
=040  \\$cCOC
=049  \\$a[ColoRm]COCB
=050  \\$aHV639.W65
=090  \\$aHV639.W65
=110  2\$aWoman's Council of Defense for Colorado.
=245  10$aReport of the Woman's Council of Defense for Colorado :$bfrom November 30, 1917to November 30, 1918.
=260  \\$a[S.l. :$bs.n.],$c1918?
=300  \\$a112 p. ;$c24 cm.
=650  \0$aWorld War, 1914-1918.
=650  \0$aWomen$zColorado.
=907  \\$a.b1000001x
=902  \\$a170206
=999  \\$b1$c940803$dm$ea$f-$g0
=994  \\$atsco
=945  \\$aHV639.W65$g1$i33027000500011$j0$ltsco $h0$o-$p$0.00$r-$sh$t13$u0$v0$w0$x0$y.i1000001x$z940804
</pre>

Download the original MARC21 file [here](/static/data/cc-one.mrc).

## BIBFRAME 1.0
After announcing about a new linked-data based vocabulary to replace
MARC in 2011, the Library of Congress released the formal BIBFRAME specification 
[http://bibframe.org/](http://bibframe.org/) and an XQuery based tool for
transforming MARC to BIBFRAME 1.0 RDF.

The BIBFRAME 1.0 Vocabulary is diagrammed here at:

![BIBFRAME 1.0 Model](http://bibframe.org/static/images/bibframe.png)

### MARC Conversion 
Here is an example BF 1.0 Work in RDF Turtle Format using the 
[https://github.com/lcnetdev/marc2bibframe/](https://github.com/lcnetdev/marc2bibframe/) XQuery 
conversation tool:

<pre>
&lt;http://catalog.coloradocollege.edu/13759163&gt; a bf:Text,
        bf:Work ;
    bf:authorizedAccessPoint """Woman's Council of Defense for Colorado. 
    Report of the Woman's Council of Defense for Colorado : from November 30, 1917
    to November 30, 1918.Report of the Woman's Council of Defense for Colorado :from 
    November 30, 1917to November 30, 1918""",
   "womanscouncilofdefenseforcoloradoreportofthewomanscouncilofdefenseforcoloradofromnovember301917tonovember301918work"@x-bf-hash ;
    bf:classification &lt;http://catalog.coloradocollege.edu/13759163classification11&gt; ;
    bf:classificationLcc &lt;http://id.loc.gov/authorities/classification/HV639.W65&gt; ;
    bf:creator &lt;http://catalog.coloradocollege.edu/13759163organization6&gt; ;
    bf:language &lt;http://id.loc.gov/vocabulary/languages/eng&gt; ;
    bf:subject &lt;http://catalog.coloradocollege.edu/13759163topic8&gt;,
        &lt;http://catalog.coloradocollege.edu/13759163topic9&gt; ;
    bf:workTitle &lt;http://catalog.coloradocollege.edu/13759163title5&gt; .

</pre>
Download the RDF Turtle file [here](/static/data/cc-one-bf1.ttl).


In the original MARC record, the **13759163** value in the control number field [001](http://www.loc.gov/marc/bibliographic/bd001.html) 
is used to construct a URL from a
base URL of `http://catalog.coloradocollege.edu/` for a new BIBFRAME Work URL of 
`http://catalog.coloradocollege.edu/13759163`. Subsequent URLs for different RDF BIBFRAME Entites
are generated by appending the Class name of the BIBFRAME class followed by a counter:

*  `http://catalog.coloradocollege.edu/13759163organization6` a BIBFRAME 1.0 Organization and has
    the following RDF Turtle representation:
    <pre>
&lt;http://catalog.coloradocollege.edu/13759163organization6&gt; a bf:Organization ;
    bf:authorizedAccessPoint "Woman's Council of Defense for Colorado." ;
    bf:hasAuthority [ a madsrdf:Authority ;
            madsrdf:authoritativeLabel "Woman's Council of Defense for Colorado." ] ;
    bf:label "Woman's Council of Defense for Colorado." .
    </pre>
*   `http://catalog.coloradocollege.edu/13759163topic8` is a bf:Topic and has a limited
    authority control through the `bf:hasAuthority` link back to the Library of Congress
    Linked Data ID service.
    <pre>
&lt;http://catalog.coloradocollege.edu/13759163topic8&gt; a bf:Topic ;

    bf:authorizedAccessPoint "World War, 1914-1918" ;
    bf:hasAuthority [ a madsrdf:Authority,
                madsrdf:Topic ;
            madsrdf:authoritativeLabel "World War, 1914-1918" ;
            madsrdf:isMemberOfMADSScheme &lt;http://id.loc.gov/authorities/subjects&gt; ] ;
    bf:label "World War, 1914-1918" .
    </pre>
    Note that this subject's authority control doesn't include a direct link to the
    URL for this subject heading located at `http://id.loc.gov/authorities/subjects/sh85148236`.




## MARC to BIBFRAME 2.0
In 2016 the Library of Congress released version 2.0 of BIBFRAME (a list of differences is 
[available](http://www.loc.gov/bibframe/docs/bibframe2-whatsnew.html)). Here is a graphical overview of
the BIBFRAME 2.0 model:

![BIBFRAME 2.0 Model](http://www.loc.gov/bibframe/docs/images/bf2-model.jpg)  

A replacement 
for the Library of Congress tool for converting MARC XML to BIBFRAME 2.0 RDF XML using XSLT transformation
scripts and is hosted on Github at 
[https://github.com/lcnetdev/marc2bibframe2](https://github.com/lcnetdev/marc2bibframe2).

The basic URL pattern used in the default XSL transformation from MARC XML is again based on the value 
in the [001 field](http://www.loc.gov/marc/bibliographic/bd001.html) with a URL fragment starting with the
pound sign (**\#**) followed by a primary BIBFRAME class. Instead of
using a simple counter, the `marc2bibframe2` XSL adds the MARC field tag followed by a XSLT position() function
call that returns an integer. 
The MARC example record XML transforms into a BIBFRAME Work `http://catalog.coloradocollege.edu/13759163#Work` 
URI.


<pre>
&lt;http://catalog.coloradocollege.edu/13759163#Work&gt; a bf:Text,
        bf:Work;
    rdfs:label "Report of the Woman's Council of Defense for Colorado : from November 30, 1917to November 30, 1918." ;
    bf:adminMetadata [ a bf:AdminMetadata ;
            bflc:encodingLevel [ a bflc:EncodingLevel ;
                    bf:code "u" ] ;
            bf:changeDate "1986-06-21T15:36:07"^^xsd:dateTime ;
            bf:creationDate "1986-06-21"^^xsd:date ;
            bf:descriptionConventions [ a bf:DescriptionConventions ;
                    bf:code "aacr" ] ;
            bf:identifiedBy [ a bf:Local ;
                    rdf:value "13759163" ] ;
            bf:source [ a bf:Agent,
                        bf:Source ;
                    rdfs:label "COC" ] ;
            bf:status [ a bf:Status ;
                    bf:code "n" ] ] ;
    bf:classification [ a bf:ClassificationLcc ;
            bf:classificationPortion "HV639.W65" ] ;
    bf:contribution [ a bflc:PrimaryContribution,
                bf:Contribution ;
            bf:agent &lt;http://catalog.coloradocollege.edu/13759163#Agent110-11&gt; ;
            bf:role &lt;http://id.loc.gov/vocabulary/relators/ctb&gt; ] ;
    bf:hasInstance &lt;http://catalog.coloradocollege.edu/13759163#Instance&gt; ;
    bf:language &lt;http://id.loc.gov/vocabulary/languages/eng&gt; ;
    bf:subject &lt;http://catalog.coloradocollege.edu/13759163#Topic650-15&gt;,
        &lt;http://catalog.coloradocollege.edu/13759163#Topic650-16&gt; ;
    bf:title [ a bf:Title ;
            rdfs:label "Report of the Woman's Council of Defense for Colorado : from November 30, 1917to November 30, 1918." ;
            bflc:titleSortKey "Report of the Woman's Council of Defense for Colorado : from November 30, 1917to November 30, 1918." ;
            bf:mainTitle "Report of the Woman's Council of Defense for Colorado" ;
            bf:subtitle "from November 30, 1917to November 30, 1918" ] .
</pre>
Download the RDF Turtle file [here](/static/data/cc-one-bf2.ttl).

*   `http://catalog.coloradocollege.edu/13759163#Agent110-11` is a BIBFRAME 2.0 Organization and Agent with a contribution 
    role to the above `http://catalog.coloradocollege.edu/13759163#Work` BIBFRAME Work URI with the final fragment part of the URI
    references in part the record's [MARC 110](http://www.loc.gov/marc/bibliographic/bd110.html) field and an integer of 11
    from this snippet in the [XSL](https://github.com/lcnetdev/marc2bibframe2/blob/master/xsl/ConvSpec-1XX%2C6XX%2C7XX%2C8XX-names.xsl) 
    `<xsl:value-of select="position()"/>`. 
    <pre>
&lt;http://catalog.coloradocollege.edu/13759163#Agent110-11&gt; a bf:Agent,
        bf:Organization ;
    rdfs:label "Woman's Council of Defense for Colorado." ;
    bflc:name10MarcKey "1102 $aWoman's Council of Defense for Colorado." ;
    bflc:name10MatchKey "Woman's Council of Defense for Colorado." ;
    bflc:primaryContributorName10MatchKey "Woman's Council of Defense for Colorado." .
    </pre>

*   `http://catalog.coloradocollege.edu/13759163#Topic650-15` a BIBFRAME 2.0
    topic URI generated from the MARC [650](http://www.loc.gov/marc/bibliographic/bd650.html) and an integer of 
    15 reflecting the XSL `position()` function call. Like in the BIBFRAME 1.0 conversion the final step would
    be preform a controlled look-up to an external Authority, in this case Library of Congress Subject heading
    and resolve to `http://id.loc.gov/authorities/subjects/sh85148236`. 
    <pre>
&lt;http://catalog.coloradocollege.edu/13759163#Topic650-15&gt; a bf:Topic,
        madsrdf:Topic ;
    rdfs:label "World War, 1914-1918." ;
    bf:source [ a bf:Source ;
            bf:code "lcsh" ] ;
    madsrdf:authoritativeLabel "World War, 1914-1918." ;
    madsrdf:isMemberofMADSScheme &lt;http://id.loc.gov/authorities/subjects&gt; .

