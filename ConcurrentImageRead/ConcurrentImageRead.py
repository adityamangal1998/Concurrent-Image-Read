from concurrent.futures.thread import ThreadPoolExecutor
import os
import cv2
import numpy as np
import glob
from functools import partial


class ConcurrentImageReader:
    def __init__(self):
        pass

    @staticmethod
    def __read_image(img_path, channel_type='BGR', grayscale=None, resize=None, normalisation=None):
        img = cv2.imread(img_path)
        if grayscale is not None:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if channel_type == 'RGB':
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if resize is not None:
            img = cv2.resize(img, resize)
        if normalisation is not None:
            img = img / 255.0
        return img

    def read(self, image_list, num_threads=3, channel_type='BGR', root_path=None, grayscale=None, resize=None,
             normalisation=None):
        try:
            if image_list is None:
                raise FileNotFoundError("File Not Found")
            if type(image_list) == str:
                "Single path of Image"
                return self.__read_image(image_list, channel_type=channel_type, grayscale=grayscale, resize=resize,
                                         normalisation=normalisation)

            elif type(image_list) == list or type(image_list) == np.ndarray:
                "Read Images from Image list Concurrently"
                new_image_list = image_list
                if root_path is not None:
                    new_image_list = [os.path.join(root_path, x) for x in image_list]
                calling_function = partial(self.__read_image, channel_type=channel_type, grayscale=grayscale,
                                           resize=resize,
                                           normalisation=normalisation)
                with ThreadPoolExecutor(max_workers=num_threads) as executor:
                    result = list(executor.map(calling_function, new_image_list))
                if type(image_list) == list:
                    return result
                else:
                    return np.array(result, dtype=object)
        except Exception as e:
            print(f"Found Error : {e}")

    def read_dir(self, dir_path, file_type='png', num_threads=3, channel_type='BGR', sub_dir=False, grayscale=None,
                 resize=None,
                 normalisation=None):
        try:
            if type(file_type) == str:
                if file_type == 'all':
                    file_type = '*'
                if sub_dir:
                    image_list = glob.glob(os.path.join(dir_path, f'**/*.{file_type}'), recursive=True)
                else:
                    image_list = glob.glob(os.path.join(dir_path, f'*.{file_type}'))
            elif type(file_type) == list:
                image_list = []
                for ftype in file_type:
                    ftype = ftype.replace(".", "")
                    if sub_dir:
                        image_list = image_list + glob.glob(os.path.join(dir_path, f'**/*.{ftype}'), recursive=True)
                    else:
                        image_list = image_list + glob.glob(os.path.join(dir_path, f'*.{ftype}'))
            return self.read(image_list, num_threads=num_threads, channel_type=channel_type, grayscale=grayscale,
                             resize=resize, normalisation=normalisation)
        except Exception as e:
            print(f"Found Error : {e}")


def read(image_list, num_threads=3, channel_type='BGR', root_path=None, grayscale=None, resize=None,
         normalisation=None):
    """
    Read Image with multi-threading
    :param image_list: List or Numpy array or Single Path of image
    :param num_threads: Integer, Number of Threads
    :param channel_type: 'BGR' or 'RGB', Channel order of Image
    :param root_path: str, Parent path for all files
    :param grayscale: Bool
    :param resize: List or Tuple resize scale in (width,height)
    :param normalisation: Bool, Image array divide by 255
    :return: List or Numpy array depend on input data type
    """
    CIR = ConcurrentImageReader()

    return CIR.read(image_list, num_threads=num_threads, channel_type=channel_type, root_path=root_path,
                    grayscale=grayscale, resize=resize, normalisation=normalisation)


def read_dir(dir_path, file_type='png', num_threads=3, channel_type='BGR', sub_dir=False, grayscale=None, resize=None,
             normalisation=None):
    """
    Read Image Files from Directory with multi-threading
    :param dir_path: str, Path of Image Directory
    :param file_type: 'all' or 'PNG','JPG',...etc or ['JPG','PNG',...]
    :param num_threads: Integer, Number of Threads
    :param channel_type: 'BGR' or 'RGB', Channel order of Image
    :param sub_dir: Bool, Find all Images in all child directory also
    :param grayscale: Bool
    :param resize: List or Tuple resize scale in (width,height)
    :param normalisation: Bool, Image array divide by 255
    :return: List of Image Array
    """
    CIR = ConcurrentImageReader()
    return CIR.read_dir(dir_path, file_type=file_type, num_threads=num_threads, channel_type=channel_type,
                        sub_dir=sub_dir, grayscale=grayscale, resize=resize, normalisation=normalisation)
