from simple_image_download import simple_image_download as so
output = so.simple_image_download
search = ["tamilnadu_bus"] #enter the prompt as per the images you have to download 

for s in search:
    output().download(s,20) #quantity of the images needed.