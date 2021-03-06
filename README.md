# Setup and run PyECLOUD

## Setup PyECLOUD
Follow instructions here: https://github.com/PyCOMPLETE/PyECLOUD/wiki/How-to-install-PyECLOUD

For this example only the part related to buildup simulations is reuqired.

## Set your pythonpath
To run the example you should have the folder containing PyECLOUD, PyPIC and PyKLU in your PYTHONPATH.

E.g. assuming that you have cloned into the folder /home/gianni/pytools:
```
export PYTHONPATH:$PYTHONPATH:/home/gianni/pytools/
```

## Clone the example on your computer
```
git clone https://github.com/lgiacome/PyECOLUDexamples
```

## Run the example
```
cd /home/giadarol/Desktop/test_with_lorenzo/PyECOLUDexamples/scripts
python 000_run_simulation.py
```

## Plot some of the simulation output
Open ipython in interactive matplotlib mode:
```
ipython --pylab
```
In ipython:
```
run 001_plot_main_output.py
```

Some description of the code input and output are provided in [PyECLOUD manual](https://raw.githubusercontent.com/PyCOMPLETE/PyECLOUD/master/doc/reference/reference.pdf). Input is defined in input files, but the same parameters can be passed also as keywords argument when building the BuildupSim object.

More advanced examples can be found in:

https://github.com/PyCOMPLETE/PyECLOUD/tree/master/other

https://github.com/PyCOMPLETE/PyECLOUD/tree/master/testing/test_buildup


