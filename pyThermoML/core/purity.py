import sdRDM

from typing import Optional, Union, List, Dict
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .epurifmethod import ePurifMethod
from .eanalmeth import eAnalMeth


@forge_signature
class Purity(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    n_halide_mass_per_cent: Optional[float] = element(
        description="mass per cent of halide impurity",
        default=None,
        tag="nHalideMassPerCent",
        json_schema_extra=dict(xml="nHalideMassPerCent"),
    )
    n_halide_mass_per_cent_digits: Optional[int] = element(
        default=None,
        tag="nHalideMassPerCentDigits",
        json_schema_extra=dict(xml="nHalideMassPerCentDigits"),
    )

    n_halide_mol_per_cent: Optional[float] = element(
        description="mass per cent of halide impurity",
        default=None,
        tag="nHalideMolPerCent",
        json_schema_extra=dict(xml="nHalideMolPerCent"),
    )
    n_halide_mol_per_cent_digits: Optional[int] = element(
        default=None,
        tag="nHalideMolPerCentDigits",
        json_schema_extra=dict(xml="nHalideMolPerCentDigits"),
    )

    n_purity_mass: Optional[float] = element(
        description="purity value in mass percent",
        default=None,
        tag="nPurityMass",
        json_schema_extra=dict(xml="nPurityMass"),
    )
    n_purity_mass_digits: Optional[int] = element(
        default=None,
        tag="nPurityMassDigits",
        json_schema_extra=dict(xml="nPurityMassDigits"),
    )

    n_purity_mol: Optional[float] = element(
        description="purity value in mole percent",
        default=None,
        tag="nPurityMol",
        json_schema_extra=dict(xml="nPurityMol"),
    )
    n_purity_mol_digits: Optional[int] = element(
        default=None,
        tag="nPurityMolDigits",
        json_schema_extra=dict(xml="nPurityMolDigits"),
    )

    n_purity_vol: Optional[float] = element(
        description="purity value in volume percent",
        default=None,
        tag="nPurityVol",
        json_schema_extra=dict(xml="nPurityVol"),
    )
    n_purity_vol_digits: Optional[int] = element(
        default=None,
        tag="nPurityVolDigits",
        json_schema_extra=dict(xml="nPurityVolDigits"),
    )
    n_step: Optional[int] = element(
        default=None, tag="nStep", json_schema_extra=dict(xml="nStep")
    )

    n_unknown_per_cent: Optional[float] = element(
        description="purity value in not specified percent",
        default=None,
        tag="nUnknownPerCent",
        json_schema_extra=dict(xml="nUnknownPerCent"),
    )
    n_unknown_per_cent_digits: Optional[int] = element(
        default=None,
        tag="nUnknownPerCentDigits",
        json_schema_extra=dict(xml="nUnknownPerCentDigits"),
    )

    n_water_mass_per_cent: Optional[float] = element(
        description="mass per cent of water",
        default=None,
        tag="nWaterMassPerCent",
        json_schema_extra=dict(xml="nWaterMassPerCent"),
    )
    n_water_mass_per_cent_digits: Optional[int] = element(
        default=None,
        tag="nWaterMassPerCentDigits",
        json_schema_extra=dict(xml="nWaterMassPerCentDigits"),
    )

    n_water_mol_per_cent: Optional[float] = element(
        description="mole per cent of water",
        default=None,
        tag="nWaterMolPerCent",
        json_schema_extra=dict(xml="nWaterMolPerCent"),
    )
    n_water_mol_per_cent_digits: Optional[int] = element(
        default=None,
        tag="nWaterMolPerCentDigits",
        json_schema_extra=dict(xml="nWaterMolPerCentDigits"),
    )

    e_anal_meth: List[Union[eAnalMeth, str]] = element(
        description="Analytical method used to determine purity",
        default_factory=ListPlus,
        tag="eAnalMeth",
        json_schema_extra=dict(multiple=True, xml="eAnalMeth"),
    )
    e_purif_method: List[Union[ePurifMethod, str]] = element(
        default_factory=ListPlus,
        tag="ePurifMethod",
        json_schema_extra=dict(multiple=True, xml="ePurifMethod"),
    )
    s_anal_meth: List[str] = element(
        default_factory=ListPlus,
        tag="sAnalMeth",
        json_schema_extra=dict(multiple=True, xml="sAnalMeth"),
    )
    s_purif_method: List[str] = element(
        default_factory=ListPlus,
        tag="sPurifMethod",
        json_schema_extra=dict(multiple=True, xml="sPurifMethod"),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/ThermoML-Specifications"
    )
    _commit: Optional[str] = PrivateAttr(
        default="374af92aef0e91313c5c390226161b9876735345"
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
