//****************************************************************
// Real-ESSI Short Course 
// 		Day 2: Motions
// Model Component: Soil-Foundation
//****************************************************************

//****************************************************************
// Predefined Parameters
//****************************************************************
mesh_size = 5;
width_of_out_foundation = mesh_size; 

height_of_structure = 60 ;
sub_height = 20;

depth_of_foundation = 5 ;
raw_width_of_structure = 30 ;
width_of_structure = raw_width_of_structure + 2 * width_of_out_foundation ;
depth_of_soil = 40;
width_of_field = width_of_structure * 3 - width_of_out_foundation ;


Ox = 0;
Oy = 0;
Oz = -depth_of_foundation;

epsilon =0.001 ;
//epsilon = 2 ;




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
// Part B: foundation  
//**************************************************************************************************

x_minus_y_minus = newp;  Point(x_minus_y_minus) = {Ox + width_of_field + epsilon, Oy + width_of_field + epsilon, Oz +  epsilon}; 
ans[] =  Extrude{width_of_out_foundation,0,0}{ Point{x_minus_y_minus} ; Layers{ Ceil(width_of_out_foundation/mesh_size)}; Recombine;};
l11 = ans[1];
ans[] =  Extrude{(width_of_structure/2. - width_of_out_foundation - epsilon),0,0}{ Point{ans[0]} ; Layers{ Ceil((width_of_structure/2. - width_of_out_foundation - epsilon)/mesh_size)}; Recombine;};
l12 = ans[1];
ans[] =  Extrude{(width_of_structure/2. - width_of_out_foundation - epsilon),0,0}{ Point{ans[0]} ; Layers{ Ceil((width_of_structure/2. - width_of_out_foundation - epsilon)/mesh_size)}; Recombine;};
l13 = ans[1];
ans[] =  Extrude{width_of_out_foundation,0,0}{ Point{ans[0]} ; Layers{ Ceil(width_of_out_foundation/mesh_size)}; Recombine;};
l14 = ans[1];

foundation_bottom_surfaces[] = {} ;

ans[] =  Extrude{0,width_of_out_foundation,0}{ Line{l11,l12,l13,l14} ; Layers{ Ceil(width_of_out_foundation/mesh_size)}; Recombine;};
l11 = ans[0]; l12 = ans[4]; l13 = ans[8]; l14 = ans[12] ; 
foundation_bottom_surfaces[] = {foundation_bottom_surfaces[], ans[1], ans[5], ans[9], ans[13]} ;

ans[] =  Extrude{0,(width_of_structure/2. -(width_of_out_foundation + epsilon)),0}{ Line{l11,l12,l13,l14} ; Layers{ Ceil((width_of_structure/2. - (width_of_out_foundation + epsilon))/mesh_size)}; Recombine;};
l11 = ans[0]; l12 = ans[4]; l13 = ans[8]; l14 = ans[12] ; 
foundation_bottom_surfaces[] = {foundation_bottom_surfaces[], ans[1], ans[5], ans[9], ans[13]} ;

ans[] =  Extrude{0,(width_of_structure/2. -(width_of_out_foundation + epsilon)),0}{ Line{l11,l12,l13,l14} ; Layers{ Ceil((width_of_structure/2. - (width_of_out_foundation + epsilon))/mesh_size)}; Recombine;};
l11 = ans[0]; l12 = ans[4]; l13 = ans[8]; l14 = ans[12] ; 
foundation_bottom_surfaces[] = {foundation_bottom_surfaces[], ans[1], ans[5], ans[9], ans[13]} ;

ans[] =  Extrude{0,width_of_out_foundation,0}{ Line{l11,l12,l13,l14} ; Layers{ Ceil(width_of_out_foundation/mesh_size)}; Recombine;};
l11 = ans[0]; l12 = ans[4]; l13 = ans[8]; l14 = ans[12] ; 
foundation_bottom_surfaces[] = {foundation_bottom_surfaces[], ans[1], ans[5], ans[9], ans[13]} ;


//x_plus_y_minus = newp; Point(x_plus_y_minus) = {Ox + width_of_field + width_of_structure - epsilon, Oy + width_of_field + epsilon, Oz +  epsilon}; 



