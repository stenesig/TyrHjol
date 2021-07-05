# TýrHjól

## The virtual drinking wheel

Run the program to spin the wheel, and press your preferred button to spin it again!

Works with all kinds of custom wheels, just place them in the images directory and modify the NUMBER_OF_RESULTS constant to reflect the number of results on your wheel



### Installing

(recommended) Start by creating a virtual environment in the root directory of the project

```bash
python -m venv .venv
```

Activate the virtual environment

Windows
```bash
. .venv/Scripts/activate
```
Linux
```bash
. .venv/bin/activate
```

Installed the required packages
```bash
pip install -r requirements.txt
```

You can now spin the wheel!

```bash
python wheel.py
```