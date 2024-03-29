# @File          :   transportproperties.py
# @Last modified :   2022/04/09 19:28:32
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

from typing import Optional
from pythermo.thermoml.props.propertyBase import PropertyBase


class TransportProperty(PropertyBase):
    """Class representing transport properties. The following properties aretaken over from ThermoML - schema definition:
    Viscosity, kinematic viscosity, self diffusion coefficient. Inherited from PropertyBase.

    Args:
        propGroup (str): Transport property group

    """

    propGroup: str = "TransportProp"

    @classmethod
    def viscosity(
        cls, ID: int, method: str, compoundID: Optional[int] = None
    ) -> "TransportProperty":
        """creates viscosity object. For more information vist documentation of PropertyBase.

        Note:
            Unit: Pa*s

        Args:
            ID (str): ID
            method (str): method
            compoundID (str): ID of referred compound

        Returns:
            TransportProperty: object of type TransportProperty.
        """
        return cls(
            propName="Viscosity",
            ID=ID,
            unit="Pa*s",
            method=method,
            compoundID=compoundID,
        )

    @classmethod
    def kinematicViscosity(
        cls, ID: int, method: str, compoundID: Optional[int] = None
    ) -> "TransportProperty":
        """creates kinematic viscosity object. For more information vist documentation of PropertyBase.

        Note:
            Unit: Pa*s

        Args:
            ID (str): ID
            method (str): method
            compoundID (str): ID of referred compound

        Returns:
            TransportProperty: object of type TransportProperty.
        """
        return cls(
            propName="Viscosity",
            ID=ID,
            unit="Pa*s",
            method=method,
            compoundID=compoundID,
        )

    @classmethod
    def selfDiffusionCoefficient(
        cls, ID: int, method: str, compoundID: int
    ) -> "TransportProperty":
        """creates self diffusion coefficient object. For more information vist documentation of PropertyBase.

        Note:
            Unit: m2/s

        Args:
            ID (str): ID
            method (str): method
            compoundID (str): determines referred compound

        Returns:
            TransportProperty: object of type TransportProperty.
        """
        return cls(
            propName="Self diffusion coefficient",
            ID=ID,
            unit="m2/s",
            method=method,
            compoundID=compoundID,
        )

    @classmethod
    def tracerDiffusionCoefficient(
        cls, ID: int, method: str, compoundID: int
    ) -> "TransportProperty":
        """creates tracer diffusion coefficient object.

        Note:
            Unit: m2/s
        Args:
            ID (str): ID
            method (str): method
            compoundID (str): describes referred compound

        Returns:
            TransportProperty: object of type TransporProperty.
        """
        return cls(
            propName="Tracer diffusion coefficient",
            ID=ID,
            unit="m2/s",
            method=method,
            compoundID=compoundID,
        )
