import os
def get_filename(dirname,subfixs):

    result = []#鎵�鏈夌殑鏂囦欢

    for maindir, subdir, file_name_list in os.walk(dirname):

        for filename in file_name_list:
            if subfixs in filename:
                apath = os.path.join(maindir+'/'+filename)#鍚堝苟鎴愪竴涓畬鏁磋矾寰�
                result.append(apath)

    return result

print(get_filename("E:/hellopython/object_detection/test_images",'.jpg'))