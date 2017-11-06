//****************************************************************
// DRM 3D Example 
//****************************************************************

//****************************************************************
// Predefined Parameters
//****************************************************************
mesh_size = 5;
height =  80 ; 
width = 30 ; 


//**************************************************************************************************
// Part A: Soil 
//**************************************************************************************************

// 1. Create the point and extrude to line, and then to surface.
p1 = newp; Point(p1) = {0, 0, 0};
ans[] = Extrude{0,0,height}{Point{p1};Layers{height/mesh_size};Recombine;} ; 
ans[] = Extrude{width,0,0}{Line{ans[1]}; Layers{width/mesh_size};Recombine;};



//********************************************************************
// Part B: Extract 2D ==> 3D
//********************************************************************

ans[] =  Extrude{0,width,0}{Surface{5}; Layers{width/mesh_size}; Recombine;};


Transfinite Surface "*";
Recombine Surface "*";

//********************************************************************
// Part C: Define Physical Group
//********************************************************************

leftmost_surface[] = {14};
rightmost_surface[] = {22};
bottom_surface[] = {26}; 

Physical Surface("leftmost_surface") = leftmost_surface[];
Physical Surface("rightmost_surface") = rightmost_surface[];
Physical Surface("bottom_surface") = bottom_surface[];

Physical Volume("all_volume") = {1} ; 

