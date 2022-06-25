from re import template
import os

from reportlab.lib import colors, styles, styles
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, Image, Paragraph
from flask import Flask, request, jsonify
import traceback
import redis
import json
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm

from service.pdfgen import utils
import base64

bottomPaddingRemaining = 0
listOfRowsStyle = []
remainingRows = 0
pagebreak = False
pdfFonts = None


def getTemplate(body):
    fullName = body.get("fullName","")
    addressAndPhone = body.get("addressAndPhone","") 
    educationalDetails = body.get("educationalDetail","") 
    workExperience = body.get("workExperience","")
    projects = body.get("projects","")
    skills = body.get("skills","")
    hobbies = body.get("hobbies","")
    certificates = body.get("certificates","")
    extraCurricular = body.get("extraCurricular","")
    achievements = body.get("achievements","")



    template = {}
    template['rows'] = []        

    if fullName and addressAndPhone:
        template['rows'].append(utils.renderFirstName(fullName))
        template['rows'].append(utils.renderAddressAndPhone(addressAndPhone))
        template['rows'].append(utils.renderSpace())

    if educationalDetails:
        template['rows'].append(utils.renderHeading("Education"))
        for i in range(len(educationalDetails)):
            utils.renderEducationalDetails(template,educationalDetails,i)
        template['rows'].append(utils.renderSpace())

    if workExperience:
        template['rows'].append(utils.renderHeading("Experience"))
        for i in range(len(workExperience)):
            utils.renderWorkExperience(template,workExperience,i)
            # if i<len(workExperience)-1:
            #     template['rows'].append(utils.renderSpace())
            
        template['rows'].append(utils.renderSpace())

    if skills:
        template['rows'].append(utils.renderHeading("Skills"))
        for key,val in skills[0].items():
            template['rows'].append(utils.renderSkills(skills,key,val))
        template['rows'].append(utils.renderSpace())

    if projects:
        template['rows'].append(utils.renderHeading("Projects/Open Source"))
        for i in range(len(projects)):
            if i==len(projects)-1:

                utils.renderProjects(template,projects,i,some="abc")
            else:
                utils.renderProjects(template,projects,i)
        template['rows'].append(utils.renderSpace())

    if certificates:
        template['rows'].append(utils.renderHeading("Certificates"))
        for i in range(len(certificates)):

            utils.renderHobbies(template,certificates,i,some="abc")
        template['rows'].append(utils.renderSpace())

    if hobbies:
        template['rows'].append(utils.renderHeading("Hobbies"))
        for i in range(len(hobbies)):
            utils.renderHobbies(template,hobbies,i,"abc")
        template['rows'].append(utils.renderSpace())

    if extraCurricular:
        template['rows'].append(utils.renderHeading("Extra Curricular"))
        for i in range(len(extraCurricular)):
            utils.renderHobbies(template,extraCurricular,i)
        template['rows'].append(utils.renderSpace())

    if achievements:
        template['rows'].append(utils.renderHeading("Achievements"))
        for i in range(len(achievements)):
            utils.renderHobbies(template,achievements,i)
        template['rows'].append(utils.renderSpace())

    return template



