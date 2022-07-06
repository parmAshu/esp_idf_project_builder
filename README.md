# ESP IDF PROJECT BUILDER

Esp IDF project builder can be used to easily create a C/C++ project for esp32 SoCs.

## Requirements

Following items must be preinstalled for running project builder and using the created project. The installation steps are platform dependent.

* python3
* cmake
* git
* ninja

Except for the above requirements, no other setup steps are required. The projects created using this project builder contain all the required components - the SDK, the compiler toolchain etc.

## Usage 

You can easily setup an esp-idf project using this script. Here is how to do it :


1. Clone the repository using the below command; you must have git installed on your system. Alternately you may simply download the repository on to your system.

```
git clone https://github.com/parmAshu/esp_idf_project_builder
```

2. Now open a terminal and navigate to the repository. Run the script using the below command; the script will ask you to enter a few details like the directory where you want to create the project and the project name.

```
python3 generate_esp_idf_project.py
```

That's it, you now have a basic esp idf project ready to be used for any kind of application development.

## Common commands

* To setup the environment :
`python3 setup.py`

* To set application target :
`idf.py set-target esp32`

* To configure the project :
`idf.py menuconfig`

* To build the project :
`idf.py build`

* To flash the application :
`idf.py -p PORT -b BAUDRATE flash`