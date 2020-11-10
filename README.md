# UEA Python ppd course


IPython Jupyter Notebooks for UEA Python PPD courses (runs interactively in browser)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ueapy/ppd_python/master)

If you want to get Python and the course materials running locally on your computer (recommended) you must complete a few steps:

## 1. Install Anaconda
If you are using a UEA desktop Anaconda Navigator should already be installed (press the Windows key and start typing anaconda to check)

If you are using a UEA laptop, install Anaconda from the UEA software centre

If you are using a personal laptop, install it [following these instructions](https://docs.anaconda.com/anaconda/install/)

## 2. Download the materials
Clone this repo with git or download as a zip file using the green button then unzip the folder

**UEA machines only**

Due to the unhelpful directory structure of UEA PCs there are several folders called Documents, Downloads etc. in different places. To make life easier in later steps, copy the ppd_python folder to the following location:

`C:\\Users\you-user-name\Documents`

Where your-user-name is your UEA letter-number jumble e.g. foo15bar

You can find this folder by opening the file explorer and going to `This PC` then `Windows (C:)` and double clicking through

## 3. Create the environment and launch the notebooks
Make sure Anaconda is installed and the course materials are downloaded. From here you have two options: use Anaconda navigator (recommended if you are not a UNIX person) or use the command line.

### **Anaconda navigator technique (best for Windows):**

3.1 Open Anaconda Navigator

3.2 Select 'Environments' from the left hand side task bar

3.3 Select 'import' from the bottom left. Press the folder icon, this will open a folder view and you can double click your way to the ppd_python folder you downloaded in step 2. Select the environment.yml file and click the buttons for 'open' then 'import'

![Import environment.yml](https://raw.githubusercontent.com/callumrollo/ppd_python/master/install-images/navigator.PNG)

Anaconda will now download all the extra packages we need. This will take some time depending on your Internet speed (<15 minutes). You will see various loading bars in Anaconda.

You may get a popup that "this app has been blocked by your system administrator" press OK and ignore it.

3.4 Once the installation is complete, select 'home' from the left hand task bar then ppd_python from the drop down list 'Applications on'

3.5 Once ppd_python is selected, press 'launch' on the jupyter notebook icon

![Import environment.yml](https://raw.githubusercontent.com/callumrollo/ppd_python/master/install-images/launch.PNG)


3.6 This will launch jupyter notebooks in a web browser. From here you can navigate Documents then ppd_python. Open the 'notebooks' folder and you are ready to begin

![Import environment.yml](https://raw.githubusercontent.com/callumrollo/ppd_python/master/install-images/jupyter.PNG)


### **Command line technique (best for UNIX):**

3.1. Open the command line (e.g., OS X terminal on Mac; **Anaconda prompt** on Windows)

3.2. Navigate to the cloned / downloaded folder (using `cd` command), for example:

`C:\\Users\you-user-name\Documents\ppd_python`

If you don't know where you are in the terminal type `dir` on Windows or `pwd` on Linux/Mac

If you don't know location of the materials, open your file navigator, right-click the ppd_python you downloaded and select `properties` this will include the location of the file

![Import environment.yml](https://raw.githubusercontent.com/callumrollo/ppd_python/master/install-images/location.PNG)


3.3. Create the environment using `conda` package manager:

```bash
conda env create -f environment.yml
```
This will take some time depending on your Internet speed (<15 minutes).

3.4. Activate the envronment

### Linux / Mac
If your default shell is NOT bash, first type `bash`. Activate the relevant environment by typing:
```bash
source activate ppd_python
```

if this fails try

```bash
conda activate ppd_python
```
### Windows
Still in the command line (Anaconda prompt), type:
```
activate ppd_python
```

3.5. Launch Jupyter
Once the environment is activated, type 
```
jupyter notebook
```
in the command line. This should open Jupyter Notebooks in your browser. If you're not sure what you should see, check one of the links below. Navigate to where you saved the ppd_python folder, open the notebooks folder and you are ready to begin.

## Still having troubles?
If the command line is not doing what you want you may find the graphical interface provided by Anaconda Navigator more convenient.

If you can't find where you saved the ppd_python folder copy it to 

`C:\\Users\you-user-name\Documents`

Alternatively, experience Python from the comfort of your browser!

- View a static version online with [nbviewer](https://nbviewer.jupyter.org/github/callumrollo/ppd_python/tree/47617a2cc12325771b958ad4ebeea02de525c6d4/)
- Launch the notebooks interactively in the cloud with Binder
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ueapy/ppd_python/master) (may take a few minutes to load)
