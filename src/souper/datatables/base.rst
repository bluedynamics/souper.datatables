
Test of extract_parameters
==========================

Create a mock Class returning Mockforminfo:: 

    >>> from souper.datatables.base import DataTable
    >>> class MockDataTable(DataTable):
    ...     def __init__(self, form):
    ...         self.form = form 
    ...     def get_form(self):
    ...         return self.form

instanciate mock Instance with the basic column parameters:: 
    
    >>> mock = MockDataTable({'sSearch': '', 'sEcho': '1', 'iColumns': '4',
    ...                       '_': '1348051573178', 'iDisplayLength': '10', 
    ...                       'iDisplayStart': '0', 'sColumns': '', 
    ...                       'bRegex': 'false', 'iSortingCols': '0'})
    >>> pprint(mock.extract_parameters())
    {'col_count': 0,
     'col_displayed': 4,
     'col_name': '',
     'col_regexfilter': False,
     'col_sortedon': 0,
     'echo': '1',
     'search': '',
     'slicelength': 10,
     'slicestart': 0}

instanciate mock Instance with variable amount of column parameters:: 

    >>> mock = MockDataTable({'bSearchable_2': 'true', 'bSearchable_3': 'true', 
    ...                       'bSearchable_0': 'true', 'bSearchable_1': 'true', 
    ...                       'bSortable_0': 'true', 'bSortable_1': 'true', 
    ...                       'bSearchable_4': 'true', 'bSearchable_5': 'false', 
    ...                       'mDataProp_2': '2', 'bSortable_4': 'true', 
    ...                       'bSortable_2': 'true', 'bSortable_3': 'true', 
    ...                       'bSortable_5': 'false', 'sSearch': '', 'sEcho': '1', 
    ...                       'iColumns': '6', '_': '1348050938567', 
    ...                       'iDisplayLength': '10', 'sSearch_5': '', 
    ...                       'sSearch_4': '', 'sSearch_3': '', 'sSearch_2': '', 
    ...                       'sSearch_1': '', 'sSearch_0': '', 'mDataProp_4': '4', 
    ...                       'mDataProp_5': '5', 'mDataProp_0': '0', 
    ...                       'mDataProp_1': '1', 'iDisplayStart': '0', 
    ...                       'mDataProp_3': '3', 'bRegex_2': 'false', 
    ...                       'bRegex_3': 'false', 'bRegex_0': 'false', 
    ...                       'bRegex_1': 'false', 'bRegex_4': 'false', 
    ...                       'bRegex_5': 'false', 'sColumns': '', 
    ...                       'bRegex': 'false', 'iSortingCols': '0'})
    >>> pprint(mock.extract_parameters())
    {0: {'dataprop': '0',
         'regex': False,
         'search': '',
         'searchable': True,
         'sortable': True},
     1: {'dataprop': '1',
         'regex': False,
         'search': '',
         'searchable': True,
         'sortable': True},
     2: {'dataprop': '2',
         'regex': False,
         'search': '',
         'searchable': True,
         'sortable': True},
     3: {'dataprop': '3',
         'regex': False,
         'search': '',
         'searchable': True,
         'sortable': True},
     4: {'dataprop': '4',
         'regex': False,
         'search': '',
         'searchable': True,
         'sortable': True},
     5: {'dataprop': '5',
         'regex': False,
         'search': '',
         'searchable': False,
         'sortable': False},
     'col_count': 6,
     'col_displayed': 6,
     'col_name': '',
     'col_regexfilter': False,
     'col_sortedon': 0,
     'echo': '1',
     'search': '',
     'slicelength': 10,
     'slicestart': 0} 
 

Test of get_json_results
========================
Prepare enviroment

:: 
    >>> from zope.interface import implementer
    >>> from zope.component import provideUtility
    >>> from repoze.catalog.catalog import Catalog
    >>> from repoze.catalog.indexes.field import CatalogFieldIndex
    >>> from souper.soup import NodeAttributeIndexer       
    >>> from souper.interfaces import ICatalogFactory
    >>> @implementer(ICatalogFactory)
    ... class MySoupCatalogFactory(object):
    ...
    ...     def __call__(self, context=None):
    ...         catalog = Catalog()
    ...         indexer = NodeAttributeIndexer('nick')
    ...         catalog[u'nick'] = CatalogFieldIndex(indexer)
    ...         indexer = NodeAttributeIndexer('name')
    ...         catalog[u'name'] = CatalogFieldIndex(indexer)   
    ...         return catalog
    
    >>> provideUtility(MySoupCatalogFactory(), name="mysoup")
    >>> from souper.soup import get_soup
    >>> soup = get_soup('mysoup', layer['storage'])


    >>> from souper.soup import Record
    >>> rec = Record()
    >>> rec.attrs['nick']='klausi'
    >>> rec.attrs['name']='Klaus von brandli'    
    >>> soup.add(rec)
    >>> rec = Record()
    >>> rec.attrs['nick']='willi'
    >>> rec.attrs['name']='wonka'    
    >>> soup.add(rec)    
    >>> rec = Record()
    >>> rec.attrs['nick']='willi'
    >>> rec.attrs['name']='wurmi'    
    >>> soup.add(rec) 
    >>> rec = Record()
    >>> rec.attrs['nick']='herbert'
    >>> rec.attrs['name']='herbert beherbergt'    
    >>> soup.add(rec)         
    >>> rec = Record()
    >>> rec.attrs['nick']='klausi'
    >>> rec.attrs['name']='Klaus von brandli'    
    >>> soup.add(rec) 
    >>> rec = Record()
    >>> rec.attrs['nick']='willi'
    >>> rec.attrs['name']='oompa loompa'    
    >>> soup.add(rec) 
    
Create a Mock Class::

    >>> class MockDataTable(DataTable):
    ...     def __init__(self, params, query):
    ...         self.params = params 
    ...     def extract_parameters(self):
    ...         return self.params
    ...     def query_builder(self):
    ...         return self.query


Create a query::
    >>> from repoze.catalog.query import Eq, Or
    >>> result = soup.query())

    
Create Mock Object::
    
    >>> mock = MockDataTable({}, Or(Eq('nick', 'klausi'), Eq('name', 'Klaus von brandli'))

    >>> interact(locals())