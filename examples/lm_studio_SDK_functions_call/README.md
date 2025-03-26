*This repository is for testing function calling on open-source models using the LMStudio SDK.*

#### Run: 
```sh
$ pyhon -m venv .venv
$ .venv\Scripts\activate.bat
$ pip install requirements.txt
# $ python simple_test.py
$ python test2_lmStudio_SDK_function_call.py
```
### Showing Logs:
```sh
$ lms #shows all related commands
$ lms log stream #shows lmStudio server logs
# Note: Please don't forget to run the lmStudio API server.
```

#### Sample of Functions:
```py
def create_file(name: str, content: str):
    """Create a file with the given name and content."""
    dest_path = Path(name)
    if dest_path.exists():
        return "Error: File already exists."
    try:
        dest_path.write_text(content, encoding="utf-8")
    except Exception as exc:
        return "Error: {exc!r}"
    return "File created."
```

Model: **gemma-3-4b-it**

<img src="examples/lm_studio_SDK_functions_call/results.gif" width="600" height="400" />

