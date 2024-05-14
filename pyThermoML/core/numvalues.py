import sdRDM

from typing import Dict, List, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .proprepeatability import PropRepeatability
from .varrepeatability import VarRepeatability
from .variablevalue import VariableValue
from .proplimit import PropLimit
from .curvedev import CurveDev
from .combineduncertainty import CombinedUncertainty
from .propertyvalue import PropertyValue
from .varuncertainty import VarUncertainty
from .propuncertainty import PropUncertainty


@forge_signature
class NumValues(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    property_value: List[PropertyValue] = element(
        default_factory=ListPlus,
        tag="PropertyValue",
        json_schema_extra=dict(multiple=True, xml="PropertyValue"),
    )
    variable_value: List[VariableValue] = element(
        default_factory=ListPlus,
        tag="VariableValue",
        json_schema_extra=dict(multiple=True, xml="VariableValue"),
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

    def add_to_property_value(
        self,
        n_prop_digits: Optional[int] = None,
        n_prop_number: Optional[int] = None,
        n_prop_value: Optional[float] = None,
        prop_limit: Optional[PropLimit] = None,
        combined_uncertainty: List[CombinedUncertainty] = ListPlus(),
        curve_dev: List[CurveDev] = ListPlus(),
        n_prop_device_spec_value: Optional[float] = None,
        prop_repeatability: Optional[PropRepeatability] = None,
        prop_uncertainty: List[PropUncertainty] = ListPlus(),
        **kwargs
    ) -> PropertyValue:
        """
        This method adds an object of type 'PropertyValue' to attribute property_value

        Args:

            n_prop_digits (): . Defaults to None
            n_prop_number (): . Defaults to None
            n_prop_value (): . Defaults to None
            prop_limit (): . Defaults to None
            combined_uncertainty (): . Defaults to ListPlus()
            curve_dev (): . Defaults to ListPlus()
            n_prop_device_spec_value (): . Defaults to None
            prop_repeatability (): . Defaults to None
            prop_uncertainty (): . Defaults to ListPlus()
        """
        params = {
            "n_prop_digits": n_prop_digits,
            "n_prop_number": n_prop_number,
            "n_prop_value": n_prop_value,
            "prop_limit": prop_limit,
            "combined_uncertainty": combined_uncertainty,
            "curve_dev": curve_dev,
            "n_prop_device_spec_value": n_prop_device_spec_value,
            "prop_repeatability": prop_repeatability,
            "prop_uncertainty": prop_uncertainty,
        }
        if id is not None:
            params["id"] = id
        self.property_value.append(PropertyValue(**params))
        return self.property_value[-1]

    def add_to_variable_value(
        self,
        n_var_digits: Optional[int] = None,
        n_var_number: Optional[int] = None,
        n_var_value: Optional[float] = None,
        n_var_device_spec_value: Optional[float] = None,
        var_repeatability: Optional[VarRepeatability] = None,
        var_uncertainty: List[VarUncertainty] = ListPlus(),
        **kwargs
    ) -> VariableValue:
        """
        This method adds an object of type 'VariableValue' to attribute variable_value

        Args:

            n_var_digits (): . Defaults to None
            n_var_number (): . Defaults to None
            n_var_value (): . Defaults to None
            n_var_device_spec_value (): . Defaults to None
            var_repeatability (): . Defaults to None
            var_uncertainty (): . Defaults to ListPlus()
        """
        params = {
            "n_var_digits": n_var_digits,
            "n_var_number": n_var_number,
            "n_var_value": n_var_value,
            "n_var_device_spec_value": n_var_device_spec_value,
            "var_repeatability": var_repeatability,
            "var_uncertainty": var_uncertainty,
        }
        if id is not None:
            params["id"] = id
        self.variable_value.append(VariableValue(**params))
        return self.variable_value[-1]
