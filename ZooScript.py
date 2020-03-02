# coding: utf-8
fclist = ["FieldSightings_lola", FieldSightings_Jimmy]
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# NameError: name 'FieldSightings_Jimmy' is not defined
fclist = ["FieldSightings_lola", "FieldSightings_Jimmy"]
print(fclist)
# ['FieldSightings_lola', 'FieldSightings_Jimmy']
bufflist = []
for fc in fclist:
    buff = arcpy.Buffer_analysis(fc, fc+"_Buffer", "1 kilometer")
    bufflist.append(buff)
for buff in bufflist:
    arcpy.SelectLayerByLocation_management('Redlands_Schools', 'WITHIN', buff, 0, 'ADD_TO_SELECTION'
)
# <Result 'Redlands_Schools'>
# <Result 'Redlands_Schools'>