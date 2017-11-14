//****************************************************************
// Real-ESSI Short Course 
// 		Day 2: Motions
// Model Component: Soil-Foundation
//****************************************************************

//****************************************************************
// Predefined Parameters
//****************************************************************

total_height = 50 ;
total_width = 210 ;

Ox = 0;
Oy = 0;
Oz = -total_height;

epsilon =0.001 ;
//epsilon = 2 ;

mesh_size = 5;



//**************************************************************************************************
// Part A: Soil
//**************************************************************************************************
// Soil: 
p1 = newp; Point(p1) = {Ox, Oy, Oz};

ans[] = Extrude{total_width,0,0}{Point{p1};Layers{total_width/mesh_size};Recombine;} ; 
l1 = ans[1];
ans[] = Extrude{0,total_width,0}{Line{l1};Layers{total_width/mesh_size};Recombine;} ; 
s1 = ans[1];
ans[] = Extrude{0,0,total_height}{Surface{s1};Layers{total_height/mesh_size};Recombine;} ; 

Physical Volume("all_soil") = {1} ;
Physical Surface("soil_bottom") = {5} ;


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