//ans[] =  Extrude{width_of_out_foundation,0,0}{ Line{x_minus_line} ; Layers{ Ceil(width_of_out_foundation/mesh_size)}; Recombine;};
//ans[] =  Extrude{0,width_of_out_foundation,0}{ Line{y_minus_line} ; Layers{ Ceil(width_of_out_foundation/mesh_size)}; Recombine;};
//ans[] =  Extrude{-width_of_out_foundation,0,0}{ Line{x_plus_line} ; Layers{ Ceil(width_of_out_foundation/mesh_size)}; Recombine;};
//ans[] =  Extrude{0,-width_of_out_foundation,0}{ Line{y_plus_line} ; Layers{ Ceil(width_of_out_foundation/mesh_size)}; Recombine;};

//x_minus_y_plus = newp; Point(x_minus_y_plus) = {Ox + width_of_field + epsilon, Oy + width_of_field + width_of_structure - epsilon, Oz +  epsilon}; 
//x_plus_y_plus = newp; Point(x_plus_y_plus) = {Ox + width_of_field + width_of_structure - epsilon, Oy + width_of_field + width_of_structure - epsilon, Oz +  epsilon}; 

//y_minus_line = newl; Line(y_minus_line) = {x_minus_y_minus, x_plus_y_minus};
//y_plus_line = newl; Line(y_plus_line) = {x_minus_y_plus, x_plus_y_plus};
//x_minus_line = newl; Line(x_minus_line) = {x_minus_y_minus, x_minus_y_plus};
//x_plus_line = newl; Line(x_plus_line) = {x_plus_y_plus, x_plus_y_minus};

//Transfinite Line(y_minus_line) = (width_of_structure/mesh_size) + 1 ; 
//Transfinite Line(y_plus_line) = (width_of_structure/mesh_size) + 1 ; 
//Transfinite Line(x_minus_line) = (width_of_structure/mesh_size) + 1 ; 
//Transfinite Line(x_plus_line) = (width_of_structure/mesh_size) + 1 ; 

////loop1 = newreg; Line Loop(loop1) = {x_minus_line,y_plus_line,x_plus_line,-y_minus_line} ;
////foundation_bottom_surface = news; Plane Surface(foundation_bottom_surface) = {loop1};
ans[] = Extrude{0,0,depth_of_foundation}{Surface{foundation_bottom_surfaces[]} ;Layers{depth_of_foundation/mesh_size};Recombine;};

////foundation_top_surface                        = ans[0] ;
//foundation_x_minus_vol[] = {ans[1], ans[19], ans[37] };
//foundation_x_plus_vol[] = {ans[13], ans[31], ans[49] };
//foundation_y_minus_vol[] = {ans[1], ans[7], ans[13] };
//foundation_y_plus_vol[] = {ans[37], ans[43], ans[49] };

//foundation_around_volume[]  = {ans[1], ans[7], ans[13], ans[19], ans[31], ans[37], ans[43], ans[49]} ;
foundation_volume[]  = {18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33} ;

foundation_x_plus_surface[]                    = {824, 736, 648, 560}   ;
foundation_y_plus_surface[]                     = {762, 784, 806, 828}  ;
foundation_x_minus_surface[]                     = {678, 766, 590, 502}  ;
foundation_y_minus_surface[]                    = {490, 512, 534, 556}  ;

//Physical Volume("foundation_x_minus_vol")          = foundation_x_minus_vol[] ;
//Physical Volume("foundation_x_plus_vol")          = foundation_x_plus_vol[] ;
//Physical Volume("foundation_y_minus_vol")          = foundation_y_minus_vol[] ;
//Physical Volume("foundation_y_plus_vol")          = foundation_y_plus_vol[] ;

//Physical Volume("foundation_around_volume")          = foundation_around_volume[] ;
Physical Volume("foundation_volume")          = foundation_volume[] ;

shell_bottom_surface[] = {701, 723, 613, 635} ;
Physical Surface("shell_bottom_surface")    = shell_bottom_surface[] ;

Physical Surface("foundation_bottom_surfaces") = foundation_bottom_surfaces[] ;

Physical Surface("foundation_x_plus_surface") = foundation_x_plus_surface[] ;
Physical Surface("foundation_y_plus_surface")  = foundation_y_plus_surface[] ;
Physical Surface("foundation_x_minus_surface")  = foundation_x_minus_surface[] ;
Physical Surface("foundation_y_minus_surface") = foundation_y_minus_surface[] ;

