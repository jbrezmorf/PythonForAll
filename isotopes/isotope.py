from typing import *
import enum
import attr


def load_isotopes_yaml():
    pass


class Isotope:
    def __init__(self, element, atomic_number, nucleon_number, hl, decays):
        self.element = element
        # Element abbreviation
        self.atomic_number = atomic_number
        self.nucleon_number = nucleon_number
        self.hl = hl
        # half-life [s]
        self.decays = decays
        # List of decays (usually just one).
        excited: int
        # Excited nuclei, metastable.

    def __repr__(self):
        return "{:2d}_{}-{} -> {}".format(self.atomic_number, self.element, self.nucleon_number, self.decays[0])

    @property
    def n_neutrons(self):
        return self.nucleon_number - self.atomic_number

    def product_isotope(self, i_decay):
        # Table of nuclei changes for different decay types.
        # Tuples: (atomic_number_change, nucleon_number_change)
        nuclei_change = {
            DecayType.alpha : (-2, -4),
            DecayType.beta_n: (+1, 0),
            DecayType.beta_p: (-1, 0),
            DecayType.gamma: (0, 0)
        }
        decay = self.decays[i_decay]
        d_at, d_nuc = nuclei_change[decay.type]
        return self.atomic_number + d_at, self.nucleon_number + d_nuc


class DecayType(enum.Enum):
    alpha = 0
    beta_n = 1
    gamma = 2
    beta_p = 3
    proton_emission = 4
    # ...


@attr.s(auto_attribs=True)
class Decay:
    type: DecayType
    # Type of decay.
    energy: float
    # Radiation energy [MeV].
    probability: float = 1
    # Probability of this type of decay.


class Isotopes:
    def __init__(self):
        self.isotopes = List[Isotope]



