title: REST APIs and URLs
published: 2017-04-26
order: 3 

REST (short for representational state transfer) is an API design pattern based
around web native technologies like HTTP verbs and URLs. REST APIs are a way to access and manage web resources using
stateless operations like Read, Add, Modify, and Delete. In developing RDF Application APIs,
REST operations are mapped to the common HTTP Verbs of GET, POST, PUT, and DELETE for URLs.


<blockquote class="blockquote bg-default">
<p>&hellip; a RESTful API ends up being simply a collection of URIs, HTTP 
calls to those URIs and some JSON and/or XML representations of resources, 
many of which will contain relational links. The RESTful principal of 
addressability is covered by the URIs. Each resource has its own address or 
URI—every interesting piece of information the server can provide is exposed 
as a resource. The constraint of uniform interface is partially addressed by the 
combination of URIs and HTTP verbs, and using them in line with the standards 
and conventions.</p>
<p>
In deciding what resources are within your system, name them as nouns as opposed 
to verbs or actions. In other words, a RESTful URI should refer to a resource 
that is a thing instead of referring to an action.
</p>
</blockquote>
From *[REST API Tutorial](/urls-rdf-apps/help#ref-5)*


## BIBCAT RDF Applications
The development roadmap for the [BIBCAT](https://bibcat.org/) and it's supporting 
[RDF Framework][RDFW] includes an proof-of-concept REST API for RDF entities.
This work has been challenging because in RDF applications that
depend heavily on a triplestore with arbitrary depth of blank-nodes and relationships,
your API must be able to manipulate the data at the 
triple granularity that is not required at the MARC record-level manipulation 
as done by most ILS. 

Regardless of how the URI is generated, accessing and managing the RDF predicates and objects
that relate to the subject Resource is how the design and implementation of the 
[RDF Framework][RDFW]. For RDF Applications built using the [RDF Framework][RDFW], a Application is 
defined in RDF triples that power a single API for use directly by other applications or
generate a HTML5 form interface for manipulation by authorized and authenticated users.

### Alliance BIBCAT Pilot
![Colorado Alliance of Research Libraries Logo](http://intro2libsys.info/code4lib-2017/static/images/coalliance-logo.png)

For the [Colorado Alliance BIBCAT Pilot Project][ALLIANCE_BC] focuses
on a sitemap index for search engines that provide landing pages for each BIBFRAME Instance
with embedded [schema.org](http://schema.org/) JSON-LD. This [project][ALLIANCE_BC]
command-line utilities for ingesting MARC XML into BIBFRAME RDF triples. For the
scope of this project, the public REST API is restricted to GET verbs for accessing these
BIBFRAME URLs.


### Plains2Peaks DP.LA Regional Service Hub
![Plains2Peak Temporary Logo](http://intro2libsys.info/code4lib-2017/static/images/plains2peaks-tmp-logo.png)

In the [Plains2Peaks Collective][P2P_COL] regional service hub follows similar restrictions 
as the [Alliance BIBCAT Pilot][ALLIANCE_BC] where we building a REST API that is restricted
to the GET access through a [ResourceSync](http://www.openarchives.org/rs/toc) feed that 
resolves to [Plains2Peaks][P2P_COL] BIBFRAME Instance URLs that output the DP.LA MAPv4 
JSON-LD.
 
As the [RDF Framework][RDFW] API support matures, we'll offer full support for all of the
REST HTTP verbs including POST, PATCH, and DELETE.

## REST Verbs with Fedora
The Fedora Repository has had a REST API for a number years starting with their 3.x
series. Fedora 4 goes further and has working towards full compliance of the W3C's
[Linked Data Platform](https://www.w3.org/TR/ldp/) specification.

## NISO eContent API Working Group
As a member of the [NISO eContent API Working Group](http://www.niso.org/news/pr/view?item_key=e18a9742103bc945868a51a1e196e62b68879df6),
we are tasked with coming up with a REST API for eContent that includes many of the common 
ILS functions and is based around Queens Public Library's draft [API Requirements Document for e-Content Partners](http://virtuallibrary.queenslibrary.org/sites/default/files/library-api-draft/Library-Webservice-API-Specification-Draft-V1_4.pdf):

*  Checking Out Items
*  Streaming media to authenticating users
*  Hold/Request Items and being able to Cancel Holds
*  Item Availability  

Adding these requirements as a REST API for selected BIBFRAME Entities in BIBCAT
is the planned focus for a development sprint in the summer of 2017 with a pilot
for NISO testing in fall.

[ALLIANCE_BC]: http://bibcat.coalliance.org/
[P2P_COL]: https://plains2peaks.org/
[RDFW]: http://knowledgelinks.io/products/rdfframework/
