# Signature

Signature, a tool for updating bunches of email signatures

## Description

This project arises from the need to update the email signatures of a large batch of user accounts. Since it is totally inefficient to ask a person to manually update all accounts, the aim is to automate the task by offering an efficient and unattended solution.

This program has been developed thinking of two possible scenarios:

- The utility runs in a server environment, in text mode, being called by another application or functioning as a service.

- The utility is run in a desktop environment, in graphical mode, by a human operator.

To cover both cases, the tool has been provided with a command interpreter, as well as a wrapper, an independent graphical application that calls the main program, passing the parameters obtained by the graphical application.

## Getting Started

### Requirements

- Python >= 3.7.x
- pip
- Python venv

### Installation

First, go to the project folder and create a virtual environment:

```bash
cd project_folder
```

#### Linux

```bash
python3 -m venv env
```

Then activate the virtual environment:

```bash
source env/bin/activate
```

Upgrade pip:

```bash
python3 -m pip install --upgrade pip
```

Install the project dependencies with pip:

```bash
pip install -r requirements.txt
```

#### Windows
```powershell
python -m venv env
```

If you are using PowerShell you need to change the execution policy:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

Then activate the virtual environment:

```powershell
env\Scripts\activate
```

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install the project dependencies with pip:

```powershell
pip install -r requirements.txt
```

### How to customize signature info

There are four variables you should care about. In the HTML template, you can include it by this way:

- The user's full name: $full_name.
- The user's email address: $email.
- The user's phone number: $telephone.
- The user's job title: $job_title.

It's mandatory to keep the "$" symbol at the beginning of the string.

### How to generate an executable file

Simply go to "signature" folder and run:

```bash
pyinstaller --onefile main.py --name signature
```

This will create an executable inside the "dist" folder.

### How to run it

Firstly, add the program to the system path.

#### Linux

Move the executable file to /usr/bin/:

```bash
mv signature /usr/bin/
```

#### Windows

For security, save a copy of the current path:

```powershell
$env:path >> path.out
```

Now, add a new entry to the path:

```powershell
setx PATH "$env:path;\signature\installation\folder" -m
```

Finally, restart the computer.

Now you can run the program. For help about command options, simply run:

```bash
signature --help
```

You have to provide as arguments the paths of the following files:

- A JSON file containing the Google workspace credentials.
- An HTML file containing the signature template.
- An ODS file (Google Sheets) containing the users' information.

### How to generate a GUI wrapper

Simply go to "gui" folder and run:

```bash
pyinstaller --onefile main.py --name signature-gui
```

This will create an executable inside the "dist" folder.

### How to run the GUI application

Simply run the executable file.

## Authors

- José Ruiz (joseruiz@keemail.me)

## Contributing

Any help is always welcomed. Just send PR or contact me.

## License

Licensed under GPLv3.
