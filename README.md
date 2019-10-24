# UEA Python ppd course
IPython Jupyter Notebooks for the June 2019 Python ppd course

To interact with the course notebooks requires three steps:
## 1. Install Anaconda
If you are using a UEA laptop, install Anaconda from the UEA software centre
If you are using a personal laptop, install it [following these instructions](https://docs.anaconda.com/anaconda/install/)
## 2. Download the materials
Clone this repo with git or download as a zip file using the green button then unzip the folder
## 3. Create the environment
3.1. Make sure Anaconda is installed and the course materials are downloaded

3.2. Open the command line (e.g., OS X terminal on Mac; **Anaconda prompt** on Windows)

3.3. Navigate to the cloned / downloaded folder (using `cd` command), for example:

```
cd C:\Users\myname\Downloads\pythoncourse2019-materials\
```
if you don't know where you are in the terminal type `dir` on Windows or `pwd` on Linux/Mac

3.4. Create the environment using `conda` package manager:

```bash
conda env create -f environment.yml
```
This will take some time depending on your Internet speed (<15 minutes).

## 4. Activate the environment
### Linux / Mac
If your default shell is NOT bash, first type `bash`. Activate the relevant environment by typing:
```bash
source activate course2019
```
### Windows
Still in the command line (Anaconda prompt), type:
```
activate course2019
```

## 5. Launch Jupyter
Once the environment is activated, type 
```
jupyter notebook
```
in the command line. This should open Jupyter Notebooks in your browser. If you're not sure what you should see, check one of the links below

## Still having troubles?
Experience Python from the comfort of your browser!

- View a static version online with [nbviewer](https://nbviewer.jupyter.org/github/callumrollo/ppd_python/tree/107939c27e7d847de93957f088e71c9c116c658d/)
- Launch the notebooks interactively in the cloud with Binder
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/callumrollo/ppd_python/107939c27e7d847de93957f088e71c9c116c658d)
 may take a few minutes to load
