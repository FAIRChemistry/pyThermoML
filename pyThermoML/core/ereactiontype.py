from enum import Enum


class eReactionType(Enum):
    COMBUSTION_WITH_OXYGEN = "Combustion with oxygen"
    ADDITION_OF_VARIOUS_COMPOUNDS_TO_UNSATURATED_COMPOUNDS = (
        "Addition of various compounds to unsaturated compounds"
    )
    ADDITION_OF_WATER_TO_A_LIQUID_OR_SOLID_TO_PRODUCE_A_HYDRATE = (
        "Addition of water to a liquid or solid to produce a hydrate"
    )
    ATOMIZATION_OR_FORMATION_FROM_ATOMS = "Atomization (or formation from atoms)"
    COMBUSTION_WITH_OTHER_ELEMENTS_OR_COMPOUNDS = (
        "Combustion with other elements or compounds"
    )
    ESTERIFICATION = "Esterification"
    EXCHANGE_OF_ALKYL_GROUPS = "Exchange of alkyl groups"
    EXCHANGE_OF_HYDROGEN_ATOMS_WITH_OTHER_GROUPS = (
        "Exchange of hydrogen (atoms) with other groups"
    )
    FORMATION_OF_A_COMPOUND_FROM_ELEMENTS_IN_THEIR_STABLE_STATE = (
        "Formation of a compound from elements in their stable state"
    )
    HALOGENATION_ADDITION_OF_OR_REPLACEMENT_BY_A_HALOGEN = (
        "Halogenation (addition of or replacement by a halogen)"
    )
    HYDROGENATION_ADDITION_OF_HYDROGEN_TO_UNSATURATED_COMPOUNDS = (
        "Hydrogenation (addition of hydrogen to unsaturated compounds)"
    )
    HYDROHALOGENATION = "Hydrohalogenation"
    HYDROLYSIS_OF_IONS = "Hydrolysis of ions"
    OTHER_REACTIONS_WITH_WATER = "Other reactions with water"
    ION_EXCHANGE = "Ion exchange"
    NEUTRALIZATION_REACTION_OF_AN_ACID_WITH_A_BASE = (
        "Neutralization (reaction of an acid with a base)"
    )
    OXIDATION_WITH_OXIDIZING_AGENTS_OTHER_THAN_OXYGEN = (
        "Oxidation with oxidizing agents other than oxygen"
    )
    OXIDATION_WITH_OXYGEN_NOT_COMPLETE = "Oxidation with oxygen (not complete)"
    POLYMERIZATION_ALL_OTHER_TYPES = "Polymerization (all other types)"
    HOMONUCLEAR_DIMERIZATION = "Homonuclear dimerization"
    SOLVOLYIS_SOLVENTS_OTHER_THAN_WATER = "Solvolyis (solvents other than water)"
    STEREOISOMERISM = "Stereoisomerism"
    STRUCTURAL_ISOMERIZATION = "Structural isomerization"
    FORMATION_OF_ION = "Formation of ion"
    OTHER_REACTIONS = "Other reactions"
