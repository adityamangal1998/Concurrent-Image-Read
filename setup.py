from setuptools import setup

setup(
    name='ConcurrentImageRead',
    version='0.0.1',
    description='Read Image Directory or Image List simultaneously with multi-processing',
    url='https://github.com/adityamangal1998/Concurrent-Image-Read.git',
    author='Aditya Mangal',
    author_email='adityamangal98@gmail.com',
    license="MIT",
    packages=['ConcurrentImageRead'],
    install_requires=['opencv-python',
                      'numpy',
                      'future',
                      'glob'
                      ],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)