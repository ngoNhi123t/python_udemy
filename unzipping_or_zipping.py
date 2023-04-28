#Create Files to Compress
# slashes(\) may need to change for MacOS or Linux
f = open("new_file.txt",'w+')
f.write("Here is some text")
f.close()
f=open("new_file2.txt",'w+')
f.write("Here is some text")
f.close()

####ZIPPING FILE
#To compress all files in a folder, just use the os.walk() method to iterate this process for all the files in a directory.
import zipfile
 
comp_file=zipfile.ZipFile('comp_file.zip','w')
comp_file.write("new_file.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

#### Extracting from Zip Files
#trichs xuaats teepj abwngf extractall(): all
#rieng le: etract()
zip_obj=zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall("extracted_content")

#USING SHUTIL LIBRARY
# luwu tru all cung luc
import shutil
#Thư viện Shutil có thể chấp nhận tham số định dạng, định dạng là định dạng lưu trữ: một trong số "zip", "tar", "gztar", "bztar" hoặc "xztar"
pwd
'C:\\Users\\Marcial\\Pierian-Data-Courses\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules'
directory_to_zip='C:\\Users\\Marcial\\Pierian-Data-Courses\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules'
# Creating a zip archive
output_filename = 'example'
# Just fill in the output_filename and the directory to zip
# Note this won't run as is because the variable are undefined
shutil.make_archive(output_filename,'zip',directory_to_zip)
'C:\\Users\\Marcial\\Pierian-Data-Courses\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules\\example.zip'
# Extracting a zip archive
# Notice how the parameter/argument order is slightly different here
shutil.unpack_archive(output_filename,dir_for_extract_result,'zip')
