import sdRDM

from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class Polymer(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    n_deg_of_polymerization_dispersity: Optional[float] = element(
        default=None,
        tag="nDegOfPolymerizationDispersity",
        json_schema_extra=dict(xml="nDegOfPolymerizationDispersity"),
    )

    n_mass_avg_mol_mass: Optional[float] = element(
        description="Weight average molecular mass, kg/kmol",
        default=None,
        tag="nMassAvgMolMass",
        json_schema_extra=dict(xml="nMassAvgMolMass"),
    )
    n_molar_mass_dispersity: Optional[float] = element(
        default=None,
        tag="nMolarMassDispersity",
        json_schema_extra=dict(xml="nMolarMassDispersity"),
    )

    n_number_avg_mol_mass: Optional[float] = element(
        description="Number average molecular mass, kg/kmol",
        default=None,
        tag="nNumberAvgMolMass",
        json_schema_extra=dict(xml="nNumberAvgMolMass"),
    )

    n_peak_avg_mol_mass: Optional[float] = element(
        description="Peak average molecular mass, kg/kmol",
        default=None,
        tag="nPeakAvgMolMass",
        json_schema_extra=dict(xml="nPeakAvgMolMass"),
    )

    n_viscosity_avg_mol_mass: Optional[float] = element(
        description="Viscosity average molecular mass, kg/kmol",
        default=None,
        tag="nViscosityAvgMolMass",
        json_schema_extra=dict(xml="nViscosityAvgMolMass"),
    )

    n_z_avg_mol_mass: Optional[float] = element(
        description="Z average molecular mass, kg/kmol",
        default=None,
        tag="nZAvgMolMass",
        json_schema_extra=dict(xml="nZAvgMolMass"),
    )
    _raw_xml_data: Dict = PrivateAttr(default_factory=dict)

    @model_validator(mode="after")
    def _parse_raw_xml_data(self):
        for attr, value in self:
            if isinstance(value, (ListPlus, list)) and all(
                (isinstance(i, _Element) for i in value)
            ):
                self._raw_xml_data[attr] = [elem2dict(i) for i in value]
            elif isinstance(value, _Element):
                self._raw_xml_data[attr] = elem2dict(value)
        return self
