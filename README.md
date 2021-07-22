# Path Builder

Path builder is a simple python script, that accepts text from the command line, and prints out the built path (as long as it exists). Using it is extremely simple

# Using Path Builder
Given that you have python installed, all you need to do is run the program from the command line. This can be done by going to the folder in the command line, where the getpath.py file is, and just typing `getpath.py`

Simple.

That's the first step, and that will run the program. To actually use the script, you will have to provide cmd args when you are attempting to run the file.
These arguments can be a series of directory names, or text, which will then be used to build the path.

## Example of Usage
Say I had a series of nested folders such as: 
```cmd
- programs -
    - folder_1
    - bfolder
    - another_folder
        - yet_another_folder
            - target_folder
```
I can get the full path to the target folder by typing ```getpath.py pro ano yet tar```. This example shows that I do not need to type the full names of the directory, just text that the directory name contains.
