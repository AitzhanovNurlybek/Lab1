import os

def analyze(given_path):
    if os.path.exists(given_path):
        print("The path exists.")
        filename = os.path.basename(given_path)
        directory = os.path.dirname(given_path)
        print("Filename:", filename)
        print("Directory:", directory)
    else:
        print("The path does not exist.")

given_path = '/Users/Aitzh/OneDrive/Рабочий стол/lab6'

analyze(given_path)