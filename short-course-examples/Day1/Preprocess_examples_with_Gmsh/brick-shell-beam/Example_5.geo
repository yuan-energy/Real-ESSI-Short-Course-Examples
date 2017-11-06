
// ###########################################################################################################################
// #                                                                                                                         #
// #  GMESSI :: Translator for The Real ESSI (Real Earthquake-Soil-Structure Interaction) Simulator                          #
// #  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                                      #
// #                                                                                                                         #
// #  Example_5 : Modeling of a embedded shells and beam                                                                     #
// #                                                                                                                         #
// #  *** geometry file  for this example ***                                                                                #
// #  *** gmessi (.gmessi) file can be located as Example_5.gmessi ***                                                       #
// #                                                                                                                         #
// #  Sumeet Kumar Sinha (July,2017)                                                                                         #
// #  Computational Geomechanics Group                                                                                       #
// #  University of California, Davis                                                                                        #
// #  s u m e e t k s i n h a . c o m                                                                                        #
// ########################################################################################################################### 


Length_Of_Soil = 10;
Width_Of_Soil  = 4;
Depth_Of_Soil  = 10;
Length_of_Beam_Shell = 10;
Embedded_Shell_And_Beam_Depth = 5;

Mesh_Size = 1;
Point(0)={0,0,0};

Extrude {Length_Of_Soil,0,0}{Point{0}; Layers{Length_Of_Soil/Mesh_Size}; Recombine;}
Extrude {0,Width_Of_Soil,0}{Line{1}; Layers{Width_Of_Soil/Mesh_Size}; Recombine;}
Extrude {0,0,-Depth_Of_Soil}{Surface{5}; Layers{Depth_Of_Soil/Mesh_Size}; Recombine;}

Physical Volume ("Soil") ={1};
Physical Surface ("Base") = {27};
Physical Surface ("Lateral_X") = {18,26};
Physical Surface ("Lateral_Y") = {14,22};


///////////////////////// Embedded Beam ////////////////////////////////////////////////////////
NewPoint = newp;
Point(newp) = {3*Mesh_Size,Width_Of_Soil/2,-(Depth_Of_Soil-Embedded_Shell_And_Beam_Depth)};
Extrude {0,0,Embedded_Shell_And_Beam_Depth}{Point{14}; Layers{Embedded_Shell_And_Beam_Depth/Mesh_Size}; Recombine;}
Extrude {0,0,Length_of_Beam_Shell-Embedded_Shell_And_Beam_Depth}{Point{15}; Layers{(Length_of_Beam_Shell-Embedded_Shell_And_Beam_Depth)/Mesh_Size}; Recombine;}

Physical Line ("Embedded_Beam") ={28};
Physical Line ("Exposed_Beam") ={29};
Physical Point ("Top_Of_Beam") = {16};
Physical Point ("Bottom_Of_Beam") = {14};
Physical Line ("Beam") ={28,29};
 

///////////////////////// Embedded Shell ////////////////////////////////////////////////////////
NewPoint = newp;
Point(newp) = {7*Mesh_Size,Width_Of_Soil/4,-(Depth_Of_Soil-Embedded_Shell_And_Beam_Depth)};
Extrude {0,2*Width_Of_Soil/4,0}{Point{17}; Layers{2*Width_Of_Soil/4/Mesh_Size}; Recombine;}
Extrude {0,0,Embedded_Shell_And_Beam_Depth}{Line{30}; Layers{Embedded_Shell_And_Beam_Depth/Mesh_Size}; Recombine;}
Extrude {0,0,Length_of_Beam_Shell-Embedded_Shell_And_Beam_Depth}{Line{31}; Layers{(Length_of_Beam_Shell-Embedded_Shell_And_Beam_Depth)/Mesh_Size}; Recombine;}

Physical Surface ("Embedded_Shell") ={34};
Physical Surface ("Exposed_Shell") ={38};
Physical Line ("Top_Of_Shell") = {35};
Physical Line ("Bottom_Of_Shell") = {30};
Physical Surface ("Shell") ={34,38};




