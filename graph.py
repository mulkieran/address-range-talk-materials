from collections import defaultdict

from justbytes import Range
from justbytes import ValueConfig
from justbytes import ROUND_DOWN

def _datum_gen(value, value_config):
    """
    Generate an integer datum for given value and value_config.

    :param int value: a value
    :param ValueConfig value_config: configuration for representation of value

    :returns: an integer corresponding to the value and value_config
    :rtype: int
    """
    radix = Range(value).getStringInfo(value_config)[0]
    return radix.as_int(ROUND_DOWN)[0]

def data_gen(values, multipliers):
    """
    Generate the data for a graph.

    :param values: an iterable of values in ascending order
    :type values: list of int
    :param multipliers: list of interesting multipliers for units
    :type multipliers: list of int

    :rtype: dict of str * (dict of str * list of int)
    :returns: maps from unit multiplier to (IEC, SI) to list of values
    """

    table = defaultdict(dict)

    for mult in multipliers:
        for unit_type in (BinaryUnits, DecimalUnits):
            value_config = ValueConfig(unit_type.unit_for_exp(mult))
            table[m][unit_type] = [_datum_gen(x, value_config) for x in values]
