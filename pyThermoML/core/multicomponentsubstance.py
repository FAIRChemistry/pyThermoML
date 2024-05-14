import sdRDM

from typing import Dict, List, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import attr, element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .regnum import RegNum
from .component import Component


@forge_signature
class MulticomponentSubstance(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    component: List[Component] = element(
        default_factory=ListPlus,
        tag="Component",
        json_schema_extra=dict(multiple=True, xml="Component"),
    )
    composition_basis: Optional[str] = attr(
        default=None,
        tag="compositionBasis",
        json_schema_extra=dict(xml="@compositionBasis"),
    )
    type: Optional[str] = attr(
        default=None, tag="type", json_schema_extra=dict(xml="@type")
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/pyThermoML"
    )
    _commit: Optional[str] = PrivateAttr(
        default="7847845987ccfa50e8c08ada56669b59d1b97819"
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

    def add_to_component(
        self,
        n_amount: Optional[float] = None,
        n_comp_index: Optional[int] = None,
        reg_num: Optional[RegNum] = None,
        n_sample_nm: Optional[int] = None,
        **kwargs
    ) -> Component:
        """
        This method adds an object of type 'Component' to attribute component

        Args:

            n_amount (): . Defaults to None
            n_comp_index (): . Defaults to None
            reg_num (): . Defaults to None
            n_sample_nm (): . Defaults to None
        """
        params = {
            "n_amount": n_amount,
            "n_comp_index": n_comp_index,
            "reg_num": reg_num,
            "n_sample_nm": n_sample_nm,
        }
        if id is not None:
            params["id"] = id
        self.component.append(Component(**params))
        return self.component[-1]
