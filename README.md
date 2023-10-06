
-`pip install pillow`

-`pip install pytesseract`

Note: pytesseract  does not provide true Python bindings. Rather, it simply provides an interface to the tesseract  binary. If you take a look at the project on GitHub you’ll see that the library is writing the image to a temporary file on disk followed by calling the tesseract  binary on the file and capturing the resulting output. This is definitely a bit hackish, but it gets the job done for us.

# How to Run the file
python ocr.py

