from setuptools import setup

setup(
    name='ConcurrentImageRead',
    version='0.0.1',
    description='Read Image Directory or Image List simultaneously with multi-processing',
    url='https://github.com/shuds13/pyexample',
    author='Aditya Mangal',
    author_email='adityamangal98@gmail.com',
    license="MIT",
    packages=['ConcurrentImageRead'],
    install_requires=['mpi4py>=2.0',
                      'numpy',
                      ],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)