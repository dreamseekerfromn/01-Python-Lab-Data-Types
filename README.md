# 01-Python-Lab-Data-Types
# Python Data Types Lab

## Objective

This lab is designed to challenge your understanding of Python's basic data types, including numbers, booleans, operators, and strings. By completing the tasks in this lab, you will solidify your knowledge of these concepts and improve your problem-solving skills. The lab is divided into four sections, each in a separate Python file, with a corresponding test suite to verify your solutions.

## Lab Structure

- **`numbers.py`**: Focuses on arithmetic operations, number types, and error handling.
- **`booleans.py`**: Deals with boolean expressions, logical operations, and type conversion.
- **`strings.py`**: Involves string manipulation, formatting, and validation.
- **`mixed_operations.py`**: Combines different data types and operations for more advanced challenges.

## Prerequisites

Before starting the lab, ensure you have Python installed on your machine. If Python is not installed, follow the instructions below.

## Installing Python


### Mac OS

1. Go to the [Python Releases for Mac OS X page](https://www.python.org/downloads/) and download the latest stable release macOS 64-bit/32-bit installer.

2. After the download is complete, run the installer and click through the setup steps leaving all the pre-selected installation defaults.

3. Once complete, we can check that Python was installed correctly by opening a Terminal and entering the command python3 --version. The latest Python 3.7 version number should print to the Terminal.

4. Execute open ~/.bash_profile from a Terminal (if the file was not found, then run touch ~/.bash_profile first).

5. Copy and paste alias python="python3" into the now open .bash_profile file and save.

6. While we’re at it, go ahead and copy and paste alias pip="pip3" into the file as well in order to create an alias for the Python 3 pip package manager.

7. Finally, restart the Terminal and run python --version. We should see the exact same output as running python3 --version.

## Installing Jupyter Notebook

Now that we have a Python distribution installed and were able to run some Python code, let’s install the Jupyter Notebook package. Jupyter Notebook is an open-source web application that allows us to create and share documents that contain live code, equations, visualizations and narrative text. This is a fantastic way to both learn and share Python code and the installation is made easier by our package installer!

Follow the below instructions to install the Jupyter Notebook package using the pip Python package manager.

1. Run pip install jupyter to download and install the Jupyter Notebook package.

2. Once complete, we can check that Jupyter Notebook was successfully installed by running jupyter notebook from a Terminal (Mac) / Command Prompt (Windows). This will startup the Jupyter Notebook server, print out some information about the notebook server in the console, and open up a new browser tab at http://localhost:8888.

## Running the Test Suite
Once you’ve completed the tasks, you can run the provided test suite to verify your solutions.

### Install unittest (Optional)
unittest is part of Python's standard library, so no additional installation is necessary. However, if you prefer using pytest for running the tests, you can install it via pip:

`pip install pytest`

### Run Tests with unittest
To run the tests using unittest, simply execute the following command:

python test_lab.py

### Run Tests with pytest
If you prefer pytest, run the tests using:

pytest test_lab.py


## Troubleshooting
If you encounter issues running the tests or completing the tasks, consider the following:

Double-check your Python installation.
Ensure that all functions in the lab files are correctly implemented and return the expected outputs.
Review error messages carefully—they often provide clues about what went wrong.
If you continue to have trouble, seek help from your instructor or peers.
