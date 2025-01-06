# Source_Code_Analysis

# How to run?

# Steps:

Clone the repository
```bash
Project repo: https://github.com/
```

### Step 01: Create a conda environment after opening the repository
```bash
conda create -n sourcecode python=3.11 -y

conda activate sourcecode
```

### Step 02: Install all requirements.
```bash
pip install -r requirements.txt
```
### Create a `.env` file in the root directory and add your GROQ_API_KEY and GOOGLE_API_KEY credentials as follow:

```ini
GROQ_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxx"
GOOGLE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxx"
```

```bash
#Finally run the following command to run application
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- GROQ
- GEMINI (model=gemini-1.5-pro)
- ChromaDB
