from os import remove, path


class File:
    @staticmethod
    def delete(filename: str):
        remove(filename)

    @staticmethod
    def read_file(filename: str):
        file = open(filename, 'r')
        # return file.readlines()
        # return (line.strip() for line in file.readlines())
        return (line.strip() for line in file.readlines())

    @staticmethod
    def exists(filename: str):
        return path.exists(filename)


print(File.exists('test.txt'))
print(File.read_file('test.txt'))
# print(File.delete('test.txt'))

