### How to Use the Script

#### 1.0 Cloning the Remote Repository

Cloning a repository from GitHub is a fundamental step when working with version control systems like Git. GitHub is a web-based platform that hosts millions of repositories, and cloning allows you to create a local copy of a repository on your computer. This is particularly useful for collaborative development, contributing to open-source projects, or simply managing your own projects efficiently.

Here's a step-by-step guide on how to clone a GitHub repository:

Install Git:
Before you can clone a repository, ensure that Git is installed on your machine. You can download and install Git from the official website: Git Downloads

Create a GitHub Account:
If you don't have a GitHub account, you'll need to create one. Go to GitHub and sign up for a new account.

Find the Repository:
Go to the GitHub website and navigate to the repository you want to clone. You can do this by searching for the repository in the GitHub search bar or by visiting the repository's URL.

Clone the Repository:
On the repository's main page, click on the "Code" button. This will reveal a URL that you can use to clone the repository. Ensure that you have selected the "HTTPS" option if you're using HTTPS.

For HTTPS:

```python
git clone https://github.com/harihara-rajan/Natural_Image_Classification.git
```
#### 2.0 Creating a New Environment
Creating an environment is a common practice in software development to manage dependencies, isolate projects, and ensure consistent and reproducible development and deployment environments. Here are some key reasons why creating an environment is essential:

Creating an environment is a common practice in software development to manage dependencies, isolate projects, and ensure consistent and reproducible development and deployment environments. Here are some key reasons why creating an environment is essential:

1. **Dependency Management:**

Environments help manage dependencies such as libraries, packages, and software versions required for a specific project. Conflicts between different projects with different dependency requirements can be avoided by encapsulating them within separate environments.

2 **Isolation:**

Environments provide isolation between projects. This isolation ensures that changes made for one project do not impact the functionality or stability of other projects. It helps avoid conflicts and unintended consequences.

```python
conda create --name  EnvironmentName python=3.11
conda activate EnvironmentName
```
#### 3.0 Installing dependencies 

The required libraries for this project are specified in the requirements.txt file. To install these dependencies, use the following pip command in your terminal or command prompt:

```python
pip install -r requirements.txt
```
This command reads the requirements.txt file and installs the specified libraries and their corresponding versions. Ensure that you have Python and pip installed on your system before running this command.