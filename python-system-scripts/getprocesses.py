import subprocess

def get_user_process_memory():
    """
    Description: This function will capture the output of the ps aux command as a string.
    It will output all users and the number of associated processes they have.
    As a bonus, I added the total memory consumption in % for each user.
    """
    #Captures the output of ps aux as a string
    ps_output = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE, text=True)
    
    #Split the ps_output into lines
    ps_lines = ps_output.stdout.splitlines()

    #Create dictionaries to count processes and memory usage for each user
    user_process_counts = {}
    user_memory_usage = {}

    #Skip the first line of pslines, and create columns for each line
    for line in ps_lines[1:]:
        #Split each line after every space
        ps_sections = line.split()

        #Extract username from column 1
        user = ps_sections[0]
        #Extract Memory usage from column 4
        memory = float(ps_sections[3])  
        
        #Skips root user
        if user == 'root':
            continue
                
        #Adds up process counts and memory usage for every user
        if user in user_process_counts:
            user_process_counts[user] += 1
            user_memory_usage[user] += memory
        #inializes new users into memory and process dictionaries 
        else:
            user_process_counts[user] = 1
            user_memory_usage[user] = memory

    #For every user in process counts dictionary
    for user in user_process_counts:
        #captures how many processes a user has
        process_count = user_process_counts[user]
        #captures the total memory usage for each user
        total_memory = user_memory_usage[user]
        #prints out the user, number of processes and total memory as a % of system memory
        print(f"{user}: {process_count} processes, {total_memory:.2f} % memory")

if __name__ == "__main__":
    get_user_process_memory()
