from enum import Enum


class eDeviceSpecMethod(Enum):
    SPECIFIED_BY_THE_MANUFACTURER = "Specified by the manufacturer"
    CERTIFIED_OR_CALIBRATED_BY_A_THIRD_PARTY = (
        "Certified or calibrated by a third party"
    )
    CALIBRATED_BY_THE_EXPERIMENTALIST = "Calibrated by the experimentalist"