def generatePdff(body):
    template = getTemplate(body)
    global pagebreak

    if not template['rows']:
        fileName = "emptypdf" + ".pdf"
        pdf = canvas.Canvas(fileName, pagesize=A4)
        pdfWidth, pdfHeight = A4
        pdf.showPage()
        pdf.save()
        with open("emptypdf.pdf", "rb") as pdf_file:
            encoded_string = base64.b64encode(pdf_file.read())
            data =str(encoded_string, 'utf-8')
        
        os.remove("emptypdf.pdf")

        
        statusCode = 200
        return jsonify(statusCode=statusCode,data=data)


    topMarginData = {
        "height": 2,
        "styles": {
            "font": "Times",
            "fontSize": 1
        },
        "columns": [
            {
            "format": "text",
            "data": "",
            "width": 100
            }
        ]
        }



    try:
        fullName = body.get('fullName',"a")
        fileName = fullName + ".pdf"
        pdf = canvas.Canvas(fileName, pagesize=A4)
        pdfWidth, pdfHeight = A4

        print(f"pdfWidth:{pdfWidth}")
        print(f"pdfHeight:{pdfHeight}")

        pdfWidthList = [
            pdfWidth * 95 / 100
        ]

        heightList = []
        for rowHeight in template['rows']:
            heightPercentage = rowHeight['height']
            heightList.append(
                pdfHeight * heightPercentage / 100
            )

        originalRows = len(template['rows'])
        index = 0
        pagebreak = True
        while pagebreak:
            listOfRowsTable = []
            print(f"Page Break Check:=>{pagebreak}")
            print(f"Original Rows:=> {originalRows}")
            print(f"remainingRows:=> {remainingRows}")

            temp = originalRows - remainingRows
            if index >= 1:
                    temp = temp + 2

            print(f"Temp :=>{temp}")

            templateRows = template['rows']

            if index == 0:

                # print(f"templateRows Before {index}:=>{templateRows}\n\n\n")

                # templateRows.insert(0, topMarginData)
                heightList.insert(0, 50)

                # print(f"templateRows After {index}:=>{templateRows}")
                data = generateRowsTable(pdfWidthList[0], heightList, templateRows, pdfHeight, pdf)
            else:
                temp-=1
                newRows=templateRows[temp:]
                newHeightList=heightList[temp:]

                newRows.insert(0, topMarginData)
                newHeightList.insert(0, 50)

                data = generateRowsTable(pdfWidthList[0], newHeightList, newRows, pdfHeight, pdf)

            print(f"### Final Bottom Padding Remaining ==>{bottomPaddingRemaining} for Page {index}")
            # print(f"listOfRowsTable :=>{data}")
            if data:
                listOfRowsTable.append(data)
                mainTable = Table([
                    listOfRowsTable
                ],
                    colWidths=pdfWidthList,
                    rowHeights=pdfHeight
                )

                mainTable.setStyle(listOfRowsStyle)
                mainTable.wrapOn(pdf, 0, 0)
                mainTable.drawOn(pdf, 0, 0)
                pdf.showPage()
            else:
                break

            index += 1

        pdf.save()
        # data=""
        print(type(pdf))
        with open(f"{fullName}.pdf", "rb") as pdf_file:
            encoded_string = base64.b64encode(pdf_file.read())
            data =str(encoded_string, 'utf-8')
        
        os.remove(f"{fullName}.pdf")

        
        statusCode = 200

    except:
        data=""
        print("Error Occured ")
        traceback.print_exc()
        statusCode = 205
    
    

    return jsonify(data=data,statusCode=statusCode)






def generateMultiTextTable(width, height, data):
    heightPercentage = data['height']
    rowHeight = height * heightPercentage / 100

    listOfMultiTextData = []
    listOfMultiTextStyle = []

    listOfMultiTextData.append(data['value'])

    multiTextTable = Table([
        listOfMultiTextData
    ], width, rowHeight)

    multiTextTable.setStyle(listOfMultiTextStyle)
    return multiTextTable

def generateVerticleTable(colWidth, rowHeight, data, result):
    colWidthList = [
        colWidth * 10 / 100,
        colWidth * 90 / 100
    ]
    # print(f"Checked Width Before : =>{colWidthList}")
    if colWidthList[0] >= 10:
        colWidthList[0] = 10

    # print(f"Checked Width After : =>{colWidthList}")

    listOfveriticalTable = []
    if result:
        listOfveriticalTable.append(
            Image("resources/checkedbox.png", width=0.2 * inch, height=0.1 * inch, kind="proportional"))
    else:
        listOfveriticalTable.append(
            Image("resources/unchecked.png", width=0.2 * inch, height=0.1 * inch, kind="proportional"))

    listOfveriticalTable.append(Paragraph(data, None))

    verticaltable = Table([
        listOfveriticalTable
    ], colWidthList, rowHeight)

    # print(f"verticaltable :=>{verticaltable}")

    return verticaltable


