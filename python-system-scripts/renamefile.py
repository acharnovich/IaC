import os

def replace_spaces_in_filenames(provided_sub_directory):
    """
    This function will traverse a sub directory provided by the user 
    and look for all files with spaces and replace them with underscores.
    
    Parameters:
    provided_sub_directory: The directory the user wants to start at
    example: /home/testuser/Desktop/
    """
    #Check if the provided directory exists
    if not os.path.isdir(provided_sub_directory):
        print(f"The provided directory does not exist: {provided_sub_directory}")
        return
    #traverses the provided directory and all subdirectories
    for dirpath, _, filenames in os.walk(provided_sub_directory):
        print(f"Looking for files in: {dirpath}")
        # for loop, go through all filenames
        for filename in filenames:
            #if filename contains space
            if ' ' in filename:
                #captures value of current file name with full path
                old_path = os.path.join(dirpath, filename)
                #replaces the " "
                new_filename = filename.replace(' ', '_')
                #creates new filepath with filename
                new_path = os.path.join(dirpath, new_filename)
                #executes the rename taking the old path and replacing it with new path
                os.rename(old_path, new_path)
                print(f'Renamed file: {old_path} -> {new_path}')

if __name__ == "__main__":
    provided_sub_directory = input('Provide a directory to start:')
    #calls the function and passes provide_sub_directory
    replace_spaces_in_filenames(provided_sub_directory)
