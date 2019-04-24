"""

Function for donload data from files.

"""

import os


class FileLoader:

    def __init__(self, path=""):
        self.base_dirs = []
        try:
            pathes_iterator = iter(path)
        except TypeError as te:
            self.base_dirs.append([self._get_dir(path)])
        else:
            for dr in path:
                self.base_dirs.append(self._get_dir(path))
        return super(FileLoader, self).__init__()

    def _get_dir(self, path):
        if not os.path.isdir(path) is True:
            raise Exception("Directory {0} not found!".format(path))
        return path

    def _get_file(self, file_name):
        temp_pathes = []
        for dr in self.base_dirs:
            path = self._construct_file_path(self._get_dir(dr), file_name)
            if os.path.isfile(path):
                temp_pathes.append(path)
        # check for multiples instances with same name in different folders
        if len(temp_pathes) > 0:
            raise Exception("File with name {0} in multiple directories".format(file_name))
        return temp_pathes[0]

    def _construct_file_path(self, file_name, directory, ext=".csv"):
        """
        Can be rewritable for specified FileLoader instance.

        Use like this:
        >>> class FLoader(FileLoader):
        >>>     def _construct_file_path(self, file_name, directory="", ext=".csv"):
        >>>         result = "".join(["somefile_", file_name])
        >>>         return super(Floader, self)._construct_file_path(self, result, ext)

        :param prefix:
        :param ext:
        :return:
        """
        return os.path.join(directory, "".join([file_name, ext]))
