title: REST APIs and URLs
published: 2017-04-26
order: 3 

REST for representational state transfer are a way to access and manage web resources using
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
[RDF Framework](https://github.com/KnowledgeLinks/rdfframework) include a robust 
REST API for RDF entities. This work is challenging because in RDF applications that
depend heavily on a triplestore, your API must be able to manipulate the data at the 
triple granularity and not at the MARC record-level as done by most ILS. 

## REST Verbs with Fedora
The Fedora Repository has had a REST API for a number years starting with their 3.x
series. Fedora 4 goes further and has working towards full compliance of the W3C's
[Linked Data Platform](https://www.w3.org/TR/ldp/) specification.

## NISO eContent API Working Group
