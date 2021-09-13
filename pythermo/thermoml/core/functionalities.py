from builtins import isinstance


def TypeChecker(value, obj):
    if isinstance(value, obj):
        return value
    else:
        raise TypeError(
            "Expected %s got %s"
            % (str(obj), str(type(value)))
        )