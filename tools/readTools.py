from core.pureOrMixtureData import PureOrMixtureData
from core.datareport import DataReport
from core.compound import Compound
from props.transportproperties import viscosity
from lxml import etree
import xmltodict, json

namespace = {'ThermoML': 'http://www.iupac.org/namespaces/ThermoML'}
namespaceString = '{http://www.iupac.org/namespaces/ThermoML}'

def get(parent, tag) -> str:
    '''
    Returns value of tag in ThermoML. Only first element of THermoML!
    controlled vocabulary!!
    
    Args:
        parent
        String tag: Name of element
    '''
    return parent.find('{http://www.iupac.org/namespaces/ThermoML}' + tag).text

def getChild(parent, childName):
    '''
    Returns subelement of parent
    '''
    return parent.find('.//{http://www.iupac.org/namespaces/ThermoML}' + childName)

# specific functions... not smart!
def getAuthors(Citation):
    '''
    Returns all authors of ThermoML in array representation'''
    authors = []
    for author in Citation.iter('{http://www.iupac.org/namespaces/ThermoML}sAuthor'):
        authors.append(author.text)
    return authors

def readThermo(path):
    '''
    Reads ThermoML document to an object layer ThermoML
    
    Args:
        String path: Path to ThermoML file
    '''
    
    tree = etree.parse(path)
    root = tree.getroot()

    dataReport = DataReport(get(getChild(root, 'Citation'), 'sTitle'), get(getChild(root, 'Citation'), 'sDOI'), *getAuthors(getChild(root, 'Citation')))
    
    for compound in root.iter('{http://www.iupac.org/namespaces/ThermoML}Compound'):
        #compound = getChild(root, 'Compound')
        regNum = getChild(compound, 'RegNum')
        comp = Compound(get(regNum, 'nOrgNum'), get(compound, 'sStandardInChi'), get(compound, 'sStandardInChiKey'), get(compound, 'sCommonName'), get(compound, 'sSmiles'))
        dataReport.addCompound(comp)

    for pureOrMixtureData in root.iter('{http://www.iupac.org/namespaces/ThermoML}PureOrMixtureData'):
        regNum = getChild(pureOrMixtureData, 'RegNum')

        # TODO: POMD name
        exp = PureOrMixtureData(get(pureOrMixtureData, 'nPureOrMixtureDataNumber'), )

    print(dataReport)

    