embed_around_surfaces[] = {670, 696, 718, 714, 626, 542, 520, 582} ; 
embed_mid_surfaces[] = {604, 608, 692, 630} ; 
embed_surfaces[] = {embed_around_surfaces[], embed_mid_surfaces[]} ; 
Physical Surface("embed_around_surfaces") = embed_around_surfaces[];
Physical Surface("embed_mid_surfaces") = embed_mid_surfaces[];
Physical Surface("embed_surfaces") = embed_surfaces[] ;

////Physical Surface("all_foundation_surfaces") = {shell_bottom_surface, foundation_x_minus_surface, foundation_y_plus_surface, foundation_x_plus_surface, foundation_y_minus_surface} ;

//Physical Volume("soil_and_foundation_vol")          = {foundation_volume, all_soils} ;

//////**************************************************************************************************
////// Part C.1 : Shell super-structure
//////**************************************************************************************************


////x_minus_y_minus = newp;  Point(x_minus_y_minus) = {Ox + width_of_field + width_of_out_foundation + epsilon, Oy + width_of_field + width_of_out_foundation + epsilon, Oz + depth_of_foundation + epsilon}; 
////x_plus_y_minus = newp; Point(x_plus_y_minus) = {Ox + width_of_field + width_of_structure - width_of_out_foundation - epsilon, Oy + width_of_field + width_of_out_foundation + epsilon, Oz + depth_of_foundation + epsilon}; 
////x_minus_y_plus = newp; Point(x_minus_y_plus) = {Ox + width_of_field + width_of_out_foundation + epsilon, Oy + width_of_field + width_of_structure - width_of_out_foundation - epsilon, Oz + depth_of_foundation + epsilon}; 
////x_plus_y_plus = newp; Point(x_plus_y_plus) = {Ox + width_of_field + width_of_structure - width_of_out_foundation - epsilon, Oy + width_of_field + width_of_structure - width_of_out_foundation - epsilon, Oz + depth_of_foundation + epsilon}; 

////y_minus_line = newl; Line(y_minus_line) = {x_minus_y_minus, x_plus_y_minus};
////y_plus_line = newl; Line(y_plus_line) = {x_minus_y_plus, x_plus_y_plus};
////x_minus_line = newl; Line(x_minus_line) = {x_minus_y_minus, x_minus_y_plus};
////x_plus_line = newl; Line(x_plus_line) = {x_plus_y_plus, x_plus_y_minus};

////Transfinite Line(y_minus_line) = (width_of_structure/mesh_size) + 1 ; 
////Transfinite Line(y_plus_line) = (width_of_structure/mesh_size) + 1 ; 
////Transfinite Line(x_minus_line) = (width_of_structure/mesh_size) + 1 ; 
////Transfinite Line(x_plus_line) = (width_of_structure/mesh_size) + 1 ; 

////// Select by GUI
////Line Loop(473) = {442, -445, -443, -444};
////shell_bottom_surface = newl; Plane Surface(shell_bottom_surface) = {473};
////embedded_shell_top_surface[] = {shell_bottom_surface} ;
////embedded_shell_top_surface[] = {shell_bottom_surface} ;

////// extrude shell structure up
N_extrude = 3 ; 
shell_super_surfaces[] = {};
//shell_bottom_surface = 701 ; 
For z_direction In {1 : N_extrude}
ans[] = Extrude{0,0,sub_height}{Surface{shell_bottom_surface[]} ;Layers{sub_height/mesh_size};Recombine;};
	shell_bottom_surface[] = {ans[0], ans[6], ans[12], ans[18]} ; 
	Delete{
		Volume{ans[1]};
		Volume{ans[7]};
		Volume{ans[13]};
		Volume{ans[19]};
	}
	For i In {0:3}
		shell_super_surfaces[] = { shell_super_surfaces[], ans[i*6] } ; 
		shell_super_surfaces[] = { shell_super_surfaces[], ans[i*6+2] } ; 
		shell_super_surfaces[] = { shell_super_surfaces[], ans[i*6+3] } ; 
		shell_super_surfaces[] = { shell_super_surfaces[], ans[i*6+4] } ; 
		shell_super_surfaces[] = { shell_super_surfaces[], ans[i*6+5] } ; 
	EndFor
EndFor
shell_super_surfaces[] = { shell_super_surfaces[], shell_bottom_surface[] } ; 

