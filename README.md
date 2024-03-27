# Docker Python Text Analysis

Welcome to the Docker Python Text Analysis project repository! This project focuses on processing text files using Python within a Docker container. You'll explore tasks such as word counting, identifying top words, and generating an output file with the results.

## Project Structure

This repository includes the following main components:

- **Python Script (`cloud_script.py`):** Contains functions to read text files, count words, find top words, and generate an output file with the results.
- **Dockerfile:** Contains instructions to build a Docker image with Python installed and set up to run the `cloud_script.py`.
- **Sample Text Files (`IF.txt`, `Limerick-1.txt`):** Text files used by the script for processing.

## Usage

To run the script, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/your-repo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo
    ```

3. Build the Docker image:

    ```bash
    docker build -t cloud-script .
    ```

4. Run the Docker container:

    ```bash
    docker run --rm cloud-script
    ```

## Tasks Overview

The project performs the following tasks:

1. **Word Count:** Count the total number of words in each text file.
2. **Top Words in IF.txt:** Identify the top 3 words in the `IF.txt` file.
3. **Output Generation:** Generate an output file (`result.txt`) with the word count information, top words, total word count, and IP address.



