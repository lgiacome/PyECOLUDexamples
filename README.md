
# Install PyECLOUD
The installation procedure has been tested only on Linux. To install **PyECLOUD** the following modules and libraries need to be installed:
 * Python 2.7+
 * numpy
 * scipy
 * matplotlib (mainly for examples and tests)
 * cython
 * f2py 

## Install on linux having root permission
The PyECLOUD code can be downloaded from the git repository https://github.com/PyCOMPLETE/PyECLOUD. This repository also contains a Wiki with the documentation of the code.
To download and install PyECLOUD on a **Linux** machine open a terminal and set up the environment variable `install_path` which indicates the directory in which PyECLOUD and the auxiliary CERN modules PyKLU and PyPIC will be downloaded. 
Eg:

    export install_path=$HOME/PyECLOUD_directory/

Then PyECLOUD can be simply installed by running the command

    sh install_linux.sh

## Install on Linux without root permission
On SLC 6 it is recommended to install Anaconda and use pip to install the missing modules. Alternative it is possible to compile and install python following the instruction here (the step concerning mpi4py can be skipped):

    

 - [Setup python (including mpi4py) without admin rights](https://github.com/PyCOMPLETE/PyECLOUD/wiki/Setup-python-%28including-mpi4py%29-without-admin-rights)


