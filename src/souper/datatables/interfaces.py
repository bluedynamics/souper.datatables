from zope.interface import Interface


class IDataTable(Interface):
    """
    Basic methods to deal with jQuery datatables with souper.soup
    """
    def column_info(self):
        """
        info about the avaiable columns. It is a list with a dictionary that contains
        information about each column

        col_info['label'] = is the columnheader displayed
        col_info['sortable'] = boolean value to describe if the column is sortable
        col_info['searchable'] = boolean value to describe if the column itself is searchable
        col_info['sortindex'] = default value is None. If none indexname equals the rowid
        else this index is taken for sorting.
        """

    def extract_parameters(self):
        """
        provides the default parameters for the columns, needed by jQuery
        They split up in the basic infos such as 'echo': '1', 'search': '',
        'slicelength': 10, 'slicestart': 0 and in the info for each column itself. 
        These are stored like that:
        {0: {'dataprop': '0',        <-- first column
         'regex': False,
         'search': '',
         'searchable': True,
         'sortable': True},
         1: {'dataprop': '1',        <-- second column
         'regex': False,
         'search': '',
         'searchable': True,
         'sortable': True},          <-- and so on
        """

    def get_form(self):
        """
        get the form parameters as a dictionary
        """