////// Internal shell surfaces.
//x_minus_mid = newp;  Point(x_minus_mid) = {Ox + width_of_field + width_of_out_foundation + epsilon, Oy + width_of_field  + width_of_structure/2 , Oz + depth_of_foundation + epsilon}; 
//x_plus_mid = newp; Point(x_plus_mid) = {Ox + width_of_field + width_of_structure - width_of_out_foundation - epsilon, Oy + width_of_field + width_of_structure/2 , Oz + depth_of_foundation + epsilon}; 
//y_minus_mid = newp; Point(y_minus_mid) = {Ox + width_of_field + width_of_structure/2 , Oy + width_of_field + width_of_out_foundation + epsilon, Oz + depth_of_foundation + epsilon}; 
//y_plus_mid = newp; Point(y_plus_mid) = {Ox + width_of_field  + width_of_structure/2 , Oy + width_of_field + width_of_structure - width_of_out_foundation - epsilon, Oz + depth_of_foundation + epsilon}; 

//x_mid = newl; Line(x_mid) = {x_minus_mid, x_plus_mid} ;
//y_mid = newl; Line(y_mid) = {y_minus_mid, y_plus_mid} ;
//Transfinite Line(x_mid) = (width_of_structure/mesh_size) + 1 ; 
//Transfinite Line(y_mid) = (width_of_structure/mesh_size) + 1 ; 

//ans[] = Extrude{0,0,height_of_structure}{Line{x_mid,y_mid};Layers{height_of_structure/mesh_size};Recombine;} ; 
//shell_super_mid_surfaces = {ans[1], ans[5]} ;
//shell_super_all_surfaces[] = { shell_super_around_surfaces[], shell_super_mid_surfaces[] } ; 	

//Physical Surface("shell_super_around_surfaces") = shell_super_around_surfaces[];
//Physical Surface("shell_super_mid_surfaces") = shell_super_mid_surfaces[];
//Physical Surface("shell_super_all_surfaces") = shell_super_all_surfaces[];
Physical Surface("shell_super_surfaces") = shell_super_surfaces[];


//////**************************************************************************************************
////// Part C.2 : Shell embedded-structure
//////**************************************************************************************************
////// extrude down the embedded_shell 
////// (1) around the foundation
////shell_embed_around_surfaces = {} ; 
////ans[] = Extrude{0,0, - depth_of_foundation }{Surface{embedded_shell_top_surface} ;Layers{depth_of_foundation/mesh_size};Recombine;};
////shell_bottommost_surface = ans[0];
////Delete{
////	Volume{ans[1]};
////}
////shell_embed_around_surfaces[] = { shell_embed_around_surfaces[], ans[2] } ; 
////shell_embed_around_surfaces[] = { shell_embed_around_surfaces[], ans[3] } ; 
////shell_embed_around_surfaces[] = { shell_embed_around_surfaces[], ans[4] } ; 
////shell_embed_around_surfaces[] = { shell_embed_around_surfaces[], ans[5] } ; 
////Physical Surface("shell_embed_around_surfaces") = shell_embed_around_surfaces[];

////// (2) in the middle of the foundation
//ans[] = Extrude{0,0, -depth_of_foundation}{Line{x_mid,y_mid};Layers{depth_of_foundation/mesh_size};Recombine;} ; 
//shell_embed_mid_surfaces = {ans[1], ans[5]} ; 
//Physical Surface("shell_embed_mid_surfaces") = shell_embed_mid_surfaces[];
////Delete{
////	Surface{embedded_shell_top_surface};
////	Surface{shell_bottommost_surface};
////}
////shell_embed_all_surfaces = {shell_embed_around_surfaces[], shell_embed_mid_surfaces[]};
//shell_embed_all_surfaces = {embed_surfaces[], shell_embed_mid_surfaces[]};
////shell_all_surfaces = {shell_super_all_surfaces[], shell_embed_all_surfaces[]};
shell_all_surfaces[] = {shell_super_surfaces[], embed_surfaces[]};

//Physical Surface("shell_embed_all_surfaces") = shell_embed_all_surfaces[];
Physical Surface("shell_all_surfaces") = shell_all_surfaces[];



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




Physical Line(472) = {449, 469, 448, 450, 465, 464, 466, 456, 468, 453, 452, 460, 470, 454};

