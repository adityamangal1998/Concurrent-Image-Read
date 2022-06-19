# Concurrent-Image-Read
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
<pre><code>pip install Concurrent-Image-Read
</code></pre>


<h1>Source code</h1>
You can check the latest sources with the command:
<pre><code>git clone https://github.com/adityamangal1998/Concurrent-Image-Read.git
</code></pre>

<h1>Usage</h1>
<h2>Default Parameters</h2>
<ul>read function
<li>num_threads = Number of threads (default 3)</li>
<li>channel_type = BGR or RBG (default BGR)</li>
</ul>
<ul>read_dir function
<li>file_type = Extension of image file (default png)</li>
<li>num_threads = Number of threads (default 3)</li>
<li>channel_type = BGR or RBG (default BGR)</li>
<li>sub_dir = Search in sub folders also (default False)</li>
</ul>

<h2>With Image List</h2>
You can check the latest sources with the command:
<pre><code>import ConcurrentImageRead as CIR
image_list = ['1.png','2.png','3.png']
images = CIR.read(image_list,num_threads=3, channel_type='BGR')
</code></pre>

<h2>With Image Path</h2>
<pre><code>import ConcurrentImageRead as CIR
image_list = '1.png'
images = CIR.read(image_list,num_threads=3, channel_type='BGR')
</code></pre>

<h2>With Directory Path</h2>
<pre><code>import ConcurrentImageRead as CIR
dir_path = 'data/images'
images = CIR.read_dir(dir_path,file_type='png', num_threads=3, channel_type='BGR', sub_dir=False)
</code></pre>
