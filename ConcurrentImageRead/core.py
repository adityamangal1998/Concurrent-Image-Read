from concurrent.futures.thread import ThreadPoolExecutor
import os
import cv2
import numpy as np
import glob
from functools import partial
import time


class ConcurrentImageReader:
    def __init__(self):
        pass

    @staticmethod
    def __image_process(img, channel_type='BGR', grayscale=None, resize=None, normalisation=None):
        try:
            if grayscale is not None:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            if channel_type == 'RGB':
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            if resize is not None:
                img = cv2.resize(img, resize)
            if normalisation is not None:
                img = img / 255.0
        except Exception as e:
            print(f"Found Error : {e}")
            return None
        return img

    @staticmethod
    def __read_image(img_path, channel_type='BGR', grayscale=None, resize=None, normalisation=None):
        try:
            img = cv2.imread(img_path)
            img = ConcurrentImageReader.__image_process(img, channel_type=channel_type, grayscale=grayscale, resize=resize,
                                                        normalisation=normalisation)
        except:
            None
        return img

    @staticmethod
    def __read_frames(frame_source, fps=None, end_time_sec=None, channel_type='BGR', grayscale=None, resize=None,
                      normalisation=None):
        if fps is None:
            frame_rate = 0
        else:
            frame_rate = fps
        if end_time_sec is None:
            end_time = 0
        else:
            end_time = end_time_sec
        frame_list = []
        frame_time = time.time()
        start_time = time.time()
        while True:
            ret, frame = frame_source.read()
            if not ret:
                break
            if time.time() - frame_time > frame_rate:
                frame_time = time.time()
                frame = ConcurrentImageReader.__image_process(frame, channel_type=channel_type, grayscale=grayscale,
                                                              resize=resize, normalisation=normalisation)

                frame_list.append(frame)
            if (time.time() - start_time > end_time) and end_time_sec is not None:
                break
        frame_source.release()
        return frame_list

    @staticmethod
    def __read_camera(source, fps=None, end_time_sec=None, channel_type='BGR', grayscale=None, resize=None,
                      normalisation=None):
        try:
            frame_source = cv2.VideoCapture(source, cv2.CAP_DSHOW)
            frame_list = ConcurrentImageReader.__read_frames(frame_source, fps=fps, end_time_sec=end_time_sec,
                                                             channel_type=channel_type,
                                                             grayscale=grayscale, resize=resize,
                                                             normalisation=normalisation)
        except Exception as e:
            frame_list = []
            print(f"Found Error : {e}")
        return frame_list

    def read_camera(self, source, num_threads=3, fps=None, end_time_sec=None, channel_type='BGR', grayscale=None,
                    resize=None,
                    normalisation=None):
        try:
            if source is None:
                raise FileNotFoundError("Source Not Found")
            if type(source) == int:
                "Single Camera"
                frame_list = self.__read_camera(source, fps=fps, end_time_sec=end_time_sec,
                                                channel_type=channel_type,
                                                grayscale=grayscale, resize=resize,
                                                normalisation=normalisation)
                return frame_list

            elif type(source) == list or type(source) == np.ndarray:
                "Read Images from Camera Concurrently"
                calling_function = partial(self.__read_camera, fps=fps, end_time_sec=end_time_sec,
                                           channel_type=channel_type,
                                           grayscale=grayscale, resize=resize,
                                           normalisation=normalisation)
                with ThreadPoolExecutor(max_workers=num_threads) as executor:
                    frame_list = list(executor.map(calling_function, source))
                if type(source) == list:
                    return frame_list
                else:
                    return np.array(frame_list, dtype=object)
        except Exception as e:
            print(f"Found Error : {e}")
        return None

    @staticmethod
    def __read_video_file(source, fps=None, end_time_sec=None, channel_type='BGR', grayscale=None, resize=None,
                          normalisation=None):
        try:
            frame_source = cv2.VideoCapture(source)
            frame_list = ConcurrentImageReader.__read_frames(frame_source, fps=fps, end_time_sec=end_time_sec,
                                                             channel_type=channel_type,
                                                             grayscale=grayscale, resize=resize,
                                                             normalisation=normalisation)
        except Exception as e:
            frame_list = []
            print(f"Found Error : {e}")
        return frame_list

    def read_video_file(self, source, num_threads=3, fps=None, end_time_sec=None, channel_type='BGR', root_path=None, grayscale=None,
                        resize=None,
                        normalisation=None):
        print(f"root_path : {root_path}")
        try:
            if source is None:
                raise FileNotFoundError("Source Not Found")
            if type(source) == str:
                "Single Video File"
                print(f"source : {source}")
                frame_list = self.__read_video_file(source, fps=fps, end_time_sec=end_time_sec,
                                                    channel_type=channel_type,
                                                    grayscale=grayscale, resize=resize,
                                                    normalisation=normalisation)
                return frame_list
            elif type(source) == list or type(source) == np.ndarray:
                "Read Images from Video File Concurrently"
                new_source = source
                if root_path is not None:
                    new_source = [os.path.join(root_path, x) for x in source]
                print(f"new_source : {new_source}")
                calling_function = partial(self.__read_video_file, fps=fps, end_time_sec=end_time_sec,
                                           channel_type=channel_type,
                                           grayscale=grayscale, resize=resize,
                                           normalisation=normalisation)
                with ThreadPoolExecutor(max_workers=num_threads) as executor:
                    frame_list = list(executor.map(calling_function, new_source))
                if type(source) == list:
                    return frame_list
                else:
                    return np.array(frame_list, dtype=object)
        except Exception as e:
            print(f"Found Error : {e}")
        return None

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
        return None

    def read_dir(self, dir_path, file_type='png', num_threads=3, channel_type='BGR', sub_dir=False, grayscale=None,
                 resize=None,
                 normalisation=None):
        image_list = []
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
        return None
