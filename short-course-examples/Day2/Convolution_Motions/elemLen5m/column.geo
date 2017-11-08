//****************************************************************
// Real-ESSI Short Course 
// 		Day 2: Motions
// Model Component: Soil-Foundation
//****************************************************************

//****************************************************************
// Predefined Parameters
//****************************************************************
height_of_column = 200 ;
width_of_column = 5  ;

Ox = 0;
Oy = 0;
Oz = 0;

mesh_size = width_of_column ;



//**************************************************************************************************
// Part A: Column
//**************************************************************************************************
p1 = newp; Point(p1) = {Ox, Oy, Oz};

ans[] = Extrude{width_of_column,0,0}{Point{p1};Layers{width_of_column/mesh_size};Recombine;} ; 
l1 = ans[1];
ans[] = Extrude{0, width_of_column, 0}{Line{l1};Layers{width_of_column/mesh_size};Recombine;} ; 
bottom_surface = ans[1];
ans[] = Extrude{0, 0, height_of_column}{Surface{bottom_surface};Layers{height_of_column/mesh_size};Recombine;} ; 
all_volume = ans[1] ;


////********************************************************************
//// Recombine
////********************************************************************
Transfinite Surface "*";
Recombine Surface "*";


////********************************************************************
//// Physical Group
////********************************************************************

Physical Surface("bottom_surface") = bottom_surface[];
Physical Volume("all_volume") = all_volume[] ; 






















////********************************************************************
//// Helper:   Print return variables while developing the model
////********************************************************************
n = #ans[];
Printf("Extrude has returned %g elements", n);
n -= 1;
For i In {0 : n}
    Printf("Extrusion value[%g] = %g.", i, ans[i]);
EndFor




