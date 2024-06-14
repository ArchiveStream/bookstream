#!/usr/bin/env python

"""
Copyright(c)2009 Archive Stream. Software license AGPL version 3.

This file is part of bookstream.

    bookstream is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    bookstream is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with bookstream.  If not, see <http://www.gnu.org/licenses/>.
    
    The bookstream source is hosted at http://github.com/archivestream/bookstream/

>>> import catalog
>>> urn = 'urn:x-internet-archive:bookstream:catalog'
>>> c = catalog.Catalog(title='Archive Stream Catalog', urn=urn)

>>> l = catalog.Link(url  = 'http://archivestream.github.io/details/itemid',
...                  type = 'application/atom+xml')
>>> e = catalog.Entry({'urn'     : 'x-internet-archive:item:itemid',
...                    'title'   : u'test item',
...                    'updated' : '2009-01-01T00:00:00Z'}, links=[l])
>>> c.addEntry(e)

>>> start    = 0
>>> numFound = 2
>>> numRows  = 1
>>> urlBase  = '/alpha/a/'
>>> n = catalog.Navigation.initWithBaseUrl(start, numRows, numFound, urlBase)
>>> c.addNavigation(n)

>>> osDescription = 'http://archivestream.github.io/bookstream/catalog/opensearch.xml'
>>> o = catalog.OpenSearch(osDescription)
>>> c.addOpenSearch(o)

>>> r = catalog.output.CatalogToAtom(c)
>>> str = r.toString()

Different version of lxml will print xmlns differently (use ellipsis in doctest):

>>> print str.rstrip() #doctest: +ELLIPSIS
<feed ...
  <title>Archive Stream Catalog</title>
  <id>urn:x-internet-archive:bookstream:catalog</id>
  <updated>1970-01-01T00:00:00Z</updated>
  <link rel="self" type="application/atom+xml" href="http://archivestream.github.io/bookstream/catalog/"/>
  <author>
    <name>Archive Stream</name>
    <uri>http://www.archivestream.github.io</uri>
  </author>
  <link rel="search" type="application/opensearchdescription+xml" href="http://archivestream.github.io/bookstream/catalog/opensearch.xml"/>
  <link rel="next" type="application/atom+xml" href="/alpha/a/1" title="Next results"/>
  <entry>
    <title>test item</title>
    <id>x-internet-archive:item:itemid</id>
    <updated>2009-01-01T00:00:00Z</updated>
    <link href="http://archivestream.github.io/details/itemid" type="application/atom+xml"/>
  </entry>
</feed>


>>> h = catalog.output.CatalogToHtml(c)
>>> html = h.toString()
>>> # print html

>>> pubInfo = {
...    'name'     : 'Archive Stream',
...    'uri'      : 'http://www.archivestream.github.io',
...    'opdsroot' : 'http://archivestream.github.io/bookstream/catalog',
...    'mimetype' : 'application/atom+xml;profile=opds',
...    'urlroot'  : '/catalog',
...    'urnroot'  : 'urn:x-internet-archive:bookstream:catalog',
... }
>>> solrUrl = 'http://se.us.archivestream.github.io:8983/solr/select?q=mediatype%3Atexts+AND+format%3A(LuraTech+PDF)&fl=identifier,title,creator,oai_updatedate,date,contributor,publisher,subject,language,month&sort=month+desc&rows=50&wt=json'
>>> ingestor = catalog.ingest.IASolrToCatalog(pubInfo, solrUrl, urn)
>>> c = ingestor.getCatalog()
>>> print c._title
Archive Stream Catalog

"""

"""
bookstream/
    __init__.py
    
    catalog/
        __init__.py
        Catalog.py
        Entry.py
        Navigation.py
        OpenSearch.py
    
        ingest/
            __init__.py
            SolrToCatalog.py
            AtomToCatalog.py (future)

    output.py
        CatalogRenderer
        CatalogToAtom
        CatalogToHtml
        CatalogToJson (future)


>>> import bookstream.catalog as catalog
>>> c = catalog.Catalog()

>>> d = {'urn': 'x-internet-archive:item:itemid'}
>>> e = catalog.Entry(d)
>>> c.addEntry(e)

>>> nexturl = 'http://archivestream.github.io/bookstream/catalog/alpha/a/1'
>>> prevurl = None
>>> n = catalog.Navigation(nexturl, prevurl)
>>> c.addNavigation(n)

>>> osDescription = 'http://archivestream.github.io/bookstream/opensearch.xml'
>>> o = catalog.OpenSearch(osDescription)
>>> c.addOpenSearch(o)

>>> r = CatalogToXml()
>>> r.render(c)

"""

import catalog
import util

if __name__ == '__main__':
    import doctest
    doctest.testmod()
