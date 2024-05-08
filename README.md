# Code challenge

  ### Criteria for the output file.
  Any user that belongs to a company in the companies file and is active
  needs to get a token top up of the specified amount in the companies top up
  field.

  If the users company email status is true indicate in the output that the
  user was sent an email ( don't actually send any emails).
  However, if the user has an email status of false, don't send the email
  regardless of the company's email status.

  Companies should be ordered by company id.
  Users should be ordered alphabetically by last name.

  Important points
  - There could be bad data
  - The code should be runnable in a command line
  - Code needs to be cloneable from github
  - Code file should be named challenge.rb

### How to install python using brew (for MacOS)
**Step 1**: Install Homebrew (If Not Installed)
• Open the Terminal.
• Install Homebrew, a package manager, by executing the following command:
```
/bin/bash -c "$(curl -fsSL
https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```


**Step 2**: Install Python 3.12
• In the Terminal, run the command brew install python@3.12 to install Python 3.12:
```
brew install python@3.12
```

**Step 3**: Verify Python Installation
• To ensure Python 3.12 is installed correctly, run the following command in the Terminal:
```
python3.12 –version
```

**Step 4**: Set Up Virtual Environments (Optional but Recommended)
• Utilize virtual environments for project isolation.
• Create a virtual environment with the command python3.12 -m venv myenv, replacing
myenv with your chosen environment name.
• Activate the virtual environment by running source myenv/bin/activate.
• To deactivate it later, simply execute deactivate.

### How to run script:
Pull the thrive_challenge from the github and run open terminal in the thrive_challenge folder and run:
```
python challenge.py
```
In few seconds you could see output.txt file in the folder


### How to run tests

To run the unit tests just place this command in terminal:

```
python -m unittest tests.TestChallenge
```

