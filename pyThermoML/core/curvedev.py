import sdRDM

from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class CurveDev(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    n_curve_dev_assess_num: Optional[int] = element(
        default=None,
        tag="nCurveDevAssessNum",
        json_schema_extra=dict(xml="nCurveDevAssessNum"),
    )
    n_curve_dev_value: Optional[float] = element(
        default=None, tag="nCurveDevValue", json_schema_extra=dict(xml="nCurveDevValue")
    )
    s_curve_spec: Optional[str] = element(
        default=None, tag="sCurveSpec", json_schema_extra=dict(xml="sCurveSpec")
    )
    n_curve_rms_dev_value: Optional[float] = element(
        default=None,
        tag="nCurveRmsDevValue",
        json_schema_extra=dict(xml="nCurveRmsDevValue"),
    )
    n_curve_rms_relative_dev_value: Optional[float] = element(
        default=None,
        tag="nCurveRmsRelativeDevValue",
        json_schema_extra=dict(xml="nCurveRmsRelativeDevValue"),
    )
    s_curve_dev_evaluator: Optional[str] = element(
        default=None,
        tag="sCurveDevEvaluator",
        json_schema_extra=dict(xml="sCurveDevEvaluator"),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/pyThermoML"
    )
    _commit: Optional[str] = PrivateAttr(
        default="4014e57ac2f3b9b09cdefb1c3e2f2cfca298f660"
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
