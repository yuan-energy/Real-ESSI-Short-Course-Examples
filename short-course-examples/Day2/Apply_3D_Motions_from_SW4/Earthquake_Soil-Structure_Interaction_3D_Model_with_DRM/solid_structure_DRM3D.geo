//****************************************************************
// Real-ESSI Short Course 
// 		Day 2: Motions
// Model Component: Soil-Foundation
//****************************************************************

//****************************************************************
// Predefined Parameters
//****************************************************************

height_of_structure = 60 ;
depth_of_foundation = 5 ;
width_of_structure = 30  ;
depth_of_soil = 40;
width_of_field = width_of_structure * 3 ;

Ox = 0;
Oy = 0;
Oz = -depth_of_foundation;

epsilon =0.001 ;
//epsilon = 2 ;

mesh_size = 5;



//**************************************************************************************************
// Part A: Soil
//**************************************************************************************************
// Soil: 
p1 = newp; Point(p1) = {Ox, Oy, Oz};

ans[] = Extrude{width_of_field,0,0}{Point{p1};Layers{width_of_field/mesh_size};Recombine;} ; 
l1 = ans[1];
ans[] = Extrude{width_of_structure,0,0}{Point{ans[0]};Layers{width_of_structure/mesh_size};Recombine;} ; 
l2 = ans[1];
ans[] = Extrude{width_of_field,0,0}{Point{ans[0]};Layers{width_of_field/mesh_size};Recombine;} ; 
l3 = ans[1];

ans[] = Extrude{0,width_of_field,0}{Line{l1,l2,l3};Layers{width_of_field/mesh_size};Recombine;} ; 
l4 = ans[0]; l5 = ans[4]; l6 = ans[8];
ans[] = Extrude{0,width_of_structure,0}{Line{l4,l5,l6};Layers{width_of_structure/mesh_size};Recombine;} ; 
l7 = ans[0]; l8 = ans[4]; l9 = ans[8];
ans[] = Extrude{0,width_of_field,0}{Line{l7,l8,l9};Layers{width_of_field/mesh_size};Recombine;} ; 



ans[] = Extrude{0, 0, -depth_of_soil}{Surface{7,11,15,19,23,27,31,35,39}; Layers{depth_of_soil/mesh_size};Recombine;};
ans[] = Extrude{0, 0, depth_of_foundation}{Surface{7,11,15,19,27,31,35,39}; Layers{depth_of_foundation/mesh_size};Recombine;};
soils_under_zero[] = {1, 2, 3, 4, 5, 6, 7, 8, 9} ; 
soils_around_foundation[] = {10, 11, 12, 13, 14, 15, 16, 17} ; 
soil_x_minus_surface = 316;
soil_x_plus_surface = 346;
soil_y_plus_surface = 378;
soil_y_minus_surface = 276;
soil_z_top_surface = 23;

Physical Volume("soils_under_zero") = soils_under_zero[] ; 
Physical Volume("soils_around_foundation") = soils_around_foundation[] ; 

Physical Surface("soil_x_minus_surface") = soil_x_minus_surface ; 
Physical Surface("soil_x_plus_surface") = soil_x_plus_surface ; 
Physical Surface("soil_y_plus_surface") = soil_y_plus_surface ; 
Physical Surface("soil_y_minus_surface") = soil_y_minus_surface ; 

Physical Surface("soil_z_top_surface") = soil_z_top_surface ; 

all_soils[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17} ;
Physical Volume("all_soils") = all_soils[] ; 

soils_bottom_most[] = {61, 83, 105, 127, 149, 171, 193, 215, 237} ; 
Physical Surface("soils_bottom_most") = soils_bottom_most[] ; 

//**************************************************************************************************
// Part B: Foundation  
//**************************************************************************************************

