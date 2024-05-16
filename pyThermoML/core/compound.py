import sdRDM

from typing import Optional, Union, List, Dict
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .componentsample import ComponentSample
from .polymer import Polymer
from .estatus import eStatus
from .especiationstate import eSpeciationState
from .sorgid import SOrgID
from .esource import eSource
from .sample import Sample
from .regnum import RegNum
from .biomaterial import Biomaterial
from .purity import Purity
from .ion import Ion
from .multicomponentsubstance import MulticomponentSubstance


@forge_signature
class Compound(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    biomaterial: Optional[Biomaterial] = element(
        default_factory=Biomaterial,
        tag="biomaterial",
        json_schema_extra=dict(xml="biomaterial"),
    )
    ion: Optional[Ion] = element(
        default_factory=Ion, tag="ion", json_schema_extra=dict(xml="ion")
    )
    multicomponent_substance: Optional[MulticomponentSubstance] = element(
        default_factory=MulticomponentSubstance,
        tag="MulticomponentSubstance",
        json_schema_extra=dict(xml="MulticomponentSubstance"),
    )
    polymer: Optional[Polymer] = element(
        default_factory=Polymer, tag="polymer", json_schema_extra=dict(xml="polymer")
    )
    e_speciation_state: Union[eSpeciationState, str, None] = element(
        default=None,
        tag="eSpeciationState",
        json_schema_extra=dict(xml="eSpeciationState"),
    )

    n_comp_index: Optional[int] = element(
        description="Index to link compounds to data",
        default=None,
        tag="nCompIndex",
        json_schema_extra=dict(xml="nCompIndex"),
    )
    n_pub_chem_id: Optional[int] = element(
        default=None, tag="nPubChemID", json_schema_extra=dict(xml="nPubChemID")
    )
    reg_num: Optional[RegNum] = element(
        default_factory=RegNum, tag="RegNum", json_schema_extra=dict(xml="RegNum")
    )
    s_cas_name: Optional[str] = element(
        default=None, tag="sCASName", json_schema_extra=dict(xml="sCASName")
    )

    s_common_name: List[str] = element(
        description="Common name, string Common name",
        default_factory=ListPlus,
        tag="sCommonName",
        json_schema_extra=dict(multiple=True, xml="sCommonName"),
    )

    s_formula_molec: Optional[str] = element(
        description="Molecular formula, string Chemical molecular formula",
        default=None,
        tag="sFormulaMolec",
        json_schema_extra=dict(xml="sFormulaMolec"),
    )

    s_iupac_name: Optional[str] = element(
        description=(
            "IUPAC name, string International Union of Physics and Applied Chemistry"
            " name"
        ),
        default=None,
        tag="sIUPACName",
        json_schema_extra=dict(xml="sIUPACName"),
    )
    s_org_id: List[SOrgID] = element(
        default_factory=ListPlus,
        tag="sOrgID",
        json_schema_extra=dict(multiple=True, xml="sOrgID"),
    )

    s_smiles: List[str] = element(
        description="SMILES notation, string SMILES notation",
        default_factory=ListPlus,
        tag="sSmiles",
        json_schema_extra=dict(multiple=True, xml="sSmiles"),
    )

    s_standard_in_ch_i: Optional[str] = element(
        description="Standard InChI string IUPAC International Chemical Identifier",
        default=None,
        tag="sStandardInChI",
        json_schema_extra=dict(xml="sStandardInChI"),
    )

    s_standard_in_ch_i_key: Optional[str] = element(
        description="Standard InChI key",
        default=None,
        tag="sStandardInChIKey",
        json_schema_extra=dict(xml="sStandardInChIKey"),
    )
    sample: List[Sample] = element(
        default_factory=ListPlus,
        tag="Sample",
        json_schema_extra=dict(multiple=True, xml="Sample"),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/pyThermoML"
    )
    _commit: Optional[str] = PrivateAttr(
        default="09a845c92b96665129bf0265d21674b8b92bf834"
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

    def add_to_s_org_id(
        self,
        s_org_identifier: Optional[str] = None,
        s_organization: Optional[str] = None,
        **kwargs
    ) -> SOrgID:
        """
        This method adds an object of type 'SOrgID' to attribute s_org_id

        Args:

            s_org_identifier (): . Defaults to None
            s_organization (): . Defaults to None
        """
        params = {
            "s_org_identifier": s_org_identifier,
            "s_organization": s_organization,
        }
        if id is not None:
            params["id"] = id
        self.s_org_id.append(SOrgID(**params))
        return self.s_org_id[-1]

    def add_to_sample(
        self,
        n_sample_nm: Optional[int] = None,
        component_sample: List[ComponentSample] = ListPlus(),
        e_source: Union[eSource, str, None] = None,
        e_status: Union[eStatus, str, None] = None,
        purity: List[Purity] = ListPlus(),
        **kwargs
    ) -> Sample:
        """
        This method adds an object of type 'Sample' to attribute sample

        Args:

            n_sample_nm (): . Defaults to None
            component_sample (): . Defaults to ListPlus()
            e_source (): . Defaults to None
            e_status (): . Defaults to None
            purity (): Purity of the sample. Defaults to ListPlus()
        """
        params = {
            "n_sample_nm": n_sample_nm,
            "component_sample": component_sample,
            "e_source": e_source,
            "e_status": e_status,
            "purity": purity,
        }
        if id is not None:
            params["id"] = id
        self.sample.append(Sample(**params))
        return self.sample[-1]
