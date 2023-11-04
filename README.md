# END to End LLM and LangChain Project

<img src='doc_file/openAI.png' width='150'><img src='https://huggingface.co/' width='150'><img src='doc_file/langchain.jpg' width='150'><img src='doc_file/Streamlit.png' width='150'>

### Step1: Create a virtual environment and activate the venv

- create a venv with the command below:

```
conda create -p venv python==3.9 -y
```

- activate the environment using the command below:

```
conda activate venv\
```

### Step2: create a `requirements.txt` file and install it

- write the libraries in this file that will be needed and can be installed altogether

- In our case, I will write
```
langchain
openai
huggingface_hub
python-dotenv
streamlit
```
   as of now and install it using the below command (don't forget to save the file)

```
pip install -r requirements.txt
```

- After this installation, we will be required to install `ipykernel` to run our Jupyter notebook in this venv(separately installing this because we are not going to install this in the deployment environment)

```
pip install ipykernel
```

- Create a file `.env` where my Open API key can be written and we can use it by using `load_environ` variable function
whenever it will be required.


## Step3: Create your own OpenAPI key for OpenAPI and Huggingface models

- go to the page `https://platform.openai.com/login`
- login or signup with your Contact and Email_ID
- Go to API ![Alt text](doc_file/SelectAPI.png)

- Go to your profile and select `view API key` from drop-down
- click on `create new secret key` and name it or not, copy the key, and save it somewhere. So that can be found next time when required.
![Alt text](doc_file/create_key.png)

### Create Hugging face API(access tokens)

- Go to `hugging face` website
- create an account and log in or signup
- verify email first and then go to `settings` and `access tokens`
- Create a new token and copy it.

## Step4: Experiments 
- Create a python notebook file as `langchain.ipynb`, this is basically our notebook where we test our code and will be doing some experiments with both the LLM libraries.
-  Here I have covered some concepts:
     - Response from OpenAI
     - Response from huggingface_hub
     - Prompt Templates and LLM chains
     - Correct way of calling prompt templates
     - Combining Multiple Chains using simple sequential chain
     - Sequential chain
     - Chatmodels with ChatOpenAI
     - Prompt Template + LLM + Output Parsers

## APP DEMO
![Alt text](doc_file/app_run.gif)
