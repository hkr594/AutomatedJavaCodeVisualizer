import os
import path
import re

def find_levels(directory):
    cc=[]
    sc=[]
    rc=[]
    sba=[]
    for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                if ".java" not in filename:
                    continue
                file_path=os.path.join(dirpath, filename)
                try:
                    myfile=open(file_path,"r", encoding='utf-8')
                    level=""
                    myline=myfile.readline()
                    while myline:
                        if "@Controller" in myline or "@RestController" in myline:
                            level="Controller"
                            cc.append([file_path,filename.strip(".java")])
                            break
                        if "@SpringBootApplication" in myline or "@EnableAutoConfiguration" in myline:
                            level="Application Run Class"
                            sba.append([file_path,filename.strip(".java")])
                            break
                        if "@Service" in myline:
                            level="Service"
                            sc.append([file_path,filename.strip(".java")])
                            break
                        if "@Repository" in myline:
                            level="Repository"
                            rc.append([file_path,filename.strip(".java")])
                            break
                        myline=myfile.readline()
                except:
                    print("File not readable")
    return(sba,cc,sc,rc)

def sc_mapping_controllers(cc):
    sc_mapping={}
    for cc_data in cc:
        cc_class=cc_data[1]
        cc_file=open(cc_data[0],"r",encoding='utf-8')
        myline=cc_file.readline()
        while myline:  
            while "import" in myline or myline == "\n":
                myline=cc_file.readline()      
            for sc_data in sc:
                if sc_data[1] in myline:
                    myline=myline.strip("\n").strip()
                    sc_name=myline.split(" ")[0]
                    sc_var=myline.split(" ")[1].strip(";")
                    sc_mapping[sc_var]=sc_name
                    break
            myline=cc_file.readline()
        cc_file.close()
    return(sc_mapping)

def parsing_controllers(cc,sc_to_var_mapping):
    for cc_data in cc:
        cc_class=cc_data[1]
        cm_to_sm={}
        cc_file=open(cc_data[0],"r",encoding='utf-8')
        myline=cc_file.readline()
        # new_method=0
        cm = ""
        while myline:
            for sc_variable in sc_to_var_mapping.keys():
                sco = sc_variable
            if "public" in myline and "(" in myline:
                #   new_method=0
                cc_method_call=myline.split("(")[0]
                cc_method=cc_method_call.split()[-1]
                cc_node=cc_class+"."+cc_method
                cm = cc_method
                
                #   new_method = 1  
        
            elif sco in myline:
                try:
                    sm_value = myline.split(".")[1]
                    sm = sm_value.split("(")[0]
                    if cc_class!= "" and cm != "" and sc_to_var_mapping[sco] != "" and sm != "":
                        print(cc_class +","+ cm +","+sc_to_var_mapping[sco]+ "," + sm)
                except: 
                    pass
            myline=cc_file.readline()


def rc_mapping_service(sc):
    sc_mapping={}
    for cc_data in sc:
        cc_class=cc_data[1]
        cc_file=open(cc_data[0],"r",encoding='utf-8')
        myline=cc_file.readline()
        while myline:  
            while "import" in myline or myline == "\n":
                myline=cc_file.readline()      
            for sc_data in rc:
                if sc_data[1] in myline:
                    myline=myline.strip("\n").strip()
                    sc_name=myline.split(" ")[0]
                    sc_var=myline.split(" ")[1].strip(";")
                    sc_mapping[sc_var]=sc_name
                    break
            myline=cc_file.readline()
        cc_file.close()
    return(sc_mapping)

def parsing_service(sc,rc_to_var_mapping):
    for cc_data in sc:
        cc_class=cc_data[1]
        cm_to_sm={}
        cc_file=open(cc_data[0],"r",encoding='utf-8')
        myline=cc_file.readline()
        # new_method=0
        cm = ""
        while myline:
            for sc_variable in rc_to_var_mapping.keys():
                sco = sc_variable
            if "public" in myline and "(" in myline:
                #   new_method=0
                cc_method_call=myline.split("(")[0]
                cc_method=cc_method_call.split()[-1]
                cc_node=cc_class+"."+cc_method
                cm = cc_method
                
                #   new_method = 1  
        
            elif sco in myline:
                try:
                    sm_value = myline.split(".")[1]
                    sm = sm_value.split("(")[0]
                    if cc_class!= "" and cm != "" and rc_to_var_mapping[sco] != "" and sm != "":
                        print(cc_class +","+ cm +","+rc_to_var_mapping[sco]+ "," + sm)
                except: 
                    pass
            myline=cc_file.readline()


# Assign directory

directory = r"/<path>/demo-application-master"
# spring-mvc-mybatis-sample-master"
sba,cc,sc,rc=find_levels(directory)
#print(sba,cc,sc,rc)
sc_to_var_mapping=sc_mapping_controllers(cc)
parsing_controllers(cc,sc_to_var_mapping)

rc_to_var_mapping=rc_mapping_service(sc)
parsing_service(sc,rc_to_var_mapping)