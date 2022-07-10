from .core import ConcurrentImageReader


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


def read_camera(source, num_threads=3, fps=None, end_time_sec=None, channel_type='BGR', grayscale=None,
                resize=None,
                normalisation=None):
    """
    Read Image from Camera with multi-threading
    :param source: Integer for Webcam or String for Path of Camera or List of Cameras
    :param num_threads: Integer, Number of Threads
    :param fps: Integer in seconds, Frame per seconds
    :param end_time_sec: Integer in seconds, end time of camera
    :param channel_type: 'BGR' or 'RGB', Channel order of Image
    :param grayscale: Bool
    :param resize: List or Tuple resize scale in (width,height)
    :param normalisation: Bool, Image array divide by 255
    :return: List of Image Array
    """
    CIR = ConcurrentImageReader()
    return CIR.read_camera(source, num_threads=num_threads, fps=fps, end_time_sec=end_time_sec,
                           channel_type=channel_type,
                           grayscale=grayscale, resize=resize,
                           normalisation=normalisation)


def read_video_file(source, num_threads=3, fps=None, end_time_sec=None, channel_type='BGR', root_path=None, grayscale=None,
                    resize=None,
                    normalisation=None):
    """
    Read Image from Video files with multi-threading
    :param source: List or Numpy array or Single Path of Video
    :param num_threads: Integer, Number of Threads
    :param fps: Integer in seconds, Frame per seconds
    :param end_time_sec: Integer in seconds, end time of camera
    :param channel_type: 'BGR' or 'RGB', Channel order of Image
    :param root_path: str, Parent path for all files
    :param grayscale: Bool
    :param resize: List or Tuple resize scale in (width,height)
    :param normalisation: Bool, Image array divide by 255
    :return: List of Image Array
    """
    CIR = ConcurrentImageReader()
    return CIR.read_video_file(source, num_threads=num_threads, fps=fps, end_time_sec=end_time_sec,
                               channel_type=channel_type,root_path=root_path,
                               grayscale=grayscale, resize=resize,
                               normalisation=normalisation)
