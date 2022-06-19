from concurrent.futures.thread import ThreadPoolExecutor
import os
import cv2
import numpy as np
import glob


class ConcurrentImageReader:
    def __init__(self):
        pass

    @staticmethod
    def _read_image(img_path):
        img = cv2.imread(img_path)
        return img

    @staticmethod
    def _read_image_rgb(img_path):
        img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB)
        return img

    def read(self, image_list, num_threads=3, channel_type='BGR'):
        try:
            if image_list is None:
                raise FileNotFoundError("File Not Found")
            if type(image_list) == str:
                "Direct Single path of Image"
                if channel_type == 'BGR':
                    return self._read_image(image_list)
                elif channel_type == 'RGB':
                    return self._read_image_rgb(image_list)
            elif type(image_list) == list or type(image_list) == np.ndarray:
                "Read Images from Image list Concurrently"
                if channel_type == 'BGR':
                    calling_function = self._read_image
                elif channel_type == 'RGB':
                    calling_function = self._read_image_rgb
                with ThreadPoolExecutor(max_workers=num_threads) as executor:
                    result = list(executor.map(calling_function, image_list))
                if type(image_list) == list:
                    return result
                else:
                    return np.array(result, dtype=object)
        except Exception as e:
            print(f"Found Error : {e}")

    def read_dir(self, dir_path, file_type='png', num_threads=3, channel_type='BGR', sub_dir=False):
        try:
            if sub_dir:
                image_list = glob.glob(os.path.join(dir_path, f'**/*.{file_type}'))
            else:
                image_list = glob.glob(os.path.join(dir_path, f'*.{file_type}'))
            return self.read(image_list, num_threads=num_threads, channel_type=channel_type)
        except Exception as e:
            print(f"Found Error : {e}")


def read(image_list, num_threads=3, channel_type='BGR'):
    """
    Read Image with multi-threading
    :param image_list:
    :param num_threads:
    :param channel_type:
    :return:
    """
    CIR = ConcurrentImageReader()
    return CIR.read(image_list, num_threads=num_threads, channel_type=channel_type)


def read_dir(dir_path, file_type='png', num_threads=3, channel_type='BGR', sub_dir=False):
    """
    Read Image with multi-threading
    :param file_type:
    :param dir_path:
    :param num_threads:
    :param channel_type:
    :param sub_dir:
    :return:
    """
    CIR = ConcurrentImageReader()
    return CIR.read_dir(dir_path, file_type=file_type, num_threads=num_threads, channel_type=channel_type,
                        sub_dir=sub_dir)
