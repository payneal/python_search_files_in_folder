from  os import walk

class Check_Folder:
    def __init__(self):
        pass

    def check_if_list_in_files(self, check_list, dir_location):
        file_names = self.__get_files_in_directory(dir_location)
        return self.__cycle_through_files_found(
                file_names, check_list, dir_location)

    # private
    def __get_files_in_directory(self, directory_loc):
        file_names = []
        for (dirpath, dirnames, filenames) in walk(directory_loc):
            file_names.extend(filenames)
            break
        return file_names

    def __check_file_for_string(self, file_location, check_for_str):
        with open(file_location) as myFile:
            if check_for_str in myFile.read():
                return True
            return False
    
    def __cycle_through_files_found(self, file_names, check_list, dir_location):
        the_check = {}
        for file_name in file_names:
            file_location = "{}/{}".format(dir_location, file_name)
            the_check = self.__cycle_through_check_list(
                check_list, the_check, file_location)
        return the_check

    def __cycle_through_check_list(self, check_list, the_check, file_location):
        for name in check_list:
            self.__create_key_if_does_not_exist(name, the_check)
            self.__add_strings_presence_in_file(file_location, name, the_check)
        return the_check

    def __create_key_if_does_not_exist(self, name, the_check):
        if name not in the_check.keys():
            the_check[name] = { "files": [] }
    
    def __add_strings_presence_in_file(self, file_location, name, the_check):
        if self.__check_file_for_string(file_location, name):
            the_check[name]['files'].append(file_location)
    