def generateHorizontalTable(colWidth, rowHeight, data):
    heightPercentage = rowHeight * 50 / 100
    # print(f"Label Style heightPercentage :=>{heightPercentage}")

    listOfHorizontalTable = []
    listOfHorizontalStyle = []

    listOfHorizontalTable.append(data['value'])

    horizontalTable = Table([
        listOfHorizontalTable
    ], colWidth, heightPercentage)

    return horizontalTable

def createTopMargin(pdfWidth):
    listOfColsData = []
    data = "Random"
    listOfColsData.append(data)

    columnTable = Table([
        listOfColsData
    ], pdfWidth, 200)

    return columnTable

def generateNestedTableRows(data, width, heightList, pdf):
    listOfNestedRowsTable = []
    noOfRows = 0

    for row in data:
        # print(f"##### Generating Number Of Nested Rows #####{noOfRows}")
        columnStyle = None
        if 'columnStyle' in row:
            columnStyle = row['columnStyle']

        columnTable = generateColumnsTable(width, heightList[noOfRows], row['columns'], columnStyle, row, pdf)
        listOfNestedRowsTable.append(columnTable)
        noOfRows += 1

    return listOfNestedRowsTable


def generateColumnsTable(pdfWidth, rowHeight, cols, columnStyle, row, pdf):
    listOfColsStyle = []
    global pdfFonts
    if 'styles' in row:
        styles = row['styles']
        if 'border' in styles:
            border = styles['border']
            listOfColsStyle.append(
                ('GRID', (0, 0), (-1, -1), 0, "Black"),
            )

        if 'leftPadding' in styles:
            leftPadding = styles['leftPadding']
            listOfColsStyle.append(
                ('LEFTPADDING', (0, 0), (-1, -1), leftPadding),
            )

        if 'rightPadding' in styles:
            rightPadding = styles['rightPadding']
            listOfColsStyle.append(
                ('RIGHTPADDING', (0, 0), (-1, -1), rightPadding),
            )

        if 'bgcolor' in styles:
            bgColor = styles['bgcolor']
            listOfColsStyle.append(
                ('BACKGROUND', (0, 0), (-1, 0), bgColor),
            )

        if 'fontColor' in styles:
            fontColor = styles['fontColor']
            listOfColsStyle.append(
                ('TEXTCOLOR', (0, 0), (-1, 0), fontColor),
            )

        if 'lineBelow' in styles:
            lineBelow = styles['lineBelow']
            listOfColsStyle.append(
                ('LINEBELOW', (0, 0), (-1, 0), 1, colors.HexColor('#000000')),
            )

        if 'bold' in styles:
            bold = styles['bold']
            listOfColsStyle.append(
                ('FONTNAME', (0, 0), (-1, -1), 'Times-Bold'),
            )

        if 'fontStyle' in styles:
            font = styles['fontStyle']
            listOfColsStyle.append(
                ('FONTNAME', (0, 0), (-1, -1), 'Times-Italic'),
            )

        if 'fontStyle' in styles and 'bold' in styles:
            font = styles['fontStyle']
            bold = styles['bold']
            listOfColsStyle.append(
                ('FONTNAME', (0, 0), (-1, -1), 'Times-BoldItalic'),
            )

    widthList = []
    listOfColsData = []

    for colWdith in cols:
        widthPercentage = colWdith['width']
        colWidth = pdfWidth * widthPercentage / 100
        widthList.append(colWidth)

    checked = u'\u2713'
    unchecked = u'\u2715'

    index = 0
    for col in cols:
        format = col['format']

        if 'align' in col:
            alignment = col['align']
            # print(f"alignment:=>{alignment}")
            if alignment == "center":
                listOfColsStyle.append(
                    ('ALIGN', (0, index), (0, index), 'CENTER'),
                )

        if format == "Image":
            pdfLogo = Image(col['data'], widthList[index], rowHeight, kind="proportional")
            listOfColsData.append(pdfLogo)

        if format == "MultiText":
            multiTextIndex = 1
            multiTextList = []
            for data in col['data']:
                print(f"###### Generating MultiText ### {multiTextIndex}")
                multiTextTable = generateMultiTextTable(colWidth, rowHeight, data)
                multiTextList.append(multiTextTable)
                multiTextIndex += 1
            listOfColsData.append(multiTextList)

        if format == "text":
            data = col['data']
            listOfColsData.append(data)

        if format == "Para":
            data = col['data']
            listOfColsData.append(Paragraph(data, None))

        if format == "Checked":
            if col['checked'] == 1:
                data = generateVerticleTable(colWidth, rowHeight, col['data'], True)
                listOfColsData.append(data)

            elif col['checked'] == 0:
                data = generateVerticleTable(colWidth, rowHeight, col['data'], False)
                listOfColsData.append(data)

        labelData = []
        if format == "Label":
            if columnStyle == 1:
                for data in col['data']:
                    data = generateHorizontalTable(colWidth, rowHeight, data)
                    labelData.append(data)
                listOfColsData.append(labelData)

        if format == "table":
            # print(f"rowHeight: {rowHeight}")
            # print(f"data: {col['data']}")
            # print(f"width: {widthList[index]}")

            heightList = []
            for rowHeights in col['data']:
                heightPercentage = rowHeights['height']
                heightList.append(
                    rowHeight * heightPercentage / 100
                )
            # print(f"Height List:{heightList}")
            data = generateNestedTableRows(col['data'], widthList[index], heightList, pdf)
            # listOfColsStyle.append(
            #     ('BOTTOMPADDING', (0, 0), (-1, -1), 50)
            # )
            listOfColsData.append(data)

        if format == "Signature":
            pdfmetrics.registerFont(TTFont('DS', 'resources/DancingScript-Medium.ttf'))
            # pdf.setFont('Times-Italic', 12)
            # print(f"Available Fonts =>{pdf.getAvailableFonts()}")
            listOfColsData.append(col['data'])

        index += 1

    # print(f"listOfColsData: {listOfColsData}")
    columnTable = Table([
        listOfColsData
    ], widthList, rowHeight)

    # print(f"listOfColsStyle===>{listOfColsStyle}")

    columnTable.setStyle(listOfColsStyle)
    return columnTable

