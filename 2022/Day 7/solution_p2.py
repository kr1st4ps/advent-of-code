dir_size = {"/":0}
cwd = ["/"]
last_line = None
total_size = 0

with open('input.txt', 'r') as file:
    while True:
        line = file.readline().strip()

        if not line:
            break
        
        #   This line is a command
        if line[0] == "$":
            command = line.split()

            #   cd
            if len(command) == 3:

                #   Goes back to home dir
                if command[2] == "/":
                    cwd = ["/"]

                #   Goes to previous dir
                elif command[2] == "..":
                    cwd.pop()

                #   Goes to next dir
                else:
                    cwd.append(command[2])
            
            #   ls
            else:

                #   Reads every line ls returns
                while True:
                    last_line = file.tell()
                    line = file.readline().strip()

                    #   Break if there is no line or next line is another command
                    if not line or line[0] == "$":
                        break

                    size, name = line.split()

                    #   If ls returns a dir, start counting its size
                    if size == "dir":
                        path = "/".join(cwd) + "/" + name
                        if path not in dir_size:
                            dir_size[path] = 0
                        continue
                    
                    #   If ls returns file, calculate size of all parent dirs this file exists in
                    temp_cwd = cwd.copy()
                    for i in range(len(cwd)):
                        path = "/".join(temp_cwd)
                        temp_cwd.pop()
                        dir_size[path] += int(size)
             
                file.seek(last_line)

#   Keeps only dirs that are of needed size
temp_dir_size = dir_size.copy()
for dir, size in dir_size.items():
    if size < 8381165:
        temp_dir_size.pop(dir)

#   Gets the dir that is closest to needed amount
lowest = min(temp_dir_size, key=temp_dir_size.get)
print(temp_dir_size[lowest])