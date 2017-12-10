

sed -i '/\/\/\ Define\ damping/,/add\ damping\ \#\ 5\ type\ Rayleigh/ d' main.fei
sed -i '/include\ \"load\.fei\";/ d' main.fei
sed -i '/include\ \"boundary_condition\.fei\"/ d' main.fei
sed -i '/include\ \"damping/ d' main.fei
 
sed -i '/include\ \"element\.fei\";/ a include\ \"boundary_condition\.fei\";' main.fei
sed -i '/include\ \"element\.fei\";/ a include\ \"damping\.fei\";' main.fei
sed -i '/include\ \"element\.fei\";/ a include\ \"damping_parameters\.fei\";' main.fei




sed -i '/\/\/\ Wave\ propagation/,/\/\/\ Dynamic\ Domain/ d' main.fei


sed -i '/include\ \"material/ d' main.fei
sed -i '/include\ \"wave/ d' main.fei
sed -i '/Choice\ of\ materials,\ comment\ or/ d' main.fei
sed -i '/If\ you\ change\ material\ here,\ you/ d' main.fei
sed -i '/\/\/\ wave\ field\ too\!/ d' main.fei

sed -i '/\/\/\ Define\ Material\ and\ Geometry/ a \/\/\ Choice\ of\ materials,\ comment\ or\ uncomment\ lines\ below' main.fei
sed -i '/\/\/\ Choice\ of\ materials,\ comment\ or\ uncomment\ lines\ below/ a \/\/\ If\ you\ change\ material\ here,\ you\ have\ to\ change' main.fei
sed -i '/\/\/\ If\ you\ change\ material\ here,\ you\ have\ to\ change/ a \/\/\ wave\ field\ too\!' main.fei

sed -i '/\/\/\ wave\ field\ too\!/ a include\ \"material_set1\.fei\";' main.fei
sed -i '/include\ \"material_set1\.fei/ a include\ \"wave_field1\.fei\";' main.fei
sed -i '/include\ \"wave_field1\.fei/ a \/\/\/\ include\ \"material_set2\.fei\";' main.fei
sed -i '/\/\/\/\ include\ \"material_set2\.fei/ a \/\/\/\ include\ \"wave_field2\.fei\";' main.fei
sed -i '/\/\/\/\ include\ \"wave_field2\.fei/ a \/\/\/\ include\ \"material_set3\.fei\";' main.fei
sed -i '/\/\/\/\ include\ \"material_set3\.fei/ a \/\/\/\ include\ \"wave_field3\.fei\";' main.fei

sed -i '/include\ \"wave_field1\.fei/ G' main.fei
sed -i '/\/\/\/\ include\ \"wave_field2\.fei/ G' main.fei

