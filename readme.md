# My CadQuery Projects

## Setup
* https://cadquery.readthedocs.io/en/latest/installation.html#installation
  * conda install -c conda-forge -c cadquery cadquery=2
  * conda install -c cadquery -c conda-forge cq-editor=2
* https://github.com/michaelgale/cq-kit
  * git clone https://github.com/michaelgale/cq-kit.git
  * cd cq-kit
  * python setup.py install
* setup my own extension
  * conda install conda-build
  * conda develop .\cqextension\

## Start Viewer
* CQ-editor.exe

## Build STL
* python build.py ./project/example.py

## Run a plain file
* python -m project.example

## Pipeline (WIP)
* source code --> stl --> slicer --> printer
* pipeline.bat ./project/example.py

