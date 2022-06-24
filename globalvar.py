# template = {
#         "rows": [
#         # {
#         #     "height": 2,
#         #     "styles": {
#         #     "font": "Times",
#         #     "fontSize": 8,
#         #     "leftPadding": 10
#         #     },
#         #     "columns": [
#         #     {
#         #         "format": "text",
#         #         "data": "",
#         #         "width": 100
#         #     }
#         #     ]
#         # },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "bold": "false",
#             "fontColor": "black",
#             "fontSize": 16,
#             },
#             "columns": [
#             {
#                 "align" : "center",
#                 "format": "text",
#                 "data": f"{fullName}",
#                 "width": 100
#             }
#             ]
#         },
#         # DOne above
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 "align" : "center",
#                 "data": f"{addressAndPhone[0]+' | '+addressAndPhone[2]+' | '}{addressAndPhone[1]}",
#                 "width": 100
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "leftPadding": 10
#             },
#             "columns": [
#         {
#             "format": "text",
#             "data": "",
#             "width": 100
#             }
#         ]
#         },
#         # Done
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "bold": "true",
#             "bgcolor": "black",
#             "fontColor": "white",
#             "border": 1
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 "data": "Education",
#                 "width": 100
#             }
#             ]
#         },
#         # {
#         #     "height": 2,
#         #     "styles": {
#         #     "font": "Times",
#         #     "fontSize": 8,
#         #     "leftPadding": 10
#         #     },
#         #     "columns": [
#         # {
#         #     "format": "text",
#         #     "data": "",
#         #     "width": 100
#         #     }
#         # ]
#         # },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "leftPadding": 10
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{educationalDetails[0].get('collegename')}",
#                 "width": 70
#             },
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{educationalDetails[0].get('location')}",
#                 "width": 30
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{educationalDetails[0].get('degree')+' '+ 'GPA '+educationalDetails[0].get('grade')}",
#                 "width": 70
#             },
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{educationalDetails[0].get('duration')}",
#                 "width": 30
#             }
#             ]
#         },
#         {
#             "height": 1,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "leftPadding": 10
#             },
#             "columns": [
#         {
#             "format": "text",
#             "data": "",
#             "width": 100
#             }
#         ]
#         },
#                 {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{educationalDetails[1].get('collegename')}",
#                 "width": 70
#             },
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{educationalDetails[1].get('location')}",
#                 "width": 30
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{educationalDetails[1].get('degree')+' '+ 'GPA '+educationalDetails[1].get('grade')}",
#                 "width": 70
#             },
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{educationalDetails[1].get('duration')}",
#                 "width": 30
#             }
#             ]
#         },
#         {
#             "height": 1,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "leftPadding": 10
#             },
#             "columns": [
#         {
#             "format": "text",
#             "data": "",
#             "width": 100
#             }
#         ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{educationalDetails[2].get('collegename')}",
#                 "width": 70
#             },
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{educationalDetails[2].get('location')}",
#                 "width": 30
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{educationalDetails[2].get('degree')+' '+ 'GPA '+educationalDetails[2].get('grade')}",
#                 "width": 70
#             },
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{educationalDetails[2].get('duration')}",
#                 "width": 30
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "leftPadding": 10
#             },
#             "columns": [
#         {
#             "format": "text",
#             "data": "",
#             "width": 100
#             }
#         ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "bold": "true",
#             "bgcolor": "black",
#             "fontColor": "white",
#             "border": 1
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 "data": "Experience",
#                 "width": 100
#             }
#             ]
#         },
#         # {
#         #     "height": 2,
#         #     "styles": {
#         #     "font": "Times",
#         #     "fontSize": 8,
#         #     "leftPadding": 10
#         #     },
#         #     "columns": [
#         # {
#         #     "format": "text",
#         #     "data": "",
#         #     "width": 100
#         #     }
#         # ]
#         # },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{workExperience[0].get('CompanyName')+' | '+workExperience[0].get('designation')}",
#                 "width": 70
#             },
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{workExperience[0].get('Location')+' | '+workExperience[0].get('duration')}",
#                 "width": 30
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "leftPadding": 30
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{workExperience[0].get('Techstacks')[0]}",
#                 "width": 100
#             }
#             ]
#         },
#         {
#             "height": 1,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "leftPadding": 10
#             },
#             "columns": [
#         {
#             "format": "text",
#             "data": "",
#             "width": 100
#             }
#         ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{workExperience[1].get('CompanyName')+' | '+workExperience[1].get('designation')}",
#                 "width": 70
#             },
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{workExperience[1].get('Location')+' | '+workExperience[1].get('duration')}",
#                 "width": 30
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "leftPadding": 30
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 "data": f"{workExperience[1].get('Techstacks')[0]}",
#                 "width": 100
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "leftPadding": 10
#             },
#             "columns": [
#         {
#             "format": "text",
#             "data": "",
#             "width": 100
#             }
#         ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "bold": "true",
#             "bgcolor": "black",
#             "fontColor": "white",
#             "border": 1
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 "data": "Skills",
#                 "width": 100
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             "leftPadding":30
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
                
