# Concurrent-Image-Read
[![PyPI Status](https://img.shields.io/badge/pypi%20package-0.0.8-orange)](https://pypi.org/project/ConcurrentImageRead/)
[![PyPI Status](https://img.shields.io/github/stars/adityamangal1998/Concurrent-Image-Read)](https://img.shields.io/github/stars/adityamangal1998/Concurrent-Image-Read)
[![PyPI Status](https://img.shields.io/github/license/adityamangal1998/Concurrent-Image-Read)](https://img.shields.io/github/license/adityamangal1998/Concurrent-Image-Read)
<br><br>
<b>Author : Aditya Mangal </b>[![PyPI Status](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aditya-mangal/)


<br>
 <b>Concurrent-Image-Read</b> is a python module to read Image Files or Image List Concurrently with multi-threading
<h1>Installation</h1>

<h2>Dependencies</h2>
<ul>
<li>Python (>= 3.7)</li>
<li>cv2 (>= 4.5)</li>
<li>NumPy (>= 1.17)</li>
<li>glob (>= 0.7)</li>
<li>future (>= 0.18.2)</li>
</ul>

<h1>User installation</h1>
<pre><code>pip install ConcurrentImageRead
</code></pre>


<h1>Source code</h1>
You can check the latest sources with the command:
<pre><code>git clone https://github.com/adityamangal1998/Concurrent-Image-Read.git
</code></pre>

<h1>Usage</h1>
<h2>Default Parameters</h2>
<ul><b>read function</b>
<li>image_list = List or Numpy array or Single Path of image</li>
<li>num_threads = Number of threads (default 3) <b>(optional)</b></li>
<li>channel_type = BGR or RBG (default BGR) <b>(optional)</b></li>
<li>root_path = String, Parent path for all files <b>(optional)</b></li>
<li>grayscale = True or False <b>(optional)</b></li>
<li>resize = List or Tuple resize scale in (width,height) <b>(optional)</b></li>
<li>normalisation = True or False, Image array divide by 255 <b>(optional)</b></li>
</ul>

<ul><b>read_dir function</b>
<li>dir_path = String, Path of Image Directory</li>
<li>file_type = 'all' or 'PNG','JPG',...etc or ['JPG','PNG',...] <b>(case sensitive)</b> (default png) <b>(optional)</b></li>
<li>num_threads = Number of threads (default 3) <b>(optional)</b></li>
<li>channel_type = BGR or RBG (default BGR) <b>(optional)</b></li>
<li>sub_dir = Bool, Find all Images in all child directory also (default False) <b>(optional)</b></li>
<li>grayscale = True or False <b>(optional)</b></li>
<li>normalisation = True or False, Image array divide by 255 <b>(optional)</b></li>
</ul>

<ul><b>read_camera function</b>
<li>source = Integer for Webcam or String for Path of Camera or List of Cameras</li>
<li>num_threads = Number of threads (default 3) <b>(optional)</b></li>
<li>fps = Integer in seconds, Frame per seconds <b>(optional)</b></li>
<li>end_time_sec = Integer in seconds, end time of camera <b>(optional)</b></li>
<li>channel_type = BGR or RBG (default BGR) <b>(optional)</b></li>
<li>grayscale = True or False <b>(optional)</b></li>
<li>normalisation = True or False, Image array divide by 255 <b>(optional)</b></li>
</ul>

<ul><b>read_video_file function</b>
<li>source = List or Numpy array or Single Path of Video</li>
<li>num_threads = Number of threads (default 3) <b>(optional)</b></li>
<li>fps = Integer in seconds, Frame per seconds <b>(optional)</b></li>
<li>end_time_sec = Integer in seconds, end time of camera <b>(optional)</b></li>
<li>channel_type = BGR or RBG (default BGR) <b>(optional)</b></li>
<li>root_path = String, Parent path for all files <b>(optional)</b></li>
<li>grayscale = True or False <b>(optional)</b></li>
<li>normalisation = True or False, Image array divide by 255 <b>(optional)</b></li>
</ul>

<h2>With Image List</h2>
You can check the latest sources with the command:
<pre><code>import ConcurrentImageRead as CIR
image_list = ['1.png','2.png','3.png']
images = CIR.read(image_list,num_threads=3, channel_type='BGR',root_path='data')
</code></pre>

<h2>With Image Path</h2>
<pre><code>import ConcurrentImageRead as CIR
image_path = '1.png'
images = CIR.read(image_list,num_threads=3, channel_type='BGR',root_path='data')
</code></pre>

<h2>With Directory Path</h2>
<pre><code>import ConcurrentImageRead as CIR
dir_path = 'data/images'
images = CIR.read_dir(dir_path,file_type='png', num_threads=3, channel_type='BGR', sub_dir=False)
</code></pre>

<h2>With Camera List</h2>
<pre><code>import ConcurrentImageRead as CIR
camera_sources = [0,1,2]
images = CIR.read_camera(camera_sources,num_threads=3,fps=1,end_time_sec=10,channel_type='RGB',normalisation=True,resize=(200,200))
</code></pre>

<h2>With Camera Path</h2>
<pre><code>import ConcurrentImageRead as CIR
camera_source = 0
# camera_source = camera url
images = CIR.read_camera(camera_source,num_threads=3,fps=1,end_time_sec=10,channel_type='RGB',normalisation=True,resize=(200,200))
</code></pre>

<h2>With Video List</h2>
<pre><code>import ConcurrentImageRead as CIR
video_list = ['1.mp4','2.mp4']
images = CIR.read_video_file(video_list,num_threads=3,fps=1,root_path='data',end_time_sec=10,channel_type='RGB',normalisation=True,resize=(200,200))
</code></pre>

<h2>With Video Path</h2>
<pre><code>import ConcurrentImageRead as CIR
video_path = '1.mp4'
images = CIR.read_video_file(video_path,num_threads=3,fps=1,end_time_sec=10,channel_type='RGB',normalisation=True,resize=(200,200))
</code></pre>

