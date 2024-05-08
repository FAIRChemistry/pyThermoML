from enum import Enum


class eSource(Enum):
    COMMERCIAL_SOURCE = "Commercial source"
    SYNTHESIZED_BY_THE_AUTHORS = "Synthesized by the authors"
    SYNTHESIZED_BY_OTHERS = "Synthesized by others"
    STANDARD_REFERENCE_MATERIAL_SRM = "Standard Reference Material (SRM)"
    ISOLATED_FROM_A_NATURAL_PRODUCT = "Isolated from a natural product"
    NOT_STATED_IN_THE_DOCUMENT = "Not stated in the document"
    NO_SAMPLE_USED = "No sample used"
