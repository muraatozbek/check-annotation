import glob
import xml.etree.ElementTree as ET
import os
import shutil

xml_dir='/path/of/folder/*.xml'
xmls=glob.glob(xml_dir)

#Counting  Annatations error
annotation_cnt=0
size_cnt=0
boundingbox_cnt=0
xml_counter=0


# labels_names
if not os.path.exists("check_annotation"):
            os.mkdir("check_annotation")
            os.mkdir("check_annotation/logs")
            os.mkdir("check_annotation/xmls")
#for writing errors xml to txt fils
annatation_write = open("check_annotation/logs/annotation_error_fils.txt", "w")
size_write = open("check_annotation/logs/size_error_fils.txt", "w")
boundingbox_write = open("check_annotation/logs/boundingbox_error_fils.txt", "w")
total_classes=[]
for xml in xmls:
        tree = ET.parse(xml)
        root = tree.getroot()
        
        annotation = root.tag
        size = root.find('size')
        boundingbox=root.find('object')
        xml_counter=xml_counter+1
        
        # print(class_name)        
        if annotation!="annotation":
            annotation_cnt=annotation_cnt+1
            annatation_write.write(xml+"\n")
            try:
                shutil.move(xml,"check_annotation/xmls/"+xml.split("/")[-1])
                # print("check_annotation/xmls/"+xml.split("/")[-1])
            except:
                pass
            # shutil.move(xml.split(".")[0]+"")
            
        if not size:
            size_cnt=size_cnt+1
            size_write.write(xml+"\n")
            try:
                shutil.move(xml,"check_annotation/xmls/"+xml.split("/")[-1])
                # print("check_annotation/xmls/"+xml.split("/")[-1])
            except:
                pass

            
        if not boundingbox:
            boundingbox_cnt=boundingbox_cnt+1
            boundingbox_write.write(xml+"\n")
            try:
                shutil.move(xml,"check_annotation/xmls/"+xml.split("/")[-1])
                # print("check_annotation/xmls/"+xml.split("/")[-1])
            except:
                pass
            
        if boundingbox:
            class_name=boundingbox.find('name')
            class_name=class_name.text
            if str(class_name) not in total_classes :
                total_classes.append(class_name)
            
    
            
print("\nTotal Xml files read: {}" .format(xml_counter))
print("\nTotal Errors in XML is : {}" .format(annotation_cnt+size_cnt+boundingbox_cnt))
print("\nTotal annotation Element not found are : {}" .format(annotation_cnt))
print("\nTotal size Element not found are : {}" .format(size_cnt))
print("\nTotal boundingbox Element not found are : {}" .format(boundingbox_cnt))
print("\nTotal Classes are {} they names are {}" .format(len(total_classes),total_classes))
