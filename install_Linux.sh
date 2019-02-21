# check if installation path has been set
if [ -z "$install_path" ]
then
	echo "Please, set install_path environment variable"
	exit 0
fi

# install numpy, scipy, matplotlib, pip, cython, gfortran
sudo apt-get install python-numpy
sudo apt-get install python-scipy
sudo apt-get install python-matplotlib
sudo apt-get install python-pip
sudo pip install cython
sudo apt-get install gfortran

# download PyECLOUD, PyKLU and PyPIC from git
git clone https://github.com/PyCOMPLETE/PyECLOUD $install_path/PyECLOUD
git clone https://github.com/PyCOMPLETE/PyKLU $install_path/PyKLU
git clone https://github.com/PyCOMPLETE/PyPIC $install_path/PyPIC

# install PyPIC
cd $install_path/PyPIC
make

# install PyECLOUD
cd $install_path/PyECLOUD
./setup_pyecloud

# install PyKLU
cd $install_path/PyKLU
./install


