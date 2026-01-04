# Create a project environment for the Flask tutorial
1. Create a folder.

2. In VS Code, open the Command Palette (View > Command Palette or (`Ctrl+Shift+P`)). Then select the Python: Create Environment command to create a virtual environment in your workspace. Select `venv` and then the Python environment you want to use to create it.

3. run Terminal: Create New Terminal (`Ctrl+Shift+(백틱)`)) from the Command Palette, which creates a terminal and automatically activates the virtual environment by running its activation script.

4. Install Flask
```
python -m pip install flask

# pip 업그레이드
python -m pip install --upgrade pip
pip install --upgrade flask
```

5. Run 
```
python -m flask run
```