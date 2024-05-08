import sdRDM

from typing import Optional, Union, List, Dict
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .esource import eSource
from .regnum import RegNum
from .estatus import eStatus
from .epurifmethod import ePurifMethod
from .componentsample import ComponentSample
from .purity import Purity
from .eanalmeth import eAnalMeth


@forge_signature
class Sample(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    n_sample_nm: Optional[int] = element(
        default=None, tag="nSampleNm", json_schema_extra=dict(xml="nSampleNm")
    )
    component_sample: List[ComponentSample] = element(
        default_factory=ListPlus,
        tag="ComponentSample",
        json_schema_extra=dict(multiple=True, xml="ComponentSample"),
    )
    e_source: Union[eSource, str, None] = element(
        default=None, tag="eSource", json_schema_extra=dict(xml="eSource")
    )
    e_status: Union[eStatus, str, None] = element(
        default=None, tag="eStatus", json_schema_extra=dict(xml="eStatus")
    )

    purity: List[Purity] = element(
        description="Purity of the sample",
        default_factory=ListPlus,
        tag="purity",
        json_schema_extra=dict(multiple=True, xml="purity"),
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

    def add_to_component_sample(
        self,
        n_comp_index: Optional[int] = None,
        n_sample_nm: Optional[int] = None,
        reg_num: Optional[RegNum] = None,
        **kwargs
    ) -> ComponentSample:
        """
        This method adds an object of type 'ComponentSample' to attribute component_sample

        Args:

            n_comp_index (): . Defaults to None
            n_sample_nm (): . Defaults to None
            reg_num (): . Defaults to None
        """
        params = {
            "n_comp_index": n_comp_index,
            "n_sample_nm": n_sample_nm,
            "reg_num": reg_num,
        }
        if id is not None:
            params["id"] = id
        self.component_sample.append(ComponentSample(**params))
        return self.component_sample[-1]

    def add_to_purity(
        self,
        n_halide_mass_per_cent: Optional[float] = None,
        n_halide_mass_per_cent_digits: Optional[int] = None,
        n_halide_mol_per_cent: Optional[float] = None,
        n_halide_mol_per_cent_digits: Optional[int] = None,
        n_purity_mass: Optional[float] = None,
        n_purity_mass_digits: Optional[int] = None,
        n_purity_mol: Optional[float] = None,
        n_purity_mol_digits: Optional[int] = None,
        n_purity_vol: Optional[float] = None,
        n_purity_vol_digits: Optional[int] = None,
        n_step: Optional[int] = None,
        n_unknown_per_cent: Optional[float] = None,
        n_unknown_per_cent_digits: Optional[int] = None,
        n_water_mass_per_cent: Optional[float] = None,
        n_water_mass_per_cent_digits: Optional[int] = None,
        n_water_mol_per_cent: Optional[float] = None,
        n_water_mol_per_cent_digits: Optional[int] = None,
        e_anal_meth: List[Union[eAnalMeth, str]] = ListPlus(),
        e_purif_method: List[Union[ePurifMethod, str]] = ListPlus(),
        s_anal_meth: List[str] = ListPlus(),
        s_purif_method: List[str] = ListPlus(),
        **kwargs
    ) -> Purity:
        """
        This method adds an object of type 'Purity' to attribute purity

        Args:

            n_halide_mass_per_cent (): mass per cent of halide impurity. Defaults to None
            n_halide_mass_per_cent_digits (): . Defaults to None
            n_halide_mol_per_cent (): mass per cent of halide impurity. Defaults to None
            n_halide_mol_per_cent_digits (): . Defaults to None
            n_purity_mass (): purity value in mass percent. Defaults to None
            n_purity_mass_digits (): . Defaults to None
            n_purity_mol (): purity value in mole percent. Defaults to None
            n_purity_mol_digits (): . Defaults to None
            n_purity_vol (): purity value in volume percent. Defaults to None
            n_purity_vol_digits (): . Defaults to None
            n_step (): . Defaults to None
            n_unknown_per_cent (): purity value in not specified percent. Defaults to None
            n_unknown_per_cent_digits (): . Defaults to None
            n_water_mass_per_cent (): mass per cent of water. Defaults to None
            n_water_mass_per_cent_digits (): . Defaults to None
            n_water_mol_per_cent (): mole per cent of water. Defaults to None
            n_water_mol_per_cent_digits (): . Defaults to None
            e_anal_meth (): Analytical method used to determine purity. Defaults to ListPlus()
            e_purif_method (): . Defaults to ListPlus()
            s_anal_meth (): . Defaults to ListPlus()
            s_purif_method (): . Defaults to ListPlus()
        """
        params = {
            "n_halide_mass_per_cent": n_halide_mass_per_cent,
            "n_halide_mass_per_cent_digits": n_halide_mass_per_cent_digits,
            "n_halide_mol_per_cent": n_halide_mol_per_cent,
            "n_halide_mol_per_cent_digits": n_halide_mol_per_cent_digits,
            "n_purity_mass": n_purity_mass,
            "n_purity_mass_digits": n_purity_mass_digits,
            "n_purity_mol": n_purity_mol,
            "n_purity_mol_digits": n_purity_mol_digits,
            "n_purity_vol": n_purity_vol,
            "n_purity_vol_digits": n_purity_vol_digits,
            "n_step": n_step,
            "n_unknown_per_cent": n_unknown_per_cent,
            "n_unknown_per_cent_digits": n_unknown_per_cent_digits,
            "n_water_mass_per_cent": n_water_mass_per_cent,
            "n_water_mass_per_cent_digits": n_water_mass_per_cent_digits,
            "n_water_mol_per_cent": n_water_mol_per_cent,
            "n_water_mol_per_cent_digits": n_water_mol_per_cent_digits,
            "e_anal_meth": e_anal_meth,
            "e_purif_method": e_purif_method,
            "s_anal_meth": s_anal_meth,
            "s_purif_method": s_purif_method,
        }
        if id is not None:
            params["id"] = id
        self.purity.append(Purity(**params))
        return self.purity[-1]
