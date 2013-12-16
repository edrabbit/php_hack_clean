import os
import shutil

nastiness = "COPY AND PASTE THE OFFENDING PHP CODE HERE"


dir = os.getcwd()
infected_count = 0
clean_count = 0
total_file_count = 0
for r,d,files in os.walk(dir):
    for file in files:
        if file.endswith(".php"):
            total_file_count += 1
            path = os.path.join(r,file)
            fobj = open(path, 'r')
            lines = fobj.readlines()
            fobj.close()
            if len(lines):
                if nastiness in lines[0]:
                    print("  FOUND NASTINESS in %s" % path)
                    infected_count += 1
                else:
                    clean_count += 1
            else:
                clean_count += 1

print("----------------")
print("Report:")
print("----------------")
print("Clean Files:         %s" % clean_count)
print("Infected Files:      %s" % infected_count)
print("Total Files Checked: %s" % total_file_count)
