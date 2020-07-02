## Notes

- Developed in 1991
- **Advantages:** quick to learn; involves less code than other languages; readable syntax (indentation not curly braces); used by every major tech company; tons of open-source libraries.
- Anaconda distribution - includes Python + other useful libraries like Jupyter.
- Can be written in **text editors** (ex. VS Code, Sublime, Atom), **full IDEs** (larger; designed for Python; more functionality - ex. PyCharm, Spyder), or **notebooks** (great for learning; see input & output together; in-line notes, visualizations, etc.; special file formats, i.e. not .py - ex. Jupyter Notebook).
- To run a python script in the command line, $ <code>python [filename]</code>
- Jupyter does NOT require internet (everything happens locally)
- After opening 'Anaconda Navigator' > New (top right) > Notebook
- Shift + Enter - run a cell
- B (add cell below); A (add cell above); D, D (delete a cell)
- Kernel > Restart - will reset all variables

#### Virtual Environments (using the built-in venv module)
- Why? So we can use different versions of modules across different projects
○ For example, a project in Django 1 may break when we upgrade to Django 2
- How?
  ``` curl
    python3 -m venv [env_name]
    source [env_name]/bin/activate
    which python (will confirm which version is being used)
    *To deactivate:* deactivate
    *To delete:* rm -rf [env-name]
  ```

- **Common practice**: run these commands WITHIN your project folder and name the virtual environment 'venv'
- DO NOT put project files within the virtual environment directory
- DO NOT commit your virtual environment to source control
<code>pip list</code> will show your downloaded modules