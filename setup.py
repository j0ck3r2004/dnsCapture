import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='dnsCapture',  

     version='1.1.1',

     author="Vasilis Manthelas",

     author_email="vasilismanthelas2004@gmail.com",

     description="a python packet to capture all DNS traffic",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/j0ck3r2004/dnsCapture",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )
