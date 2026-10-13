def calculate_mean(values):
    """
    Calculate the arithmetic mean of a list of numbers.

    Parameters
    ----------
    values : list
        List of numerical measurements.

    Returns
    -------
    float
        Arithmetic mean of the measurements.
    """
    return sum(values) / len(values)

help(calculate_mean)