title: SEO Aware URIs
published: 2017-04-26
order: 2

The importance of creating URLs that are favored for human consumption
has become more important, particularly as requirements are pulled from
the Colorado Alliance of Research Libraries BIBCAT project. Reading 
[Cool URIs don't change][REF2] by Sir Tim Berners-Lee in date of 2001. 
Google's recommendations for [structuring URLs]("#ref-2") emphasizes simple
URLs that are constructed in a logical fashion, with readable words, and 
using hyphens for punctuation. 

## Slugify Pattern
In building the first iterations of the Aristotle Discovery Layer (the 
latest iteration drives Colorado College's Digital Repository interface
at (https://digitalccbeta.coloradocollege.edu) with the web publishing 
[Django][DJGO] platform, I liked that [Django][DJGO] provides a function 
called [slugify](https://docs.djangoproject.com/en/1.11/ref/utils/#django.utils.text.slugify) for creating a 
SEO friendly url. While I no longer actively develop in [Django][DJGO],
I still use this basic regular expression function in many of my projects.

<pre>&gt;&gt;&gt; import re
&gt;&gt;&gt; def slugify(value):
    """
    Converts to lowercase, removes non-word characters (alphanumerics and
    underscores) and converts spaces to hyphens. Also strips leading and
    trailing whitespace.
    """
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)
&gt;&gt;&gt; print(slugify("A Midsummer Night's Dream"))
a-midsummer-nights-dream
</pre>

## Wikipedia Pattern
[Wikipedia ](https://en.wikipedia.org) uses a different URL pattern where spaces in the title are replaced with underscores
(**_**) while keep other punctuation like single and double quotes. Here is an example: 
[https://en.wikipedia.org/wiki/A_Midsummer_Night's_Dream](https://en.wikipedia.org/wiki/A_Midsummer_Night's_Dream)


## Conclusions
*   The more I develop applications, starting with human recognizable, canonical 
    URLs has trade-offs but I'm more often supporting search engine optimizations
*   Speak

## References
1.  <a id="ref-1"></a>Coyle, K. *On the Web, of the Web* LITA 2011 Keynote, October 1, 2011. Accessed
    [http://www.kcoyle.net/presentations/lita2011.html](http://www.kcoyle.net/presentations/lita2011.html)
1.  <a id="ref-2"></a> *Keep a simple URL structure*. Accessed 
    [https://support.google.com/webmasters/answer/76329](https://support.google.com/webmasters/answer/76329)
1.  <a id="ref-3"></a> *Use canonical URLs*. Accessed
    [https://support.google.com/webmasters/answer/139066](https://support.google.com/webmasters/answer/139066) 
1.  <a id="ref-4"></a> Fishkin, R. *15 SEO Best Practices for Structuring URLs*. February 24, 2015.
    Accessed [https://moz.com/blog/15-seo-best-practices-for-structuring-urls](https://moz.com/blog/15-seo-best-practices-for-structuring-urls)

[DJGO]: https://www.djangoproject.com/
[REF2]: https://www.w3.org/Provider/Style/URI
