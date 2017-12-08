import sys
import gmessi as GMESSI
import os
from math import *

 
gmESSI = GMESSI.gmESSIPython() 

#****************************************************************

# DRM 3D Example

#****************************************************************
gmESSI.loadGmshFile("column.msh")

gmESSI.setSimulationDir("./column_fei",1)

gmESSI.setMainFile(gmESSI.SimulationDir+ "main.fei")

gmESSI.setNodeFile(gmESSI.SimulationDir+ "node.fei")

gmESSI.setElementFile(gmESSI.SimulationDir+ "element.fei")

gmESSI.setLoadFile(gmESSI.SimulationDir+ "load.fei")


#2 1 "bottom_surface"

#3 2 "all_volume"
gmESSI.Convert("[Add_All_Node{ unit:= m, nof_dofs:= 3}]")
gmESSI.CopyCommand("\n");
## Soil
gmESSI.Convert("[Fix_All_Dofs{Physical_Group#bottom_surface}]")
gmESSI.Convert("[Fix_Dofs{Physical_Group#all_volume, DofTypes:= uy}]")
gmESSI.CopyCommand("\n");gmESSI.Convert("[Generate_DRM_Physical_Group_1D{Physical_Group#soil_volume, surface_normal:= z, Node_Coordinate_Tol:= 0.01 , Number_of_layers:= 3 , PhysicalGroupName:= Inside, PhysicalGroupName:= DRM, PhysicalGroupName:= Damping }]")
gmESSI.CopyCommand("\n");gmESSI.Convert("[Add_8NodeBrick{Physical_Group#Inside, MaterialNo:= 1}]")
gmESSI.Convert("[Add_8NodeBrick{Physical_Group#DRM, MaterialNo:= 2}]")
gmESSI.Convert("[Add_8NodeBrick{Physical_Group#Damping, MaterialNo:= 3}]")
gmESSI.CopyCommand("\n");gmESSI.Convert("[Generate_DRM_HDF5_1D{Physical_Group#DRM, Surface_Normal:= z, Node_Coordinate_Tol:= 0.01 , FileName:= DRMinput.hdf5}]")
gmESSI.CopyCommand("\n");gmESSI.CopyCommand("\n");gmESSI.Convert("[Add_8NodeBrick{Physical_Group#foundation_volume, MaterialNo:= 4}]")
gmESSI.CopyCommand("\n");
gmESSI.setLoadFile(gmESSI.SimulationDir+ \"fix_all_uz.fei\")

gmESSI.Convert("[Fix_Dofs{Physical_Group#all_volume, DofTypes:= uz}]")
gmESSI.CopyCommand("\n");gmESSI.CopyCommand("\n");
### ======================================================

### Damping

### ======================================================

#[Add_Damping_To_Element{Physical_Group#shell_all_surfaces, DampingNo:= 1}]
gmESSI.Convert("[Add_Damping_To_Element{Physical_Group#foundation_volume, DampingNo:= 2}]")
gmESSI.Convert("[Add_Damping_To_Element{Physical_Group#Inside, DampingNo:= 3}]")
gmESSI.Convert("[Add_Damping_To_Element{Physical_Group#DRM, DampingNo:= 4}]")
gmESSI.Convert("[Add_Damping_To_Element{Physical_Group#Damping, DampingNo:= 5}]")
gmESSI.CopyCommand("\n");gmESSI.CopyCommand("\n");gmESSI.CopyCommand("\n");gmESSI.CopyCommand("\n");