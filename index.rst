Concurrent-Image-Read
=====================

|PyPI Status| |image1| |image2| Author : Aditya Mangal \ |image3|

Concurrent-Image-Read is a python module to read Image Files or Image
List Concurrently with multi-threading

.. raw:: html

   <h1>

Installation

.. raw:: html

   </h1>

.. raw:: html

   <h2>

Dependencies

.. raw:: html

   </h2>

.. raw:: html

   <ul>

.. raw:: html

   <li>

Python (>= 3.7)

.. raw:: html

   </li>

.. raw:: html

   <li>

cv2 (>= 4.5)

.. raw:: html

   </li>

.. raw:: html

   <li>

NumPy (>= 1.17)

.. raw:: html

   </li>

.. raw:: html

   <li>

glob (>= 0.7)

.. raw:: html

   </li>

.. raw:: html

   <li>

future (>= 0.18.2)

.. raw:: html

   </li>

.. raw:: html

   </ul>

.. raw:: html

   <h1>

User installation

.. raw:: html

   </h1>

.. raw:: html

   <pre><code>pip install ConcurrentImageRead
   </code></pre>

.. raw:: html

   <h1>

Source code

.. raw:: html

   </h1>

You can check the latest sources with the command:

.. raw:: html

   <pre><code>git clone https://github.com/adityamangal1998/Concurrent-Image-Read.git
   </code></pre>

.. raw:: html

   <h1>

Usage

.. raw:: html

   </h1>

.. raw:: html

   <h2>

Default Parameters

.. raw:: html

   </h2>

.. raw:: html

   <ul>

read function

.. raw:: html

   <li>

image_list = List or Numpy array or Single Path of image

.. raw:: html

   </li>

.. raw:: html

   <li>

num_threads = Number of threads (default 3) (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

channel_type = BGR or RBG (default BGR) (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

root_path = String, Parent path for all files (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

grayscale = True or False (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

resize = List or Tuple resize scale in (width,height) (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

normalisation = True or False, Image array divide by 255 (optional)

.. raw:: html

   </li>

.. raw:: html

   </ul>

.. raw:: html

   <ul>

read_dir function

.. raw:: html

   <li>

dir_path = String, Path of Image Directory

.. raw:: html

   </li>

.. raw:: html

   <li>

file_type = ‘all’ or ‘PNG’,‘JPG’,…etc or [‘JPG’,‘PNG’,…] (case
sensitive) (default png) (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

num_threads = Number of threads (default 3) (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

channel_type = BGR or RBG (default BGR) (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

sub_dir = Bool, Find all Images in all child directory also (default
False) (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

grayscale = True or False (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

normalisation = True or False, Image array divide by 255 (optional)

.. raw:: html

   </li>

.. raw:: html

   </ul>

.. raw:: html

   <ul>

read_camera function

.. raw:: html

   <li>

source = Integer for Webcam or String for Path of Camera or List of
Cameras

.. raw:: html

   </li>

.. raw:: html

   <li>

num_threads = Number of threads (default 3) (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

fps = Integer in seconds, Frame per seconds (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

end_time_sec = Integer in seconds, end time of camera (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

channel_type = BGR or RBG (default BGR) (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

grayscale = True or False (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

normalisation = True or False, Image array divide by 255 (optional)

.. raw:: html

   </li>

.. raw:: html

   </ul>

.. raw:: html

   <ul>

read_video_file function

.. raw:: html

   <li>

source = List or Numpy array or Single Path of Video

.. raw:: html

   </li>

.. raw:: html

   <li>

num_threads = Number of threads (default 3) (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

fps = Integer in seconds, Frame per seconds (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

end_time_sec = Integer in seconds, end time of camera (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

channel_type = BGR or RBG (default BGR) (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

root_path = String, Parent path for all files (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

grayscale = True or False (optional)

.. raw:: html

   </li>

.. raw:: html

   <li>

normalisation = True or False, Image array divide by 255 (optional)

.. raw:: html

   </li>

.. raw:: html

   </ul>

.. raw:: html

   <h2>

With Image List

.. raw:: html

   </h2>

You can check the latest sources with the command:

.. raw:: html

   <pre><code>import ConcurrentImageRead as CIR
   image_list = ['1.png','2.png','3.png']
   images = CIR.read(image_list,num_threads=3, channel_type='BGR',root_path='data')
   </code></pre>

.. raw:: html

   <h2>

With Image Path

.. raw:: html

   </h2>

.. raw:: html

   <pre><code>import ConcurrentImageRead as CIR
   image_path = '1.png'
   images = CIR.read(image_list,num_threads=3, channel_type='BGR',root_path='data')
   </code></pre>

.. raw:: html

   <h2>

With Directory Path

.. raw:: html

   </h2>

.. raw:: html

   <pre><code>import ConcurrentImageRead as CIR
   dir_path = 'data/images'
   images = CIR.read_dir(dir_path,file_type='png', num_threads=3, channel_type='BGR', sub_dir=False)
   </code></pre>

.. raw:: html

   <h2>

With Camera List

.. raw:: html

   </h2>

.. raw:: html

   <pre><code>import ConcurrentImageRead as CIR
   camera_sources = [0,1,2]
   images = CIR.read_camera(camera_sources,num_threads=3,fps=1,end_time_sec=10,channel_type='RGB',normalisation=True,resize=(200,200))
   </code></pre>

.. raw:: html

   <h2>

With Camera Path

.. raw:: html

   </h2>

.. raw:: html

   <pre><code>import ConcurrentImageRead as CIR
   camera_source = 0
   # camera_source = camera url
   images = CIR.read_camera(camera_source,num_threads=3,fps=1,end_time_sec=10,channel_type='RGB',normalisation=True,resize=(200,200))
   </code></pre>

.. raw:: html

   <h2>

With Video List

.. raw:: html

   </h2>

.. raw:: html

   <pre><code>import ConcurrentImageRead as CIR
   video_list = ['1.mp4','2.mp4']
   images = CIR.read_video_file(video_list,num_threads=3,fps=1,root_path='data',end_time_sec=10,channel_type='RGB',normalisation=True,resize=(200,200))
   </code></pre>

.. raw:: html

   <h2>

With Video Path

.. raw:: html

   </h2>

.. raw:: html

   <pre><code>import ConcurrentImageRead as CIR
   video_path = '1.mp4'
   images = CIR.read_video_file(video_path,num_threads=3,fps=1,end_time_sec=10,channel_type='RGB',normalisation=True,resize=(200,200))
   </code></pre>

.. |PyPI Status| image:: https://img.shields.io/badge/pypi%20package-0.0.8-orange
   :target: https://pypi.org/project/ConcurrentImageRead/
.. |image1| image:: https://img.shields.io/github/stars/adityamangal1998/Concurrent-Image-Read
   :target: https://img.shields.io/github/stars/adityamangal1998/Concurrent-Image-Read
.. |image2| image:: https://img.shields.io/github/license/adityamangal1998/Concurrent-Image-Read
   :target: https://img.shields.io/github/license/adityamangal1998/Concurrent-Image-Read
.. |image3| image:: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
   :target: https://www.linkedin.com/in/aditya-mangal/
