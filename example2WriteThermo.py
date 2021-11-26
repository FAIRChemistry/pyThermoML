from pythermo.thermoml.core import DataReport, Compound
from pythermo.thermoml.core.pureOrMixtureData import PureOrMixtureData
from pythermo.thermoml.tools.writeTools import ThermoMLWriter
from pythermo.thermoml.tools.readTools import ThermoMLReader



writer = ThermoMLWriter(dataRep="github.json", filename="testThermo1.xml")
writer.writeThermo()