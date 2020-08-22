import os

files = os.listdir("captions")

with open("all_text.txt", "w") as main_doc:

    index = 0
    for file_name in files:
        
        main_doc.writelines(f"index: {index}" + "\n")
        text = open("captions/" + file_name, "r").readlines()
        main_doc.writelines(line for line in text)
        main_doc.writelines('\n' * 3)
        index += 1

