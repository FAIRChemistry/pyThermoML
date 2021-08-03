from props.transportproperties import viscosity


def getPropMapping(ePropName):
    return propMapping[ePropName]


propMapping = {
    "Viscosity, Pa*s": (viscosity, "transport-prop")
}


if __name__ == "__main__":

    func, findParam = getPropMapping("Viscosity, Pa*s")

    print(func("LALALA", "HELOLEO"))
