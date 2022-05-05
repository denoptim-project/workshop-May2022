# Installation
The goal of the present instructions is to prepare your machine for the hand-on exercises of the workshop. To this end, we will:
* ensure you have **conda** on your system, or install it,
* create an environment for running **denoptim**,
* download data sets needed for the exercises.

Since **conda** is extremely popular in data sciences, chances are you already have it installed and know how to use it. In this case, you can jump directly to the section [Create DENOPTIM Environment](#Create_DENOPTIM_Environment).

The instructions are inspired by and derived from work by [Software Carpentry](http://software-carpentry.org) and [CodeRefinery](https://coderefinery.org/) which is licensed under the terms of the [Creative Commons Attribution license 4.0](https://creativecommons.org/licenses/by-sa/4.0/). 

## Command line
On **macOS/Linux** you can use the default Terminal and skipp this section.
On **Windows you** can install GitBash following the steps below or by watching the
  [Carpentries video tutorial](https://www.youtube-nocookie.com/embed/339AEqk9c-8?modestbranding=1&playsinline=1&iv_load_policy=3&rel=0).

  - Download the [Git for Windows installer](https://gitforwindows.org/).
  - Run the installer and follow the steps below:
    1.  Click on "Next" four times (two times if you've previously
        installed Git).  You don't need to change anything
        in the Information, location, components, and start menu screens.
    2.  **From the dropdown menu select "Use the Nano editor by default"
        (NOTE: you will need to scroll <emph>up</emph> to find it) and click on "Next".**
    3.  On the page that says "Adjusting the name of the initial branch in new repositories", ensure that
        "Let Git decide" is selected. This will ensure the highest level of compatibility for our lessons.
    4.  Ensure that "Git from the command line and also from 3rd-party software" is selected and
        click on "Next". (If you don't do this Git Bash will not work properly, requiring you to
        remove the Git Bash installation, re-run the installer and to select the "Git from the
        command line and also from 3rd-party software" option.)
    5.  Ensure that "Use the native Windows Secure Channel Library" is selected and click on "Next".
    6.  Ensure that "Checkout Windows-style, commit Unix-style line endings" is selected and click on "Next".
    7.  **Ensure that "Use Windows' default console window" is selected and click on "Next".**
    8.  Ensure that "Default (fast-forward or merge) is selected and click "Next"
    9.  Ensure that "Git Credential Manager <strong>Core</strong>" is selected and click on "Next".
    10. Ensure that "Enable file system caching" is selected and click on "Next".
    11. Click on "Install".
    12. Click on "Finish" or "Next".
  - If your "HOME" environment variable is not set (or you don't know what this is):
    1.  Open command prompt (Open Start Menu then type `cmd` and press enter)
    2.  Type the following line into the command prompt window exactly as shown: `setx HOME "%USERPROFILE%"`
    3.  Press enter, you should see `SUCCESS: Specified value was saved.`
    4.  Quit command prompt by typing `exit` then pressing enter.

  This will provide you with both Git and Bash in the Git Bash program. You can then start it by searching for "Git Bash" in your Start menu.

  *Text copied and adapted from: [the Carpentries set up page](https://carpentries.github.io/workshop-template/#shell)*


## Install Conda

Miniconda (and Anaconda, too) comes with a complete Python distribution that lets
you create isolated **environments** that don't affect anything else.
**conda** is the tool that manages these environments.

### Do I have conda?
On **macOS/Linux**, open a Terminal and run the following command. On **Windows**, open the Anaconda promt from the Windows search bar (if Anaconda Prompt is not found, then install Miniconda as shown below): 

```conda list```

If you have conda installed, a list of packages will be printed and you can skip the installation and go to the upgrade section.

### Installation: If you don't have Miniconda or Anaconda at all

- From the [Miniconda installer page](https://docs.conda.io/en/latest/miniconda.html),
  download Miniconda3 installer with the latest Python version.
- Follow [regular installation instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation)
  of your operating system.
- Make sure selecting:
    - installing just for you
    - "Add miniconda3 to my PATH environment variable"
    - "Register Miniconda3 as my default Python 3.9"


### Upgrade: If you have Miniconda or Anaconda but you have not used it for a long time

- If you have only old Anaconda, but not Miniconda, then install Miniconda3
  following the instruction above.
- If you have old Miniconda (no matter if you have Anaconda or not), follow the
  instruction below and upgrade Conda. Please replace `anaconda` with `conda`
  in the instruction for Windows and macOS:
    - [Windows](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/windows.html#updating-conda)
    - [macOS](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/macos.html#updating-anaconda-or-miniconda)
    - [Linux](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/linux.html#updating-anaconda-or-miniconda)


### Setting path to Conda from your terminal shell 

This step is usually not needed, but if after the installation you still get an error message like `conda command not found` whey you type `conda --version` in your shell terminal.

#### Windows
  1. Go to the Miniconda3 (or if you have a relatively new Anaconda, then
     Anaconda3) folder. You can find it by serching from File Explorer search
     bar.
  2. Navigate to `etc` folder, and then to `profile.d` folder. You will find
     the `conda.sh` file.
  3. In the folder, right click and choose "Git Bash Here". You should be able
     to see the path to this folder in the Git Bash (something like
     ~/Miniconda3/etc/profile.d).
  4. Run the following command (type the following and enter):
     ```shell
     $ echo ". '${PWD}'/conda.sh" >> ~/.bashrc
     ```
  5. Close Git Bash and reopen it.
  6. Verify that now Git Bash can "see" conda by running `conda --version`
  After step 5 you may see this warning but this is nothing to worry about and will
  not show up the next time you open Git Bash:
  ```
  WARNING: Found ~/.bashrc but no ~/.bash_profile, ~/.bash_login or ~/.profile.
  This looks like an incorrect setup.
  A ~/.bash_profile that loads ~/.bashrc will be created for you.
  ```
  *Reference: ["Setting Up Conda in Git Bash", Sep 2020, at Codecademy
  Forums](https://discuss.codecademy.com/t/setting-up-conda-in-git-bash/534473)*

#### macOS
  1. Open a terminal window.
  2. Find the `.zshrc` file (or `.bash_profile` if your shell is Bash)
     which should be located in your home directory
     (/User/your-user-name)
  3. Navigate to the directory where `.zshrc` is located (or `.bash_profile` if your shell is Bash).
  4. Add the following in `.zshrc` file (or `.bash_profile`):
  ```shell
  export PATH="$HOME/miniconda3/bin:$PATH"
  ```

#### Linux
  1. Open a terminal window.
  2. Run this command which will append to your `.bashrc` file (adapt the path if Miniconda has been installed
     to a different place):
  ```shell
  $ echo 'source $HOME/miniconda3/bin/activate' >> ~/.bashrc
  ```
  If you prefer not to edit your `.bashrc`, you can also run this command after opening your terminal (each time you open one)
  and it will bring all `conda` commands "into view":
  ```shell
  $ source $HOME/miniconda3/bin/activate
  ```


### How to uninstall/remove Conda

If you wish to remove Conda again after the workshop, here is how:

- [Windows](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/windows.html#uninstalling-conda)
- [macOS](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/macos.html#uninstalling-anaconda-or-miniconda)
- [Linux](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/linux.html#uninstalling-anaconda-or-miniconda)


## Create DENOPTIM Environment

We now ask **conda** to create a dedicated environment for the workshow. The environment required **DENOPTIM** do **conda** will install is and make it available within such environment.
1. Open a new terminal (macOS/Linux) or a new GitBash (Windows) after having completed the installation of **conda**.
2. If you have not, activate `conda` in Miniconda first using `conda activate` or `source ~/miniconda3/bin/activate`. If neither works, please first follow {ref}`setting-conda-path`. You probably need to restart your shell terminal. Then try `conda activate` or `source ~/miniconda3/bin/activate` again.
3. Run the following command:
```
conda env create -f  https://raw.githubusercontent.com/denoptim-project/workshop-May2022/main/environment.yml
```
4. Make sure that you see "dnp_workshop" in the output when you ask for a list of all available environments:
```
conda env list
```

### Activating the `dnp_workshop` environment

In the workshop, we will ask you to activate this environment. 

First, follow the steps 1 and 2 above (i.e. open your terminal shell and activate `conda`).
Then run the following:
```
conda activate dnp_workshop
```

If this does not work, the `dnp_workshop` part should be replaced with the whole path, for example:
```
source activate ~/Miniconda3/envs/coderefinery
```


### How to verify the environment

Once activated, try the following 5 commands:
```
denoptim -v
```

You should see an output like this and not see errors (exact version numbers are not too important):
```
V3.1.0
```


### Deactivating the `dnp_workshop` environment
Deactivating will remove the `denoptim` command, so it is an operation meant for when you are done working with the software. After deactivating, you can always re-activate the environment again.
```
conda deactivate
```

