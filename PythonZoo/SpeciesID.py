import arcpy
import numpy

arcpy.env.workspace = r"C:\Users\abeer\Documents\ArcGIS\Packages\ZooEscape_9ea7ab\p20\ZooEscape.gdb"

# Create a new function which returns a list of species by identifying unique values in the attribute table.
def getSpecies(table, field):
    data = arcpy.da.TableToNumPyArray(table, [field])
    return numpy.unique(data[field]).tolist()

# Call the new function and assign the output to a variable.
speciesList = getSpecies("FieldSightings_Jimmy", "Species")

# Print the variable containing the list of species.
print(speciesList)