x_minus_y_minus = newp;  Point(x_minus_y_minus) = {Ox + width_of_field + epsilon, Oy + width_of_field + epsilon, Oz+  epsilon}; 
x_plus_y_minus = newp; Point(x_plus_y_minus) = {Ox + width_of_field + width_of_structure - epsilon, Oy + width_of_field + epsilon, Oz+  epsilon}; 
x_minus_y_plus = newp; Point(x_minus_y_plus) = {Ox + width_of_field + epsilon, Oy + width_of_field + width_of_structure - epsilon, Oz+  epsilon}; 
x_plus_y_plus = newp; Point(x_plus_y_plus) = {Ox + width_of_field + width_of_structure - epsilon, Oy + width_of_field + width_of_structure - epsilon, Oz+  epsilon}; 

y_minus_line = newl; Line(y_minus_line) = {x_minus_y_minus, x_plus_y_minus};
y_plus_line = newl; Line(y_plus_line) = {x_minus_y_plus, x_plus_y_plus};
x_minus_line = newl; Line(x_minus_line) = {x_minus_y_minus, x_minus_y_plus};
x_plus_line = newl; Line(x_plus_line) = {x_plus_y_plus, x_plus_y_minus};
Transfinite Line(y_minus_line) = (width_of_structure/mesh_size) + 1 ; 
Transfinite Line(y_plus_line) = (width_of_structure/mesh_size) + 1 ; 
Transfinite Line(x_minus_line) = (width_of_structure/mesh_size) + 1 ; 
Transfinite Line(x_plus_line) = (width_of_structure/mesh_size) + 1 ; 
loop1 = newreg; Line Loop(loop1) = {x_minus_line,y_plus_line,x_plus_line,-y_minus_line} ;
foundation_bottom_surface = news; Plane Surface(foundation_bottom_surface) = {loop1};
ans[] = Extrude{0,0,depth_of_foundation}{Surface{foundation_bottom_surface} ;Layers{depth_of_foundation/mesh_size};Recombine;};

foundation_top_surface                        = ans[0] ;

foundation_volume                             = ans[1] ;

foundation_x_minus_surface                    = ans[2]  ;
foundation_y_plus_surface                     = ans[3]  ;
foundation_x_plus_surface                     = ans[4]  ;
foundation_y_minus_surface                    = ans[5]  ;

Physical Volume("foundation_volume")          = foundation_volume;

Physical Surface("foundation_top_surface")    = foundation_top_surface ;
Physical Surface("foundation_bottom_surface") = foundation_bottom_surface ;

Physical Surface("foundation_x_minus_surface") = foundation_x_minus_surface ;
Physical Surface("foundation_y_plus_surface")  = foundation_y_plus_surface ;
Physical Surface("foundation_x_plus_surface")  = foundation_x_plus_surface ;
Physical Surface("foundation_y_minus_surface") = foundation_y_minus_surface ;


//////**************************************************************************************************
////// Part C: Structure
//////**************************************************************************************************
ans[] = Extrude{0,0,height_of_structure}{Surface{foundation_top_surface} ;Layers{height_of_structure/mesh_size};Recombine;};
structure_volume = ans[1] ; 
structure_top_surface = ans[0] ; 

structure_x_minus_surface                     = ans[2]  ;
structure_y_plus_surface                      = ans[3]  ;
structure_x_plus_surface                      = ans[4]  ;
structure_y_minus_surface                     = ans[5]  ;

Physical Volume("structure_volume") = structure_volume;

Physical Surface("structure_top_surface") = structure_top_surface ; 

Physical Surface("structure_x_minus_surface") = structure_x_minus_surface ;
Physical Surface("structure_y_plus_surface")  = structure_y_plus_surface ;
Physical Surface("structure_x_plus_surface")  = structure_x_plus_surface ;
Physical Surface("structure_y_minus_surface") = structure_y_minus_surface ;


////********************************************************************
//// Recombine
////********************************************************************


Transfinite Surface "*";
Recombine Surface "*";


























n = #ans[];
Printf("Extrude has returned %g elements", n);
n -= 1;
For i In {0 : n}
    Printf("Extrusion value[%g] = %g.", i, ans[i]);
EndFor




