import calendar

class Calendar:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def get_calendar(self):
        cal = calendar.monthcalendar(self.year, self.month)
        return cal

    def print_calendar(self):
        cal = self.get_calendar()
        print(calendar.month_name[self.month], self.year)
        print("Mon  Tue  Wed  Thu  Fri  Sat  Sun")
        for week in cal:
            for day in week:
                if day == 0:
                    print("     ", end="")
                else:
                    print("{:2d}   ".format(day), end="")
            print()

# Example usage
cal = Calendar(2022, 1)
cal.print_calendar()