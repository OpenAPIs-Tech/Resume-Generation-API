# Resume-PDF Generation Service

## Running on local machine

1. From root directory, Create virtual environment
```shell
python3 -m venv [name_of_virtual_env]
```

2. Activate virtual environment
```shell
source [name_of_virtual_env]/bin/activate
```

3. Install dependencies
```shell
pip install -r requirements.txt
```

4. Run the application
```shell
python main.py
```

## for end point of POST Request --> https://openapis.herokuapp.com/generatePdf
#### It returns pdf data in base64 string which can be used in frontend to render it.

Input Payload:
```
{
    "fullName": "Emaddd Razaa khan",
    "addressAndPhone": [
        "emadk3@gmail.com",
        "Raza Manzil, Ward Number 7, Bihar-844506",
        "+91-7667149548"
    ],
    "educationalDetail": [
        {
            "degree": "B.Tech Mecanical Engineering",
            "location": "Aligarh,India",
            "collegename": "Aligarh Muslim University",
            "grade": "8.01",
            "duration": "20-03-2018 to 22-05-2022"
        },
        {
            "degree": "Intermediate",
            "location": "Patna,India",
            "collegename": "Dr. Zakir Husain High School +2",
            "grade": "7.6",
            "duration": "20-03-2015 to 22-05-2017"
        },
        {
            "degree": "Matriculation",
            "location": "Patna,India",
            "collegename": "T. Raja High School +2",
            "grade": "10",
            "duration": "20-03-2014 to 22-05-2015"
        }
    ],
    "workExperience": [
        {
            "CompanyName": "BDIPlus Private Limited",
            "designation": "Software Engineer",
            "Location": "Bengaluru",
            "duration": "May-2022 to Present",
            "Techstacks": [
                "Working on RESTful APIs development"
            ]
        },
        {
            "CompanyName": "Filo Edtech Pvt Ltd",
            "designation": "Software Engineer Intern",
            "Location": "Gurugram",
            "duration": "Jan-2022 to April 2022",
            "Techstacks": [
                "Worked on APIs development on Django Rest Framework, Dockerisation of Application"
            ]
        }
    ],
    "projects": [
        {
           "projectName": "Open Source Resume Builder API",
           "techstacks": "Python, Flask, REST",
           "briefInfo": "API which takes all user information and return PDF"
        },
        {
           "projectName": "CRUD Operations backend",
           "techstacks": "Java, Spring boot",
           "briefInfo": "Different end points for CRUD operationss"
        }
    ],
    "skills": [
        {
            "programmingLangs": "Python, Java",
            "librariesOrFrameworks": "Flask, Django, Spring boot",
            "toolsOrPlatforms": "Docker, REST, Postman, Insomnia, Git",
            "databases": "MySQL, Redis"
        }
    ],
    "certificates": [
        {
            "certificate":"C++ from udemy"
        },
        {
            "certificate":"Java from udemy"
        }
    ],
    "hobbies": [
        {
            "hobby":"Music"
        },
        {
            "hobby":"Badminton"
        }
    ],
    "extraCurricular": [
        {
            "activity":"Sports"
        },
        {
            "activity":"Volunteering"
        }
    ],
    "achievements": [
        {
            "achievement":"Winner of Mr. Fresher event"
        }
    ]
}
```


