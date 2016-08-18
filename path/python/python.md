# Python Learning Path

## Basic

### Set up a Python development environment

This will get you up and running with Python 3 on a development laptop. You should be relatively comfortable with running commands and changing directories, setting permissions for files and folders from the command line.

#### Tasks

1. Launch the terminal and change directory to you home directory.
2. Create a work directory if one doesn't already exist.
3. Change directory to your work directory and launch the Atom editor: `atom .`
4. Create `hello.py` and write a program to write "Hello, World!" to output.

  ```python
  #!/usr/bin/env python3

  print("Hello, World!")
  ```

5. Back in the terminal, run you new script in Python 3.

  ```sh
  ~/exercises $ python3 hello.py
  Hello, World!
  ```

6. Make the script executable and run it directly from the command line.

  ```sh
  ~/exercises $ chmod +x hello.py
  ~/exercises $ ./hello.py
  Hello, World!
  ```

#### Example

- [`hello.py`](basic/hello.py)

#### References

- [Python](https://www.python.org)
- [Atom editor](https://atom.io)
- ["Hello World!" program](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program)
- [Shebang (Unix)](https://en.wikipedia.org/wiki/Shebang_(Unix))
- [`print()`](https://docs.python.org/3.5/library/functions.html#print)

### Python Basic Data Types

See this python.org tutorial for an introduction to basic data types: [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html)

Stop when you reach section 3.2, "First Steps Towards Programming".

#### Examples
- [`numbers.py`](basic/numbers.py)
- [`variables.py`](basic/variables.py)
- [`strings.py`](basic/strings.py)

### First Steps Towards Programming

Generate the first few numbers of the Fibonacci series by following [section 3.2](https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming) of the python.org tutorial.

#### Example
- [`fibo.py`](basic/fibo.py)
