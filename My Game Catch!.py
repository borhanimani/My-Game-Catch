from tkinter import *

# Making Screen
dateConvertor = Tk()
dateConvertor.title("Date Convertor")
dateConvertor.geometry("600x500+300+150")
dateConvertor.configure(bg = "light green" )
    
# Variables
day = StringVar()
month = StringVar()
weekDay = StringVar()
waitedDays = StringVar()
expectedDay = StringVar()
expectedMonth = StringVar()
expectedWeekDay = StringVar()
numberOfMonths = 0
numberOfDaysleft = 0
weekNumber = 0
expectedWeekDaysNumber = 0
weekDays = {"Saturday":0 , "Sunday":1 , "Monday":2 , "Tuesday": 3 , "Wednesday":4 , "Thursday":5 , "Friday":6}
weekDaysInNumber = {0:"Saturday" , 1:"Sunday" , 2:"Monday" , 3:"Tuesday" , 4:"Wednesday" , 5:"Thursday" , 6:"Friday"}

# Function
def run():
    if int(month.get()) <= 12: 
        if int(month.get()) <= 6:
            numberOfMonths = int(waitedDays.get())// 31
            numberOfDaysleft = int(waitedDays.get()) % 31
        elif int(month.get()) > 6:
            numberOfMonths = int(waitedDays.get()) // 30
            numberOfDaysleft = int(waitedDays.get()) % 30
    else:
        warningLabel = Label(dateConvertor,text ="Month Is Not Value",fg="red").place(x=150,y=450)
        
    expectedDay.set(int(day.get()) + numberOfDaysleft)
    expectedMonth.set( int(month.get()) + numberOfMonths)
    weekNumber = weekDays[weekDay.get()]    
    expectedWeekDaysNumber = (int(waitedDays.get())+weekDays[weekDay.get()])%7
    expectedWeekDay.set(weekDaysInNumber[expectedWeekDaysNumber])
    
# GUI
# Labels
dayLabel = Label(dateConvertor,text = "Day" , bg = "light green" , ).place(x = 80 , y = 100)
monthLabel = Label(dateConvertor,text = "Month" , bg = "light green" , ).place(x = 80 , y = 220)
weekDayLabel = Label(dateConvertor,text = "Week Day" , bg = "light green" , ).place(x = 80 , y = 340)
waitedDaysLabel = Label(dateConvertor,text = "Number of Days" , bg = "light green" , ).place(x = 240 , y = 230)
expectedDayLabel = Label(dateConvertor,text = "Day" , bg = "light green" , ).place(x = 390 , y = 100)
expectedMonthLable = Label(dateConvertor,text = "Month" , bg = "light green" , ).place(x = 390 , y = 220)
expectedWeekDayLabel = Label(dateConvertor,text = "Week Day" , bg = "light green" , ).place(x = 390 , y = 340)

# Entries
dayEntry = Entry(dateConvertor,textvariable = day).place(x = 80 , y = 130)
monthEntry = Entry(dateConvertor,textvariable = month).place(x = 80 , y = 250)
weekDayEntry = Entry(dateConvertor,textvariable = weekDay).place(x = 80 , y = 360)
waitedDaysEntry = Entry(dateConvertor,textvariable = waitedDays).place(x = 240 , y = 255)
convertButton = Button(dateConvertor,text="Run",command=run).place(x = 270 , y = 280)
expectedDayEntry = Entry(dateConvertor,textvariable = expectedDay).place(x = 390 , y = 130)
expectedMonthEntry = Entry(dateConvertor,textvariable = expectedMonth).place(x = 390 , y = 250)
expectedWeekDayEntry = Entry(dateConvertor,textvariable = expectedWeekDay).place(x = 390 , y = 360)
dateConvertor.mainloop()