def generateRowsTable(pdfWidth, heightList, rows, pdfHeight, pdf):
    listOfRowsTable = []
    global listOfRowsStyle
    global pagebreak
    global remainingRows
    global bottomPaddingRemaining

    totalNumberOfRows = len(rows)
    print(f"###Total Rows:=>\n {totalNumberOfRows}")
    # print(f"### Current Rows Data:=>\n {rows}")

    if (totalNumberOfRows <= 0):
        pagebreak = False
        return listOfRowsTable

    # print(f"listOfRowsTable:=>{listOfRowsTable}")

    noOfRows = 0
    for row in rows:
        # print(f"##### Generating number OF Rows #####{noOfRows}")
        # print(f"{row['columns']}")
        columnStyle = None
        if 'columnStyle' in row:
            columnStyle = row['columnStyle']

        if noOfRows == 0:
            previousBottompadding = pdfHeight
        else:
            previousBottompadding = bottomPaddingRemaining

        # print(f"height of Each Row:=> {heightList[noOfRows]}")
        # print(f"Last Bottom Padding:=> {previousBottompadding}")
        # print(f"bottomPaddingRemaining After Each Row:=> {bottomPaddingRemaining}")

        if previousBottompadding < heightList[noOfRows]:
            pagebreak = True
            remainingRows = totalNumberOfRows - (noOfRows - 1)
            break
        else:
            pagebreak = False

        bottomPaddingRemaining = pdfHeight - heightList[noOfRows]
        pdfHeight = bottomPaddingRemaining

        columnTable = generateColumnsTable(pdfWidth, heightList[noOfRows], row['columns'], columnStyle, row, pdf)
        listOfRowsTable.append(columnTable)

        noOfRows += 1

    listOfRowsStyle.append(
        ('BOTTOMPADDING', (0, 0), (-1, -1), bottomPaddingRemaining),
    )
    # print(f"remainingRows: {remainingRows}")
    return listOfRowsTable
