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

def calculate_molecular_mass(amino_acid_masses):
    """
    Calculate the total mass of a list of amino acids.

    Parameters
    ----------
    amino_acid_masses : list
        Individual amino acid masses.

    Returns
    -------
    float
        Sum of the supplied masses.
    """
    return sum(amino_acid_masses)