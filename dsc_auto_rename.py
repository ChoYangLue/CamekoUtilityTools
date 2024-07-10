import os
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(img):
    exif = img._getexif()
    try:
        for id,val in exif.items():
            tg = TAGS.get(id,id)
            if tg == "DateTimeOriginal":
                return val
    except AttributeError:
        return "NON"
    return "NON"

def rename_files(directory):
    for file in os.listdir(directory):
        #print(file)
        try:
            img = Image.open(directory+file)

            datetimeinfo = get_exif(img)
            filenametemp = datetimeinfo.replace(":", "")
            filenametemp = filenametemp.replace(" ", "_")
            newfilename = "PIC_"+filenametemp+"."+file.split(".")[1] # ex) PIC_20210213_134722.JPG

            img.close()
            
            if datetimeinfo != "NON" and directory+file != directory+newfilename:
                if not os.path.exists(directory+newfilename):
                    os.rename(directory+file, directory+newfilename)
                    print(file+" -->> "+newfilename)
                else:
                    old_file_size = int(os.path.getsize(directory+file))
                    new_file_size = int(os.path.getsize(directory+newfilename))
                    if old_file_size > new_file_size:
                        os.remove(directory+newfilename)
                        os.rename(directory+file, directory+newfilename)
                        print("delete new file")
                    else:
                        os.remove(directory+file)
                        print("delete old file")
                    print(file+" -->> "+newfilename)
        except:
            continue
        

def main():
    target_path = os.getcwd() + "/"
    print(target_path)
    rename_files(target_path)
    input("Finish! Press Any Key to Exit.")

if __name__ == '__main__':
    main()
