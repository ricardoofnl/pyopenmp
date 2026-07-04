cmake_minimum_required(VERSION 3.15)
project(pyopenmp C)

find_package(Python3 REQUIRED COMPONENTS Development.Embed)

add_library(pyopenmp SHARED pyopenmp.c)
set_target_properties(pyopenmp PROPERTIES PREFIX "")
target_link_libraries(pyopenmp PRIVATE Python3::Python)
