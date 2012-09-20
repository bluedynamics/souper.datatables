from .interfaces import IDataTable
from zope.interface import implementer


@implementer(IDataTable)
class DataTable(object):

    def get_soup_name(self):
        raise NotImplementedError()

    def column_info(self):
        raise NotImplementedError()

    def query_builder(self):
        raise NotImplementedError()

    def get_form(self):
        raise NotImplementedError()
    
    def extract_parameters(self):
        info = {}
        form = self.get_form()

        info['search'] = form['sSearch']
        info['echo'] = form['sEcho']
        info['slicestart'] = int(form['iDisplayStart'])
        info['slicelength'] = int(form['iDisplayLength'])
        info['col_displayed'] = int(form['iColumns'])
        info['col_name'] = form['sColumns']
        info['col_regexfilter'] = form['bRegex'] == 'true'
        info['col_sortedon'] = int(form['iSortingCols'])

        idx = 0

        while 'bSortable_%d' % idx in form:
            info[idx] = {}
            info[idx]['sortable'] = form['bSortable_%d' % idx] == 'true'
            info[idx]['regex'] = form['bRegex_%d' % idx] == 'true'
            info[idx]['searchable'] = form['bSearchable_%d' % idx] == 'true'
            info[idx]['dataprop'] = form['mDataProp_%d' % idx]
            info[idx]['search'] = form['sSearch_%d' % idx]

            idx += 1

        info['col_count'] = idx
        return info



    def get_json_result(self):
        params = self.extract_parameters()
        query = self.query_builder()
        #execute query consider sort
        #slice results
        #build jQuery lookalike datastructure from results (see pfg.soup)
        #return datastructure as json

