import os
import xml.etree.ElementTree as ET
import lxml.etree as ETL


if __name__ == "__main__":
    tree1 = ETL.parse('DataGudrunGygli/cml2ThermoML/ChCl_urea/ChCl_urea_DOI3.xml')
    tree2 = ETL.parse('DataGudrunGygli/cml2ThermoML/ChCl_urea/ChCl_urea_withmistake_DOI3.xml')

    set1 = list(tree1.getroot().itertext())
    set2 = list(tree2.getroot().itertext())

    print(set1)
    print(set2)

    print (set1 == set2)