Output:
```
{
    "data": "JVBERi0xLjQKJZOMi54gUmVwb3J0TGFiIEdlbmVyYXRlZCBQREYgZG9jdW1lbnQgaHR0cDovL3d3dy5yZXBvcnRsYWIuY29tCjEgMCBvYmoKPDwKL0YxIDIgMCBSIC9GMiAzIDAgUgo+PgplbmRvYmoKMiAwIG9iago8PAovQmFzZUZvbnQgL0hlbHZldGljYSAvRW5jb2RpbmcgL1dpbkFuc2lFbmNvZGluZyAvTmFtZSAvRjEgL1N1YnR5cGUgL1R5cGUxIC9UeXBlIC9Gb250Cj4+CmVuZG9iagozIDAgb2JqCjw8Ci9CYXNlRm9udCAvVGltZXMtQm9sZCAvRW5jb2RpbmcgL1dpbkFuc2lFbmNvZGluZyAvTmFtZSAvRjIgL1N1YnR5cGUgL1R5cGUxIC9UeXBlIC9Gb250Cj4+CmVuZG9iago0IDAgb2JqCjw8Ci9Db250ZW50cyA4IDAgUiAvTWVkaWFCb3ggWyAwIDAgNTk1LjI3NTYgODQxLjg4OTggXSAvUGFyZW50IDcgMCBSIC9SZXNvdXJjZXMgPDwKL0ZvbnQgMSAwIFIgL1Byb2NTZXQgWyAvUERGIC9UZXh0IC9JbWFnZUIgL0ltYWdlQyAvSW1hZ2VJIF0KPj4gL1JvdGF0ZSAwIC9UcmFucyA8PAoKPj4gCiAgL1R5cGUgL1BhZ2UKPj4KZW5kb2JqCjUgMCBvYmoKPDwKL1BhZ2VNb2RlIC9Vc2VOb25lIC9QYWdlcyA3IDAgUiAvVHlwZSAvQ2F0YWxvZwo+PgplbmRvYmoKNiAwIG9iago8PAovQXV0aG9yIChhbm9ueW1vdXMpIC9DcmVhdGlvbkRhdGUgKEQ6MjAyMjA2MjUwMDI3MTktMDUnMDAnKSAvQ3JlYXRvciAoUmVwb3J0TGFiIFBERiBMaWJyYXJ5IC0gd3d3LnJlcG9ydGxhYi5jb20pIC9LZXl3b3JkcyAoKSAvTW9kRGF0ZSAoRDoyMDIyMDYyNTAwMjcxOS0wNScwMCcpIC9Qcm9kdWNlciAoUmVwb3J0TGFiIFBERiBMaWJyYXJ5IC0gd3d3LnJlcG9ydGxhYi5jb20pIAogIC9TdWJqZWN0ICh1bnNwZWNpZmllZCkgL1RpdGxlICh1bnRpdGxlZCkgL1RyYXBwZWQgL0ZhbHNlCj4+CmVuZG9iago3IDAgb2JqCjw8Ci9Db3VudCAxIC9LaWRzIFsgNCAwIFIgXSAvVHlwZSAvUGFnZXMKPj4KZW5kb2JqCjggMCBvYmoKPDwKL0ZpbHRlciBbIC9BU0NJSTg1RGVjb2RlIC9GbGF0ZURlY29kZSBdIC9MZW5ndGggMTc2MQo+PgpzdHJlYW0KR2IhO2Q5bG8mSSZBQDcubG5NNEYoXVhsKG0mQEYpNDNsS1xAT11QcURcKjRIWVhxWHA4XCouPWEqMSpaV2hsWDtWMjc3bmRKLSdPNXMyZi5EZytKTydML1xwKkc1QU0sPDNERl5jNzkiXmpQLlprU2hgOkR1UC4lZideSFdnQUw5NkRqR0hYMVBeSDk2VUQ+PSZyJzhuRCdJbC1MbmkuXT5YWk1DK3AlZT8lLFJSZy5TNWZHcjwvbFcocWs5ImpcdGJSPjpnRD4kSmwqTk1vP2w4VWI8cWNdVTZeWG1fKXUpUjUtNEpvKmtWUXBDVElvVV5XVjQjc1pAWj5QMiI0Tk51bmNnNE0nJC0xR104Tk89RDMjSCkxMmdlbTs0SyQkIWUrc2BdUzQhVmBxJUcndTJnMVM+M1VxY0c1PkAzW0FvUltYLSdMWFZqX1UzREJCcGNRTkxYX3FLQD9TaC8sWlVwPFBNPE1EMUFIWWlHTCkzKT9FUGxPck9fdUouInUpTiRbbTtfWHByaj5ScFh0RSp0Ui9EJS81Vko2RmotRFFfX0FaOF4xNUYpO0oxW0MsNVIjYnNLJVpQYElKQHMnaFFxIlVSV11Yaj9FQGZ1MGdJSUYqS0lQXSFtKShPYHFaLHBPRVQ7Qjc5J0BbNGdAU0puUToxTmorbEsrZUxzQVkhNE1IOjVGazo2RkJnI0w4Qy9eaSxhUGxwKyUpS1tTVkVsYjRWNUxVb0RTNSNkNGsoLVwsTSUjNDonY1ZvKTc0JGFzZWRdLSZpYko1S2luIilnR0UzRilXPylEVjw7RStMWDcuKk9KR1knT3JnJlIlXVlWPV5PSCQ9Xi0iRVc3ZTNcW1siLShaMnFGXi06dERjR3NwPmJ0L1RCbT0zMjJkNi87PiInQjxtUUctRSsubmxHUHNnJzdZUUxgYF5aT2ElRC5FTV9vIS9OR11JYGU5aGVFKypPQilNblM2PUFAXS9IJytGYjhfJFFxdGowS2V0RjI/UlBCNkMtLEYwalhQWXBOSSNFaD5xTWgmZHRQNUFNaFhYODhKSGtfWG5mWnRHZyNLJWFrX0I5VkdabG1rSlBdQzkmWDwiPEMhOHAzbUhoaiM3KlgvTDRcMExkMGwwI0UxVzs6JTJnXWhcMVk3ciN1MC1bU09nRl41LFYwKz8uREdWPS5HbCtTT29NQjVuUkVrNE8vL1pqcjE/TSQ9bjpDYyRISUBWc0g2cT5AIUo0Sk0/YSFoVk5tNipvRWBYTVBnVEE6Q3V0VzItWUJ1L1YjaS9JT0dcZjhkJG4ickYiKS5MV0xqW0hddD5HQ1dJYEwobTl0TXFcc0ozbmxoX2lEOCdlTTZgJFprcGonS19kOV9MSytCVkJlLzgpTlxUc1BWUTdGO1ZfTSNuSVolSi87NFNcayMqKjNZJUwmYGxIXU1IXE1oZXBCKkAyc29OX2NlQihpMCpHXlQoW1szLUtgKz5aNE1YOUlhXipJMG1aW0htOWMhKjMrPjpsMitpZFptYT43VTIla15SLEUiPElfT15yZUBuI0s/RzxSRmVPMmlralBmOCg4Kl80aEFXQj5oIkZqLFp0STU0c2NuRj5OWTItOis7P21XO1xMYTFvbSxgPlZVYWY/bmJkK2VHcipePUEickk3OkUib28mZSJGZWQpOVM1cHQyWVYnQz1mZSsnbm5JMTtncmQqLj9wMTpBdCg9QEAtLSdAWmJDckAnJTZqPS9YSzY9ayxwVVU/aVZHSiE1ZyI+I0g6Tl1GYyJRYEhcY0dINihkMDwyO0tbRjIuYEIqTzZHNUpmXDg+Xi88MDQ6bS5wLDsvJUAlRDFaYV5eblkmMidgSzRoJjteMmo5KUFGakdSREBAZUVCKDRhPWhaXGEoO00pSD9EJyZSMlNCRlsuXjghcUJQUGtBSXRKIzZMYy0/VlBLP1VdbWc2Vi4+JnA6JkIyNnRfUUQzKCk7bUMiYzBCOHJaNGlncSE5JyNXITg8VGNyNWtubVRFNStXbGNpLnVDSlgkMj04QGM8PFszVkNHOXBLMlwlQysnPnNwcTQna1ZiTypVMj5hSCIjOjUiayRAUWkza0tAMjIuWDUpMiQoQUFfVmJzRlx0KnBtZEk8Tkx1SWdnVTNNckxUbyVTbis+IlVGbCJKJmU+aWw0JS5dPyI9SS9ucyVoNmknJG5jZ2Y7SU0tQDtHITNfTzknMEF1ZWFYMSJLZyNLLiRGNTdrVTthQikjKFJSYV85PmldS3MuPDs1PjM2K0tCMk9KKkZeLixuQmk/NzlEdCVjXidoYlNUIWRtITI/bShTSjhtO0soaGpNPDN0VF1fTWZsVEx0K34+ZW5kc3RyZWFtCmVuZG9iagp4cmVmCjAgOQowMDAwMDAwMDAwIDY1NTM1IGYgCjAwMDAwMDAwNzMgMDAwMDAgbiAKMDAwMDAwMDExNCAwMDAwMCBuIAowMDAwMDAwMjIxIDAwMDAwIG4gCjAwMDAwMDAzMjkgMDAwMDAgbiAKMDAwMDAwMDUzMiAwMDAwMCBuIAowMDAwMDAwNjAwIDAwMDAwIG4gCjAwMDAwMDA4OTYgMDAwMDAgbiAKMDAwMDAwMDk1NSAwMDAwMCBuIAp0cmFpbGVyCjw8Ci9JRCAKWzw2ZTdkMDQzYjcxOWJhYzE4ZjYwMDVkOGUxMjM4N2E3MD48NmU3ZDA0M2I3MTliYWMxOGY2MDA1ZDhlMTIzODdhNzA+XQolIFJlcG9ydExhYiBnZW5lcmF0ZWQgUERGIGRvY3VtZW50IC0tIGRpZ2VzdCAoaHR0cDovL3d3dy5yZXBvcnRsYWIuY29tKQoKL0luZm8gNiAwIFIKL1Jvb3QgNSAwIFIKL1NpemUgOQo+PgpzdGFydHhyZWYKMjgwNwolJUVPRgo=",
    "statusCode": 200
}
```







