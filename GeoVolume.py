'''
package name: GeoPackage
module name: GeoArea
This module contains functions to compute volume of:
sphere and cuboid
'''

def VolumeSphere(radius):
    """
    objective: To compute volume of the sphere
    Input para: radius
    output: Volume of the sphere
    """

    vol=(4/3)*(3.14)*(radius**3)
    return vol


def VolumeCuboid(length,breadth,height):
    '''
    objective: To compute volume of the cuboid
    Input para: length,breadth,height
    output: Volume of the cuboid
    '''

    vol = length*breadth*height
    return vol