//****************************************************************
// DRM 3D Example 
//****************************************************************

//****************************************************************
// Predefined Parameters
//****************************************************************
mesh_size = 5;

total_width_of_field =  150 ; 
total_height_of_soil = 30 ; 


//**************************************************************************************************
// Part A: Soil 
//**************************************************************************************************

// 1. Create the point and extrude to line, and then to surface.
p1 = newp; Point(p1) = {0, 0, 0};
ans[] = Extrude{0,0,total_height_of_soil}{Point{p1};Layers{total_height_of_soil/mesh_size};Recombine;} ; 
ans[] = Extrude{total_width_of_field,0,0}{Line{ans[1]}; Layers{total_width_of_field/mesh_size};Recombine;};



//********************************************************************
// Part B: Extract 2D ==> 3D
//********************************************************************

ans[] =  Extrude{0,total_width_of_field,0}{Surface{5}; Layers{total_width_of_field/mesh_size}; Recombine;};


Transfinite Surface "*";
Recombine Surface "*";

//********************************************************************
// Part C: Define Physical Group
//********************************************************************

leftmost_soil_surface[] = {14};
rightmost_soil_surface[] = {22};
bottom_soil_surface[] = {26}; 

Physical Surface("leftmost_soil_surface") = leftmost_soil_surface[];
Physical Surface("rightmost_soil_surface") = rightmost_soil_surface[];
Physical Surface("bottom_soil_surface") = bottom_soil_surface[];

Physical Volume("soil") = {1} ; 

