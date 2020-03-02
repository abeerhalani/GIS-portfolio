# -*- coding: utf-8 -*-
"""Generated by ArcGIS ModelBuilder on: 2020-03-01 18:10:33
All ModelBuilder functionality may not be exported. Edits may be required for equivalency with the original model.
"""

import arcpy

# To allow overwriting the outputs change the overwrite option to true.
arcpy.env.overwriteOutput = False

# Script parameters
Hydro = arcpy.GetParameterAsText(0) or "Hydro"
City_Limits = arcpy.GetParameterAsText(1) or "City Limits"
Parks = arcpy.GetParameterAsText(2) or "Parks"
Residential_Parcels = arcpy.GetParameterAsText(3) or "Residential Parcels"
FtCollins_gdb = arcpy.GetParameterAsText(4) or r"C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb"
Flood_Plain = arcpy.GetParameterAsText(5) or "Flood Plain"
VacParcels = arcpy.GetParameterAsText(6) or r"C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\VacParcels"
# Local variables:
CityBuf = r"C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\CityBuf"
RiverBuf = r"C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\RiverBuf"
MustBeIn = r"C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\MustBeIn"
ResBuf = r"C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ResBuf"
Unsuitable__2_ = ResBuf
ParksBuf = r"C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf"
Unsuitable = r"C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\Unsuitable"
SuitableAreas = r"C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\SuitableAreas"
Vacant_Suitable = r"C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\VacParcels_Clip"
Candidates = r"C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\VacParcels_Clip_Select"

# Process: Buffer City
arcpy.Buffer_analysis(in_features=City_Limits, out_feature_class=CityBuf, buffer_distance_or_field="1 Miles", line_side="FULL", line_end_type="ROUND", dissolve_option="ALL", dissolve_field="", method="PLANAR")

# Process: Buffer River
arcpy.Buffer_analysis(in_features=Hydro, out_feature_class=RiverBuf, buffer_distance_or_field="3000 Feet", line_side="FULL", line_end_type="ROUND", dissolve_option="ALL", dissolve_field="", method="PLANAR")

# Process: Clip
arcpy.Clip_analysis(in_features=CityBuf, clip_features=RiverBuf, out_feature_class=MustBeIn, cluster_tolerance="")

# Process: Buffer Residential
arcpy.Buffer_analysis(in_features=Residential_Parcels, out_feature_class=ResBuf, buffer_distance_or_field="300 Feet", line_side="FULL", line_end_type="ROUND", dissolve_option="ALL", dissolve_field="", method="PLANAR")

# Process: Buffer Parks
arcpy.Buffer_analysis(in_features=Parks, out_feature_class=ParksBuf, buffer_distance_or_field="300 Feet", line_side="FULL", line_end_type="ROUND", dissolve_option="ALL", dissolve_field="", method="PLANAR")

# Process: Create Feature Class
arcpy.CreateFeatureclass_management(out_path=FtCollins_gdb, out_name="Unsuitable", geometry_type="POLYGON", template="", has_m="DISABLED", has_z="DISABLED", spatial_reference="PROJCS['NAD_1983_StatePlane_Colorado_North_FIPS_0501',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',914401.8289],PARAMETER['False_Northing',304800.6096],PARAMETER['Central_Meridian',-105.5],PARAMETER['Standard_Parallel_1',39.71666666666667],PARAMETER['Standard_Parallel_2',40.78333333333333],PARAMETER['Latitude_Of_Origin',39.33333333333334],UNIT['Meter',1.0]];-36047400 -29011000 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision", config_keyword="", spatial_grid_1="0", spatial_grid_2="0", spatial_grid_3="0", out_alias="")

# Process: Append
arcpy.Append_management(inputs=r"C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ResBuf;C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf;'Flood Plain'", target=Unsuitable, schema_type="NO_TEST", field_mapping=r"FUNCTDESC "FUNCTDESC" true true false 254 Text 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ResBuf,FUNCTDESC,0,254;BUFF_DIST "BUFF_DIST" true true false 0 Double 0 0,First,#;ORIG_FID "ORIG_FID" true true false 0 Long 0 0,First,#;PARKNAME "PARKNAME" true true false 40 Text 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,PARKNAME,0,40;PARKTYPE "PARKTYPE" true true false 20 Text 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,PARKTYPE,0,20;PARKNO "PARKNO" true true false 2 Short 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,PARKNO,-1,-1;AGENCY "AGENCY" true true false 10 Text 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,AGENCY,0,10;STNO "STNO" true true false 5 Text 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,STNO,0,5;PREDIR "PREDIR" true true false 2 Text 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,PREDIR,0,2;STNAME "STNAME" true true false 40 Text 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,STNAME,0,40;STTYPE "STTYPE" true true false 4 Text 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,STTYPE,0,4;ACRESDEV "ACRESDEV" true true false 8 Double 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,ACRESDEV,-1,-1;ACRESUNDEV "ACRESUNDEV" true true false 8 Double 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,ACRESUNDEV,-1,-1;ACRESTTL "ACRESTTL" true true false 8 Double 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,ACRESTTL,-1,-1;PRKNGOFFST "PRKNGOFFST" true true false 2 Short 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,PRKNGOFFST,-1,-1;PRKNGONST "PRKNGONST" true true false 2 Short 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,PRKNGONST,-1,-1;IDNUM "IDNUM" true true false 2 Short 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,IDNUM,-1,-1;YEAR "YEAR" true true false 2 Short 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,YEAR,-1,-1;PARKIMAGE "PARKIMAGE" true true false 40 Text 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,PARKIMAGE,0,40;BUFF_DIST "BUFF_DIST" true true false 0 Double 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ResBuf,BUFF_DIST,-1,-1,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,BUFF_DIST,-1,-1;ORIG_FID "ORIG_FID" true true false 0 Long 0 0,First,#,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ResBuf,ORIG_FID,-1,-1,C:\EsriTraining\BldgModelsPro\FtCollins\FtCollins.gdb\ParksBuf,ORIG_FID,-1,-1;MAJOR "MAJOR" true true false 8 Text 0 0,First,#,Flood Plain,MAJOR,0,8;MINOR "MINOR" true true false 8 Text 0 0,First,#,Flood Plain,MINOR,0,8;DESCRIPTOR "DESCRIPTOR" true true false 16 Text 0 0,First,#,Flood Plain,DESCRIPTOR,0,16;FLD_TYPE "FLD_TYPE" true true false 2 Short 0 0,First,#,Flood Plain,FLD_TYPE,-1,-1", subtype="", expression="")

# Process: Erase
arcpy.Erase_analysis(in_features=MustBeIn, erase_features=Unsuitable__2_, out_feature_class=SuitableAreas, cluster_tolerance="")

# Process: Clip (2)
arcpy.Clip_analysis(in_features=VacParcels, clip_features=SuitableAreas, out_feature_class=Vacant_Suitable, cluster_tolerance="")

# Process: Select
arcpy.Select_analysis(in_features=Vacant_Suitable, out_feature_class=Candidates, where_clause="Shape_Area > 50000")

