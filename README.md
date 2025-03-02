# PythonAgentAI

PythonAgentAI is a project designed to leverage advanced OpenAI models, including `gpt-4o-mini` with a 128k context window, to perform various AI-driven tasks. This project utilizes the `llama-index` library (version 0.12.22) and its experimental extensions to enhance functionality.

## Features

- Integration with OpenAI's `gpt-4o-mini` model, supporting a 128k context window.
- Modular code structure with components like `main.py`, `pdf.py`, `prompts.py`, and `note_engine.py`.
- Utilization of `llama-index` and `llama-index-experimental` libraries for advanced indexing and querying.

## Installation

### Prerequisites

- Python 3.11 installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

## Configuration

1. **Create the `.env` File**

   The project requires a `.env` file for storing environment variables, including the OpenAI API key. You can create it by running:

   ```bash
   cp .env.example .env
   ```

2. **Set Your OpenAI API Key**

   Open the `.env` file in a text editor and configure your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   Replace `your_openai_api_key_here` with your actual API key from OpenAI.

### Setup Instructions

1. **Clone the Repository**

   Open your terminal and run:

   ```bash
   git clone https://github.com/your-username/PythonAgentAI.git
   cd PythonAgentAI
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies. To create one using Python's `venv` module:

   ```bash
   python3.11 -m venv env
   ```

3. **Activate the Virtual Environment**

   - On **Unix or macOS**:

     ```bash
     source env/bin/activate
     ```

   - On **Windows**:

     ```bash
     .\env\Scripts\activate
     ```

4. **Install Dependencies**

   With the virtual environment activated, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

   This will install the following essential packages:

   - `llama-index==0.12.22`
   - `llama-index-experimental==0.5.4`
   - `pypdf==5.3.1`
   - `python-dotenv==1.0.1`
   - `pandas==2.2.3`

## Usage

After setting up the environment and installing the dependencies, you can run the main script:

```bash
python main.py
```


Ensure that you have configured any necessary environment variables or settings required by the script. Refer to the `prompts.py` and `note_engine.py` files for customizable parameters and functionalities.
