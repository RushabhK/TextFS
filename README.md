# TextFS

TextFS is an application which can store all the metadata and the actual data of the files inside a single text file.

## Features

  - create new files. 
  - write and copy contents into newly created files.
  - list all files. 
  - print contents of internal files. 
  - delete existing files.


## Installation

```sh
$ python setup.py
```

## Steps to run
```sh
$ python main.py
```

## How to use 

##### 1. Create file/files:
**Command:** touch filename

```sh
> touch file1 file2 file3 ..
```

##### 2. Write to a file:
**Command:** write filename

```sh
> write filename
#Enter contents of the file
#Enter save
```



##### 3. Delete a file:
**Command:** rm filename

```sh
> rm filename
```

##### 4. Print contents of a file:
**Command:** cat filename

```sh
> cat filename
```

##### 5. List all files:
**Command:** ls 

```sh
> ls
```

##### 6. Exit the program:
**Command:** exit 

```sh
> exit
```