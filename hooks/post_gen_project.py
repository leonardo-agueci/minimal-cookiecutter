import time

help = """
Your project has been created!
_____________________________________________________________________________
                            ___________ _
  \/                    __/   .::::.-'-(/-/)
                     _/:  .::::.-' .-'\/\_`*******            __ (_))
        \/          /:  .::::./   -._-.  d\|                 (_))_(__))
                     /: ("'"'/    '.  (__/||             (_))__(_))--(__))
                      \::).-'  -._  \/ \\/\|
              __ _ .-'`)/  '-'. . '. |  (i_O
          .-'      \       -'      '\|
     _ _./      .-'|       '.  (    \\                           % % %
  .-'   :      '_  \         '-'\  /|/      @ @ @               % % % %
 /      )\_      '- )_________.-|_/^\      @ @ @@@             % %\/% %
 (   .-'   )-._-:  /        \(/\'-._ `.     @|@@@@@              ..|........
  (   )  _//_/|:  /          `\()   `\_\     |/_@@               )'-._.-._.-
   ( (   \()^_/)_/             )/      \\    /                  /   /
    )  _.-\\.\(_)__._.-'-.-'-.//_.-'-.-.)\-'/._                /       
.-.-.-'   _o\ \\\     '::'   (o_ '-.-' |__\'-.-;~ ~ ~ ~ ~ ~ ~~/   /\   
          \ /  \\\__          )_\    .:::::::.-'\            '- - -|
     :::''':::::^)__\:::::::::::::::::'''''''-.  \                  '- - - - 
    :::::::  '''''''''''   ''''''''''''':::. -'\  \       C. SWANSIGER
_____':::::_____________________________________\__\_________________________

"""
instructions = """
If you have not done so already, create a python virtual environment for your new 
project:

- Using uv (recommended)
# Run if you don't have uv installed
pip install uv
# Create the environment (no ne)
cd {{cookiecutter.repo_name}}
uv venv --python 3.10
# Install dependencies
uv install

- Using conda

cd {{cookiecutter.repo_name}}
conda create --name {{cookiecutter.repo_name}} python=3.11
conda activate {{cookiecutter.repo_name}}
conda env export > environment.yml

Install your new project in your local conda environment with:

pip install -e .

IMPORTANT: You will need to manually add the environment folder (.venv if you 
used the default in uv) to .gitignore to prevent it from syncing to version 
control.

Don't forget to sync to GitHub. Have fun!
"""
print(help)
time.sleep(3)
print(instructions)