#                 "data": "Programming Languages:",
#                 "width": 23
#             },
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 # "leftPadding":"20",
#                 "data": f"{skills[0].get('programmingLangs')}",
#                 "width": 77
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             "leftPadding":30
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
                
#                 "data": "Libraries/Frameworks:",
#                 "width": 23
#             },
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 # "leftPadding":"20",
#                 "data": f"{skills[0].get('librariesOrFrameworks')}",
#                 "width": 77
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             "leftPadding":30
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
                
#                 "data": "Tools/Platforms:",
#                 "width": 23
#             },
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 # "leftPadding":"20",
#                 "data": f"{skills[0].get('toolsOrPlatforms')}",
#                 "width": 77
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             "leftPadding":30
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
                
#                 "data": "Databases:",
#                 "width": 23
#             },
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 # "leftPadding":"20",
#                 "data": f"{skills[0].get('databases')}",
#                 "width": 77
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "leftPadding": 10
#             },
#             "columns": [
#         {
#             "format": "text",
#             "data": "",
#             "width": 100
#             }
#         ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "bold": "true",
#             "bgcolor": "black",
#             "fontColor": "white",
#             "border": 1
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 "data": "Projects/Open Source",
#                 "width": 100
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "bold":"true",
#             # "leftPadding": 10
#             "leftPadding":27
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
                
#                 "data": f"{projects[0].get('projectName')}",
#                 "width": 42
#             },
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 # "leftPadding":"20",
#                 "data": f"{projects[0].get('techstacks')}",
#                 "width": 58
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             "leftPadding":27
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 "data": f"{projects[0].get('briefInfo')}",
#                 "width": 100
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "leftPadding": 10
#             },
#             "columns": [
#         {
#             "format": "text",
#             "data": "",
#             "width": 100
#             }
#         ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "bold":"true",
#             # "leftPadding": 10
#             "leftPadding":27
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 # "align" : "center",
                
#                 "data": f"{projects[1].get('projectName')}",
#                 "width": 42
#             },
#             {
#                 "format": "text",
#                 # "align" : "center",
#                 # "leftPadding":"20",
#                 "data": f"{projects[1].get('techstacks')}",
#                 "width": 58
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             "leftPadding":27
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 "data": f"{projects[1].get('briefInfo')}",
#                 "width": 100
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "leftPadding": 10
#             },
#             "columns": [
#         {
#             "format": "text",
#             "data": "",
#             "width": 100
#             }
#         ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "bold": "true",
#             "bgcolor": "black",
#             "fontColor": "white",
#             "border": 1
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 "data": "Certificates",
#                 "width": 100
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             "leftPadding":27
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 "data": f"{certificates[0]}",
#                 "width": 100
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "leftPadding": 10
#             },
#             "columns": [
#         {
#             "format": "text",
#             "data": "",
#             "width": 100
#             }
#         ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "bold": "true",
#             "bgcolor": "black",
#             "fontColor": "white",
#             "border": 1
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 "data": "Hobbies",
#                 "width": 100
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             "leftPadding":27
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 "data": f"{hobbies[0]}",
#                 "width": 100
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "leftPadding": 10
#             },
#             "columns": [
#         {
#             "format": "text",
#             "data": "",
#             "width": 100
#             }
#         ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "bold": "true",
#             "bgcolor": "black",
#             "fontColor": "white",
#             "border": 1
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 "data": "Extra Curricular",
#                 "width": 100
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             "leftPadding":27
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 "data": f"{extraCurricular[0]}",
#                 "width": 100
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "leftPadding": 10
#             },
#             "columns": [
#         {
#             "format": "text",
#             "data": "",
#             "width": 100
#             }
#         ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             "bold": "true",
#             "bgcolor": "black",
#             "fontColor": "white",
#             "border": 1
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 "data": "Achievements",
#                 "width": 100
#             }
#             ]
#         },
#         {
#             "height": 2,
#             "styles": {
#             "font": "Times",
#             "fontSize": 8,
#             # "leftPadding": 10
#             "leftPadding":27
#             },
#             "columns": [
#             {
#                 "format": "text",
#                 "data": f"{achievements[0]}",
#                 "width": 100
#             }
#             ]
#         }

#         ]
#     }