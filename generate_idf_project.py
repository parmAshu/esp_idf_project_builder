"""
This script creates a IDF project
"""
import os, shutil, time, json, requests, platform, traceback

IDF_LINK = "https://github.com/espressif/esp-idf.git"

SYSTEM_OS = platform.system()

ACCEPTED_AFFIRMATIVE_RESPONSES = [ "Y", "y", "yes" ]

def affirmative( resp ):
    """
    This function determines if the passed parameter is a valid affirmative response

    Args:
        resp ( str ): response string from user

    Returns:
        Bool : If resp is affirmative response
    """
    if resp in ACCEPTED_AFFIRMATIVE_RESPONSES:
        return True
    else:
        return False

try:
        
    print( "WELCOME TO PICO APP BUILDER..." )

    # Get the current working directory
    CURRENT_DIRECTORY = os.getcwd()

    # Get the location for project
    while True:
        print()
        print("Please provide the working directory: ")
        WORKING_DIRECTORY = input()
        if affirmative( input( "Are you sure ? (Y/N) : " ) ):
            break
    if os.path.exists( WORKING_DIRECTORY ) == False:
        print( "Invalid working directory!" )
        raise Exception

    # Get the project name
    project_name = ""
    while True:
        project_name = input( "What do you want to call your project ? " )
        if affirmative( input( "Are you sure ? (Y/N) : " ) ):
            break

    # Creating the project directory and navigating to it
    print( "Creating project directory : " )
    print( project_name )
    project_dir = os.path.join( WORKING_DIRECTORY , project_name )
    os.mkdir( project_dir )
    os.chdir( project_dir )
    os.mkdir( "tools" )
    os.mkdir( "main" )

    # Parsing the guide
    guide_string = ""
    with open( os.path.join( CURRENT_DIRECTORY, "template", "guide.json" ) ) as guide_file:
        guide_string = guide_file.read()
    guide_obj = json.loads( guide_string )

    # Cloning the IDF in the project directory
    print()
    print( "Cloning the IDF..." )
    os.system( "git clone --recursive " + IDF_LINK )

    # Set the tools installation path
    os.environ["IDF_TOOLS_PATH"] = os.path.join( project_dir, "tools" )

    print()
    print( "Installing tools..." )
    # Install the tools
    os.chdir( os.path.join( project_dir, "esp-idf" ) )
    if "Win" in SYSTEM_OS:
        os.system( ".\install.bat" )
    else:
        os.system( "./install.sh all" )
    os.chdir( WORKING_DIRECTORY )

    print()
    print( "Creating project files..." )
    # Create the project files
    for obj in guide_obj[ "files" ]:
        source_file_name = obj[ "template_name" ]
        dest_file_name = obj[ "dest_name" ]
        source_file = open( os.path.join( CURRENT_DIRECTORY, "template", source_file_name ) )
        dest_file = open( os.path.join( project_dir, dest_file_name ), "w" )
        
        source_string = source_file.read()
        for edit in obj["edit"]:
            edit_value = ""
            if edit[1] == "project_name":
                edit_value = project_name
            source_string = source_string.replace( edit[0], edit_value )

        dest_file.write( source_string )
        source_file.close()
        dest_file.close()

except Exception as e:
    traceback.print_exc()
finally:
    print( "Bye!!" )