import time
from datetime import date
from datetime import timedelta
add_library('pdf')

title_start_x = 20
startDate_of_chart = date(2018, 6, 1)
endDate_of_chart = date(2018, 10, 1)


def setup():
    global delta, title_area_width, chart_area_width, rect_width_per_day, roboto12, roboto16
    size(1200, 400, P2D)
    smooth(128)
    title_area_width = width * 0.20
    chart_area_width = width * 0.75
    delta = abs(startDate_of_chart - endDate_of_chart)
    rect_width_per_day = chart_area_width / delta.days
    roboto12 = createFont("RobotoCondensed-Bold", 12)
    roboto16 = createFont("RobotoCondensed-Bold", 16)
    
     
def draw():
    beginRecord(PDF, "ganttChartTest.pdf")
    noLoop()
    
    textMode(SHAPE)
    background(255)
    currentX = title_area_width
    currentY = 120
    
    todayDelta = abs(startDate_of_chart - date.today())
    for i in range(delta.days + 1):
        strokeWeight(1)
        if i == todayDelta.days:
            stroke(255, 0, 0)
        else:
            stroke(228)
        x = i * rect_width_per_day + currentX
        line(x, 100, x, height - 100)

    # Draw Month headers based on date range
    draw_months(currentX, 50, rect_width_per_day, startDate_of_chart, endDate_of_chart)
    
    # Draw Year headers
    draw_years(currentX, 25, rect_width_per_day, startDate_of_chart, endDate_of_chart)
    
    # Draw Individual task rectangles and Title Information
    
    startDate = date(2018, 6, 14)
    startDate = drawTask(currentX, currentY, rect_width_per_day, startDate_of_chart, 
        startDate, 4, "Test")
    currentY = currentY + 25 # Increment Y-coordinate to draw next task rectangle
    startDate = drawTask(currentX, currentY, rect_width_per_day, startDate_of_chart, 
        startDate, 2, "Test")
    currentY = currentY + 25
    startDate = drawTask(currentX, currentY, rect_width_per_day, startDate_of_chart, 
        startDate, 9, "Test")
    currentY = currentY + 25
    startDate = drawTask(currentX, currentY, rect_width_per_day, startDate_of_chart, 
        startDate, 6, "Test")
    currentY = currentY + 25
    startDate = drawTask(currentX, currentY, rect_width_per_day, startDate_of_chart, 
        startDate, 12, "Test")
    
    endRecord()

def drawTask(startX, startY, rect_width_per_day, chart_start, task_start_date, task_duration_in_days, title):
    days_from_start = abs(chart_start - task_start_date)
    x = (days_from_start.days * rect_width_per_day) + startX
    width_of_rect = task_duration_in_days * rect_width_per_day
    fill(0, 255, 255)
    rect(x, startY, width_of_rect, 20)
    fill(0)
    textSize(12)
    textOffset = textWidth(title)
    textAlign(LEFT, CENTER)
    text(title, title_start_x, startY, textOffset + 10, 20)
    textSize(10)
    textOffset = textWidth(title)
    textAlign(RIGHT, CENTER)
    text(task_start_date.strftime("%m/%d"), x - textOffset, startY, textOffset - 4, 20)
    return task_start_date + timedelta(days=task_duration_in_days)



def draw_years(startX, startY, rect_width_per_day, start_date, end_date):
    currentX = startX
    currentY = startY
    rectHeight = 20
    padding = 2
        
    total_days = abs(start_date - end_date).days
    
    current = start_date
    
    while total_days > 0:
        if current.year == end_date.year:
            offset = end_date
        else:
            m = 1 if current_year < end_date.year else end_date.month
            y = current_year + 1 if current_year < end_date.year else current_year
            offset = date(y, m, 1)
            
        days_until_next_year = abs(current - offset)
        rectWidth = days_until_next_year.days * rect_width_per_day
        fill(200)
        rect(currentX + padding, currentY, rectWidth - padding, rectHeight)
        
        fill(255)
        noStroke()
        textFont(roboto12)
        textAlign(CENTER, CENTER)
        yearString = current.strftime("%Y")
        text(yearString, currentX, currentY, rectWidth, rectHeight)
        
        current = offset
        
        total_days = total_days - days_until_next_year.days
        currentX = currentX + rectWidth

def draw_months(startX, startY, rect_width_per_day, start_date, end_date):
    currentX = startX
    currentY = startY
    rectHeight = 30
    padding = 1
            
    delta = start_date - end_date
    total_days = abs(delta.days)
    
    current = start_date
        
    while total_days > 0:
        if current.month == end_date.month and current.year == end_date.year:
            offset = end_date
        else:
            m = 1 if current.month == 12 else current.month + 1
            y = current.year + 1 if current.month % 12 == 0 else current.year
            offset = date(y, m, 1)
        days_until_next_month = abs(current - offset)
        rectWidth = days_until_next_month.days * rect_width_per_day
        fill(150)
        rect(currentX + padding, currentY, rectWidth - padding, rectHeight)
        
        fill(255)
        noStroke()
        textFont(roboto16)
        textAlign(CENTER, CENTER)
        monthString = current.strftime("%b").upper()
        text(monthString, currentX, currentY, rectWidth, rectHeight)
        
        current = offset
      
        total_days = total_days - days_until_next_month.days
        currentX = currentX + rectWidth
        
