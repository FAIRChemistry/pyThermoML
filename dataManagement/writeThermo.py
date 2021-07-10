import lxml.etree as etree
import xml.etree.ElementTree as ET

def jsonToThermoML(dataRepJson):

    attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    nsmap = {None: 'http://www.iupac.org/namespaces/ThermoML', 'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}
    DataReport = etree.Element("DataReport", {attr_qname: "http://www.iupac.org/namespaces/ThermoML ThermoML.xsd"}, nsmap=nsmap)


    ET.dump(DataReport)

def createVersion(DataReport):
    