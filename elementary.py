#!/usr/bin/env python3

# Jacob Anabi and Abby Wheaton
# 2294644 and 2299246
# anabi@chapman.edu and wheaton@chapman.edu
# PHYS220
# CW05

from scipy import constants

"""Module Description
This module includes a Particle object, ChargedParticle(Particle) object,
Electron(ChargedParticle) object, Proton(ChargedParticle) object
"""

class Particle(object):
    """Class Description
    The Particle class creates a Particle object, with a .impulse and .move functions

    Attributes:
        mass: the mass of the particle (float)
        position: the position of the particle in the xyz-coordinate system (tuple)
        momentum: the momentum of the particle in the xyz-coordinate system (tuple)
    """

    mass = 0.0

    def __init__(self, x, y, z):
        """Class constructor
        Sets the initial floats of the .position tuple to the three values (x, y, z) passed into the constructor,
        sets the mass to 1.0,
        and sets the initial momentum to (0.0, 0.0, 0.0)

        Args:
            x: the x position
            y: the y position
            z: the z position
        """
        self.position = (x, y, z)
        self.mass = 1.0
        self.momentum = (0.0, 0.0, 0.0)

    def impulse(self, px, py, pz):
        """Function docstring
        The .impulse functions increments the .momentum tuple by values px, py, pz

        Args:
            px: increments the x-position of the momentum tuple
            py: increments the y-position of the momentum tuple
            pz: increments the z-position of the momentum tuple
        """
        self.momentum = (self.momentum[0]+px, self.momentum[1]+py, self.momentum[2]+pz)

    def move(self, dt):
        """Function docstring
        The .move functions moves the position function given a dt value, and the mass and momentum of the paricle

        Args:
            dt: a time increment to move the position of the paricle
        """
        self.position = (self.position[0]+(self.momentum[0]/self.mass)*dt, self.position[1]+(self.momentum[1]/self.mass)*dt, self.position[2]+(self.momentum[2]/self.mass)*dt)

class ChargedParticle(Particle):
    """Class Description
    The ChargedParticle class creates a ChargedParticle object inherited from Particle

    Attributes:
        charge: the mass of the particle (float)
    """

    charge = 0.0

    def __init__(self, x, y, z):
        """
        Class constructor
        Sets the initial floats of the .position tuple to the three values (x, y, z) passed into the parent constructor,
        sets the mass to 1.0 through the parent
        and sets the initial momentum to (0.0, 0.0, 0.0) through the parent constructor
        sets the charge to 1.0

        Args:
            x: the x position
            y: the y position
            z: the z position
        """
        super(ChargedParticle, self).__init__(x, y, z)
        self.charge = 1.0

class Electron(ChargedParticle):
    """Class Description
    The Electron class creates an Electron object inherited from ChargedParticle
    """

    def __init__(self, x, y, z):
        """
        Class constructor
        Sets the initial floats of the .position tuple to the three values (x, y, z) passed into the parent constructor,
        and sets the initial momentum to (0.0, 0.0, 0.0) through the parent constructor
        sets the mass to the mass of the electron
        sets the charge to the charge of the electron

        Args:
            x: the x position
            y: the y position
            z: the z position
        """
        super(Electron, self).__init__(x, y, z)
        self.mass = constants.m_e
        self.charge = -constants.e

class Proton(ChargedParticle):
    """Class Description
    The Proton class creates an Proton object inherited from ChargedParticle
    """

    def __init__(self, x, y, z):
        """
        Class constructor
        Sets the initial floats of the .position tuple to the three values (x, y, z) passed into the parent constructor,
        and sets the initial momentum to (0.0, 0.0, 0.0) through the parent constructor
        sets the mass to the mass of the proton
        sets the charge to the charge of the proton

        Args:
            x: the x position
            y: the y position
            z: the z position
        """
        super(Proton, self).__init__(x, y, z)
        self.mass = constants.m_p
        self.charge = constants.e