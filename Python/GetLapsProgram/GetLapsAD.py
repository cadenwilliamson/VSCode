import subprocess


def GetLapsAD(script_path, user_input):
    try:
        # Use 'powershell.exe' to run the script
        script_result = subprocess.run(['powershell.exe', '-File', script_path], capture_output=True, text=True, check=True)

        # print("PowerShell script output:")

        print(script_result.stdout)
    
    except subprocess.CalledProcessError as error:
        print(f"Error running PowerShell script: {error}")



if __name__ == "__main__":
    script_path = r'C:\\Users\\willcj2\\Documents\\VSCode\\Python\\GetLapsProgram\\myscript.ps1'  # Replace with your actual script path
    user_input = input("Please input Computer Name: ")
    
    
    print(user_input)
    GetLapsAD(script_path, user_input)