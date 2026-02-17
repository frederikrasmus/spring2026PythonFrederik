# Python´s OS module
Python's `os` module provides a way to use operating system dependent functionality. It includes a wide range of functions to interact with the file system, manage paths, and access environment variables, among other capabilities. 

### Using Python's `os` Module

1. **Import the Module**: Before you can use any functions in the `os` module, you need to import it into your Python script.
   ```python
   import os
   ```

2. **Accessing Functions**: After importing, you can call various functions using `os.function_name()`. For example, `os.getcwd()` returns the current working directory.

3. **Handling File Paths**: The `os` module is particularly useful for path manipulation (like joining or splitting paths) which is done in a way that's independent of the operating system.

4. **Environment Variables**: It provides a portable way of using operating system dependent functionality like reading or setting environment variables.

5. **File and Directory Operations**: You can create, delete, move, or rename files and directories.

### Some Useful Methods in the `os` Module

1. **`os.getcwd()`**: Returns the current working directory.
2. **`os.chdir(path)`**: Changes the current working directory to the specified path.
3. **`os.listdir(path='.')`**: Returns a list of the names of the entries in the directory given by path.
4. **`os.mkdir(path, mode=0o777)`**: Creates a directory named path with the specified mode.
5. **`os.makedirs(path, mode=0o777, exist_ok=False)`**: Recursive directory creation function.
6. **`os.rmdir(path)`**: Removes (deletes) the directory path.
7. **`os.remove(path)`**: Removes (deletes) a file path.
8. **`os.rename(src, dst)`**: Renames the file or directory from src to dst.
9. **`os.path.join(path, *paths)`**: Joins one or more path components intelligently.
10. **`os.path.split(path)`**: Splits the path into a pair (head, tail) where tail is the last pathname component.
11. **`os.path.exists(path)`**: Returns True if path refers to an existing path.
12. **`os.path.isfile(path)`**: Returns True if path is an existing regular file.
13. **`os.path.isdir(path)`**: Returns True if path is an existing directory.
14. **`os.environ`**: A mapping object representing the string environment.
15. **`os.walk(top, topdown=True, onerror=None, followlinks=False)`**: Generates the file names in a directory tree by walking the tree either top-down or bottom-up.

For more detailed information and additional functions [Python `os` module documentation](https://docs.python.org/3/library/os.html).
