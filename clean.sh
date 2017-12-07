# ##########################################################
# This script is used to clean the output of ESSI Simulation
# ##########################################################

find ./ -name "*.h5.feioutput" -delete
find ./ -name "*.h5.*.feioutput" -delete
find ./ -name "essi_*.log" -delete
find ./ -name "log" -delete
find ./ -name "RealESSI_VERSION_INFO.txt" -delete
find ./ -name "petsc_log.txt" -delete
find ./ -name "*.pyc" -delete
find ./ -name "gmon.out" -delete
find ./ -name "vtk_errors.txt" -delete
find ./ -name "*_RESTART.essi" -delete
find ./ -name "*.swp" -delete
find ./ -name "*.csv" -delete
find ./ -name "benchmark.txt" -delete

