
# pdf-watermarker
A python command-line utitily to apply watermark to all pages of a pdf
## Usage
1. make sure python is installed
2. create folder for program
3. create new venv inside folder: `virtualenv my_venv`
4. activate venv: `.\my_venv\Scripts\activate`
5. install dependencies: `pip install img2pdf PyPDF2`
6. ` python pdf-watermarker.py [pdf_file] ?[output_file] ?[watermark_file]`
	* `[pdf_file]` - is the path to the pdf file on which you want to add a watermark
	* `?[output_file]` - an optional argument which specifies the **full path** of the output file and default to `.../Desktop/output.pdf`
	* `?[watermark_file]` an optional argument which specifies the full path of the watermark file of type **png**. This value default to the value `DEFAULT_WATERMARK_PATH` which is in file `local_vars.py` which you should place inside same folder as `pdf-watermarker.py`. (as seen in Image1)

### Images
Image1
![Image1](https://lh5.googleusercontent.com/E_wq4CgfzBfonP1eXK2OHPJ5hnaPVoI3mz6UwsM4mxjppL5bw7g_9KNTTHxklC618IJo6MQ48nuZeA=w2289-h1363-rw)
