from service.pdfgen import genpdf1

def renderSpace():
    data =    {
            "height": 2,
            "styles": {
            "font": "Times",
            "fontSize": 8,
            "leftPadding": 10
            },
            "columns": [
        {
            "format": "text",
            "data": "",
            "width": 100
            }
        ]
        }
    return data

def renderHeading(val):
    data =   {
            "height": 2,
            "styles": {
            "font": "Times",
            "fontSize": 8,
            "bold": "true",
            "bgcolor": "black",
            "fontColor": "white",
            "border": 1
            },
            "columns": [
            {
                "format": "text",
                "data": f"{val}",
                "width": 100
            }
            ]
        }
    return data

def renderFirstName(fullName):
    data = {
    "height": 2,
    "styles": {
    "font": "Times",
    "bold": "false",
    "fontColor": "black",
    "fontSize": 16,
    },
    "columns": [
    {
        "align" : "center",
        "format": "text",
        "data": f"{fullName}",
        "width": 100
    }
    ]
    }

    return data

def renderAddressAndPhone(addressAndPhone):
    data =    {
            "height": 2,
            "styles": {
            "font": "Times",
            "fontSize": 8,
            # "leftPadding": 10
            },
            "columns": [
            {
                "format": "text",
                "align" : "center",
                "data": f"{addressAndPhone[0]+' | '+addressAndPhone[2]+' | '}{addressAndPhone[1]}",
                "width": 100
            }
            ]
        }

    return data

def renderEducationalDetails(template,educationalDetails,index):
    data1 =    {
            "height": 2,
            "styles": {
            "font": "Times",
            "fontSize": 8,
            "leftPadding": 10,
            "bold":"true"
            },
            "columns": [
            {
                "format": "text",
                # "align" : "center",
                "data": f"{educationalDetails[index].get('collegename')}",
                "width": 70
            },
            {
                "format": "text",
                # "align" : "center",
                "data": f"{educationalDetails[index].get('location')}",
                "width": 30
            }
            ]
        }
    template['rows'].append(data1)
    data2 =  {
            "height": 2,
            "styles": {
            "font": "Times",
            "fontSize": 4,
            "leftPadding": 10
            },
            "columns": [
            {
                "format": "text",
                # "align" : "center",
                "data": f"{educationalDetails[index].get('degree')+' '+ 'GPA '+educationalDetails[index].get('grade')}",
                "width": 70
            },
            {
                "format": "text",
                # "align" : "center",
                "data": f"{educationalDetails[index].get('duration')}",
                "width": 30
            }
            ]
        }
    template['rows'].append(data2)
    return

def renderWorkExperience(template,workExperience,index):
    data1=    {
            "height": 2,
            "styles": {
            "font": "Times",
            "fontSize": 8,
            "leftPadding": 10
            },
            "columns": [
            {
                "format": "text",
                # "align" : "center",
                "data": f"{workExperience[index].get('CompanyName')+' | '+workExperience[index].get('designation')}",
                "width": 70
            },
            {
                "format": "text",
                # "align" : "center",
                "data": f"{workExperience[index].get('Location')+' | '+workExperience[index].get('duration')}",
                "width": 30
            }
            ]
        }
    template['rows'].append(data1)
    data2=    {
            "height": 2,
            "styles": {
            "font": "Times",
            "fontSize": 8,
            "leftPadding": 30
            },
            "columns": [
            {
                "format": "text",
                # "align" : "center",
                "data": f"{workExperience[index].get('Techstacks')[0]}",
                "width": 100
            }
            ]
        }
    template['rows'].append(data2)

    return

def renderSkills(skills,key,val):
    mapp={"programmingLangs":"Programming Languages","librariesOrFrameworks":"Libraries/Frameworks","toolsOrPlatforms":"Tools/Platforms","databases":"Databases"}
    data =   {
            "height": 2,
            "styles": {
            "font": "Times",
            "fontSize": 8,
            # "leftPadding": 10
            "leftPadding":30
            },
            "columns": [
            {
                "format": "text",
                # "align" : "center",
                
                "data": f"{mapp[key]}:",
                "width": 23
            },
            {
                "format": "text",
                # "align" : "center",
                # "leftPadding":"20",
                "data": f"{skills[0].get(key)}",
                "width": 77
            }
            ]
        }

    return data

def renderProjects(template,projects,index,some=None):
    data1 =    {
            "height": 2,
            "styles": {
            "font": "Times",
            "fontSize": 8,
            "bold":"true",
            # "leftPadding": 10
            "leftPadding":27
            },
            "columns": [
            {
                "format": "text",
                # "align" : "center",
                
                "data": f"{projects[index].get('projectName')}",
                "width": 42
            },
            {
                "format": "text",
                # "align" : "center",
                # "leftPadding":"20",
                "data": f"{projects[index].get('techstacks')}",
                "width": 58
            }
            ]
        }
    # a = genpdf1.template
    # a['rows'].append(data1)
    template['rows'].append(data1)
    data2=    {
            "height": 2,
            "styles": {
            "font": "Times",
            "fontSize": 4,
            # "leftPadding": 10
            "leftPadding":27
            },
            "columns": [
            {
                "format": "text",
                "data": f"{projects[index].get('briefInfo')}",
                "width": 100
            }
            ]
        }
    # genpdf1.template['rows'].append(data2)
    # a['rows'].append(data2)
    template['rows'].append(data2)
    
    # print("hiiii",genpdf1.varr)
    # if genpdf1.varr==1:

    #     dataspace = {
    #         "height": 2,
    #         "styles": {
    #         "font": "Times",
    #         "fontSize": 8,
    #         "leftPadding": 10
    #         },
    #         "columns": [
    #     {
    #         "format": "text",
    #         "data": "",
    #         "width": 100
    #         }
    #     ]
    #     }
    #     template['rows'].append(dataspace)
    return

def renderHobbies(template,hobbies,index,some=None):
    # print("hereeeeeeeee",some)
    # if some=="abc":
    #     dataspace = {
    #         "height": 2,
    #         "styles": {
    #         "font": "Times",
    #         "fontSize": 8,
    #         "leftPadding": 10
    #         },
    #         "columns": [
    #     {
    #         "format": "text",
    #         "data": "",
    #         "width": 100
    #         }
    #     ]
    #     }
    #     template['rows'].append(dataspace)


    data=    {
            "height": 2,
            "styles": {
            "font": "Times",
            "fontSize": 8,
            # "leftPadding": 10
            "leftPadding":27,
            "topPadding":10
            },
            "columns": [
            {
                "format": "text",
                "data": f"{hobbies[index]}",
                "width": 100
            }
            ]
        }
    template['rows'].append(data)
    return
