import os
def get_filename(dirname):

    result = []#所有的文件

    for maindir, subdir, file_name_list in os.walk(dirname):

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#合并成一个完整路径
            result.append(apath)

    return result

# print(get_filename("D:\Liang_Develop"))