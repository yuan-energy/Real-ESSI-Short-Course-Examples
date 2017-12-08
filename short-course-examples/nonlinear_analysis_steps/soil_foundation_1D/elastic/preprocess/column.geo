//****************************************************************
// Real-ESSI Short Course 
// 		Day 2: Motions
// Model Component: Soil-Foundation
//****************************************************************

//****************************************************************
// Predefined Parameters
//****************************************************************
height_of_column = 50 ;
width_of_column = 5  ;
depth_of_foundation = 5 ; 
Ox = 0;
Oy = 0;
Oz = -height_of_column ;

mesh_size = 5 ;
foundation_meshs_size = mesh_size/5 ; 
height_of_soil = height_of_column - depth_of_foundation ; 


//**************************************************************************************************
// Part A: Column
//**************************************************************************************************
p1 = newp; Point(p1) = {Ox, Oy, Oz};

ans[] = Extrude{width_of_column,0,0}{Point{p1};Layers{width_of_column/mesh_size};Recombine;} ; 
l1 = ans[1];
ans[] = Extrude{0, width_of_column, 0}{Line{l1};Layers{width_of_column/mesh_size};Recombine;} ; 
bottom_surface = ans[1];
ans[] = Extrude{0, 0, height_of_soil}{Surface{bottom_surface};Layers{height_of_soil/mesh_size};Recombine;} ; 
soil_volume = ans[1] ;
foundation_bottom_surface = ans[0] ;
ans[] = Extrude{0, 0, depth_of_foundation}{Surface{foundation_bottom_surface};Layers{depth_of_foundation/foundation_meshs_size};Recombine;} ; 
foundation_volume = ans[1] ;
foundation_top_surface = ans[0] ;
all_volume[] = {foundation_volume, soil_volume};




////********************************************************************
//// Recombine
////********************************************************************
Transfinite Surface "*";
Recombine Surface "*";


////********************************************************************
//// Physical Group
////********************************************************************

Physical Surface("bottom_surface") = bottom_surface[];
Physical Volume("soil_volume") = soil_volume[] ; 
Physical Volume("foundation_volume") = foundation_volume[] ; 
Physical Volume("all_volume") = all_volume[] ; 
Physical Surface("foundation_top_surface") = foundation_top_surface[] ; 
Physical Surface("foundation_bottom_surface") = foundation_bottom_surface[] ; 





















////********************************************************************
//// Helper:   Print return variables while developing the model
////********************************************************************
n = #ans[];
Printf("Extrude has returned %g elements", n);
n -= 1;
For i In {0 : n}
    Printf("Extrusion value[%g] = %g.", i, ans[i]);
EndFor




