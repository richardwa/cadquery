# My CadQuery Projects

## Setup
* https://cadquery.readthedocs.io/en/latest/installation.html#installation
  * conda install -c conda-forge -c cadquery cadquery=2
  * conda install -c cadquery -c conda-forge cq-editor=2
* https://github.com/michaelgale/cq-kit
  * git clone https://github.com/michaelgale/cq-kit.git
  * cd cq-kit
  * python setup.py install
* code is referenced in module fashion, always invoke using python -m from project root

## Start Viewer
* python -m viewer

## Build STL
* python -m build ./cq_files/example.py

## Run a plain file (debugging)
* python -m cq_files.example

## Pipeline (WIP)
* source code --> stl --> slicer --> printer
* pipeline.bat ./cq_files/example.py

