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

# Main Script Overview

## Import Statements:

The script imports several pipeline components and the logging module.

## Logging Initialization:

Logging is used to record information about the script's execution. It starts by logging the beginning of the "Data Ingestion" stage.

## Data Ingestion Stage (Stage 01):

- The `IngestDataPipeline` class is instantiated, and its `main` method is called to execute the data ingestion stage.
- Logging records the completion of the "Data Ingestion" stage. `IngestDataPipeline` calls `IngestDataComponent` class
- The `IngestDataComponent` class is a fundamental component designed for the data ingestion stage in a machine learning pipeline. This class facilitates the downloading and extraction of data from a specified source, with a focus on utilizing the Kaggle API for this purpose.

## Base Model Generator Stage (Stage 02):

- The script contains a try-except block to handle exceptions during the execution of the "Base Model Generator" stage (`BaseModelPipeline`). `BaseModelPipeline` calls `BaseModelGeneratorComponent` class
- `BaseModelGeneratorComponent` is a class designed for generating base and actual deep learning models using TensorFlow and Keras. It includes functionalities for loading a pre-trained base model, modifying it to create an actual model with customizable configurations, and saving the models. 
- If successful, it prints messages indicating the start and end of the stage.
- Any exceptions raised during this stage are re-raised.

## Model Training Stage (Stage 03):

- Another try-except block is used to handle exceptions during the execution of the "Model Training" stage (`ModelTrainingPipeline`). `ModelTrainingPipeline` calls `TrainingComponent` class
- `TrainingComponent` is a class designed to streamline the process of training and evaluating a deep learning model using TensorFlow and Keras. It includes functionalities for loading a pre-trained model, performing a train-test split, and training the model with specified callbacks. 
- If successful, it prints messages indicating the start and end of the stage.
- Any exceptions raised during this stage are re-raised.

## Model Evaluation Stage (Stage 04):

- Another try-except block is used to handle exceptions during the execution of the "Model Evaluation" stage (`ModelEvaluationPipeline`). `ModelEvaluationPipeline` calls `ModelEvaluation`
- `ModelEvaluation` is a class designed for evaluating a trained deep learning model using TensorFlow and Keras. It includes functionalities for loading a trained model, preparing a validation data generator, and conducting
    evaluation. The evaluation results are then saved as a JSON file.
- If successful, it prints messages indicating the start and end of the stage.
- Any exceptions raised during this stage are re-raised.

## How to train a convolutional model
In the config.yaml file, you have the flexibility to specify the name of the dataset that you wish to download. The dataset_name parameter plays a crucial role in defining the target dataset for your machine learning pipeline.</br>

Configuration Example: </br>
In the config.yaml file, you can set the dataset_name parameter to the desired dataset name. For instance:</br>

Example config.yaml
```python
data_ingest:
  dataset_name: "prasunroy/natural-images"
  data_folder: "path/to/data/folder"
```
In this example, the dataset_name is set to "prasunroy/natural-images." You can replace this value with the specific name of the dataset you want to work with. </br>
In the `params.yaml` file, you have the flexibility to customize and set various parameters that influence the behavior of your machine learning pipeline. Below are the key parameters along with their descriptions:

#### 1. `EPOCHS`: 
   - **Description:** The number of training epochs, representing the number of times the model will iterate over the entire training dataset.
   - **Example:** `15`

#### 2. `CLASSES`:
   - **Description:** The number of classes or categories in the dataset. This value is dataset-specific and depends on the nature of the classification task.
   - **Example:** `8`

#### 3. `IMAGE_SIZE`:
   - **Description:** The dimensions of input images expected by the model. It is specified as a list with three elements representing width, height, and the number of channels (e.g., `[224, 224, 3]`).
   - **Example:** `[224, 224, 3]`

#### 4. `TEST_SIZE`:
   - **Description:** The proportion of the dataset to include in the test split. It is a value between 0 and 1.
   - **Example:** `0.2`

#### 5. `BATCH_SIZE`:
   - **Description:** The number of samples in each batch during training. It impacts the speed and memory usage during training.
   - **Example:** `16`

#### 6. `LR`:
   - **Description:** The learning rate, which controls the step size during optimization. It influences the convergence and training speed.
   - **Example:** `0.005`

#### 7. `AUG`:
   - **Description:** A boolean indicating whether data augmentation is enabled (`True`) or disabled (`False`). Data augmentation involves applying random transformations to training data, enhancing model generalization.
   - **Example:** `True`

#### 8. `MODEL`:
   - **Description:** An identifier or version number for the model. It helps track and distinguish different versions of the trained models.
   - **Example:** `2`
