## Installing Pymol on MacOSX

1. Install pymol throguh homebrew
   
   ```brew tap brewsci/bio```
   
   ```brew install pymol```
3. Create conda environment
   
   ```conda create -n pymolenv python=3.12```
4. Add pymol to your python path
   
   ```export PYTHONPATH=$PYTHONPATH:/opt/homebrew/Cellar/pymol/3.0.0/libexec/lib/python3.12/site-packages/ ```



