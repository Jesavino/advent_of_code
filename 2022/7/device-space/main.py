class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.sub_directories = []
        self.files = []

    def add_subdirectory(self, sub):
        self.sub_directories.append(sub)

    def add_file(self, file):
        self.files.append(file)

    def get_sub_dir(self, name):
        for dir in self.sub_directories:
            if dir.name == name:
                return dir

    def size(self):
        size = 0
        for dir in self.sub_directories:
            size += dir.size()
        for file in self.files:
            size += file.size
        return size


DIR_LIST = []


def main():

    root = Directory(name="/")
    current_directory = root
    with open("input.txt") as input:
        for line in input.read().split("\n"):
            cmd = line.split()
            if cmd[1] == "cd":
                if cmd[2] == "..":
                    current_directory = current_directory.parent
                else:
                    current_directory = current_directory.get_sub_dir(cmd[2])
            elif cmd[0] == "dir":
                sub_dir = Directory(cmd[1], current_directory)
                DIR_LIST.append(sub_dir)
                current_directory.add_subdirectory(sub_dir)
            elif cmd[1] == "ls":
                pass
            else:  # should just be the file size case
                file = File(cmd[1], int(cmd[0]))
                current_directory.add_file(file)

        sum = 0
        for dir in DIR_LIST:
            size = dir.size()
            if size < 100000:
                sum += size

        # sum of directories under 100000 in size
        print(sum)

        used_space = root.size()
        unused_space = 70000000 - used_space
        space_required = 30000000 - unused_space
        closest = 1000000000000000
        for dir in DIR_LIST:
            size = dir.size()
            if size >= space_required:
                if size < closest:
                    closest = size

        print(closest)


if __name__ == "__main__":
    main()
