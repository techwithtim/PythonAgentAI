# PythonAgentAI

The **PythonAgentAI** project aims to leverage advanced OpenAI models (including `gpt-4o-mini` with a 128k context window) to perform a variety of AI-powered tasks. This project integrates [**Scrapeless**](https://www.scrapeless.com/en?utm_source=github&utm_medium=readme&utm_campaign=twt) for [Google Maps](https://www.scrapeless.com/en/product/deep-serp-api?utm_source=github&utm_medium=readme&utm_campaign=twt) and the **llama-index** library (version 0.12.22) along with its experimental extensions to enable large language models to provide real-time responses.

## Features

- Integration with OpenAI’s `gpt-4o-mini` model, supporting a 128k context window.
- Modular code structure including components like `main.py`, `pdf`.`py`, `prompts.py`, and `note_engine.py`.
- Advanced indexing and querying via `llama-index` and `llama-index-experimental` libraries.

## Installation

### Prerequisites

- Python 3.11 must be installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

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

- **Log into [Scrapeless](https://app.scrapeless.com/passport/login?utm_source=github&utm_medium=readme&utm_campaign=twt) and obtain your API token.**

![Get the Scrapeless API key](https://assets.scrapeless.com/prod/posts/naver-product/77c0cef86a29013173eb41a34f42d3f4.png)

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

2. **Input the provided prompts to receive results**. After a short wait, you’ll see output similar to the images below:

- **Find the highest rated coffee shop within 0.5km**

![Result of the highest rated coffee shop within 0.5km](https://assets.scrapeless.com/prod/posts/deep-serp-api-online/4ea1b12e422967bccd0db82282cb0270.png)
 
- **Find the closest coffee shop to the target location**

![Result of the closest coffee shop to the location](https://assets.scrapeless.com/prod/posts/deep-serp-api-online/d7e32f4d01913dbd7b76e15983ce46e2.png)
