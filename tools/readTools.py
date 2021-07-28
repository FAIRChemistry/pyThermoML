from props.transportproperties import viscosity
from lxml import etree
import xmltodict, json

namespace = {'ThermoML': 'http://www.iupac.org/namespaces/ThermoML'}

def readThermo(path):
    '''
    Reads ThermoML document to an object layer ThermoML
    
    Args:
        String path: Path to ThermoML file
    '''

    tree = etree.parse(path)
    root = tree.getroot()
    print(str(etree.dump(root)))
    x = '"""\n' + str(etree.dump(root)) + '"""'
    print(x)
    obj = xmltodict.parse(str(etree.dump(root)))
    print(json.dumps(obj))

    #for elem in root.findall('ThermoML:nVersionMajor', namespace):
    #    print(elem.text)

