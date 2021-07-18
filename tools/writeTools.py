import lxml.etree as etree
import xml.etree.ElementTree as ET

import json

'''
class WriteTools(object):
    
    def __init__(self, dataRep, filename):
        self.dataRep = dataRep
        self.filename = filename

    @property
    def dataRep(self):
        return self._dataRep
    
    @property
    def filename(self):
        return self._filename

    @dataRep.setter
    def dataRep(self, dataRep):
        self._dataRep = dataRep
    
    @filename.setter
    def filename(self, filename):
        self._filename = filename
'''

def toThermoML(dataRep, filename):
    attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    nsmap = {None: 'http://www.iupac.org/namespaces/ThermoML', 'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}
    DataReport = etree.Element("DataReport", {attr_qname: "http://www.iupac.org/namespaces/ThermoML ThermoML.xsd"}, nsmap=nsmap)
    
    DataReport = __createVersion(DataReport, dataRep)
    DataReport = __createCitation(DataReport, dataRep)
    ET.dump(DataReport)
    __writeFile(DataReport, filename)

def __createVersion(DataReport, dataRep):
    
    Version = etree.SubElement(DataReport, 'Version')
    nVersionMajor = etree.SubElement(Version, 'nVersionMajor')
    nVersionMajor.text = '4'
    nVersionMinor = etree.SubElement(Version, 'nVersionMinor')
    nVersionMinor.text = '0'

    return DataReport

def __createCitation(DataReport, dataRep):
    Citation = etree.SubElement(DataReport, 'Citation')
    for i in range(len(dataRep['authors'])):
        sAuthor = etree.SubElement(Citation, 'sAuthor')
        sAuthor.text = dataRep['authors'][i]
    sDOI = etree.SubElement(Citation, 'sDOI')
    sDOI.text = dataRep['_DOI']
    sTitle = etree.SubElement(Citation, 'sTitle')
    sTitle.text = dataRep['_title']
    return DataReport

def __createCompound(DataReport, dataRep):
    pass

def __writeFile(DataReport, filename):
    convertedString = etree.tostring(DataReport, pretty_print=True, xml_declaration=True, encoding="utf-8")
    file = open(filename + '.xml', 'wb')
    file.write(convertedString)
    file.close()
