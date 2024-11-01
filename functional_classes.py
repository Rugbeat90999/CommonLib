import datetime

class staticproperty:
  def __init__(self, func):
    self.func = func

  def __get__(self, instance, owner):
    return self.func(owner)


class staticstr(type):
  def __str__(cls):
    return cls.__str__()
  



class Calculator:
  class Time:
    @staticmethod
    def to_seconds(years:int=0, days:int=0, hours:int=0, minutes:int=0, seconds:int=0) -> int:
      if seconds < 0 or minutes < 0 or hours < 0 or days < 0 or years < 0:
        raise ValueError("Invalid time value")
      seconds_total = seconds
      minutes_total = minutes * 60 + seconds_total
      hours_total = hours * 3600 + minutes_total
      days_total = days * 86400 + hours_total
      years_total = years * 31536000 + days_total
      return years_total
    

    @staticmethod
    def from_seconds(seconds:int) -> tuple[int, int, int, int, int]:
      if seconds < 0:
        raise ValueError("Invalid time value")
      years = seconds // 31536000
      seconds %= 31536000
      days = seconds // 86400
      seconds %= 86400
      hours = seconds // 3600
      seconds %= 3600
      minutes = seconds // 60
      seconds %= 60
      return years, days, hours, minutes, seconds


    @staticmethod
    def days_to_months(days:int) -> int:
      if days < 0:
        raise ValueError("Invalid time value")
      months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
      months_past = 0

      for month in months:
        if days < month:
          break
        
        months_past += 1
        days -= month

      return months_past


    @staticmethod
    def months_to_days(months:int) -> int:
      if months < 0:
        raise ValueError("Invalid time value")
      days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

      total_days = 0
      for index in range(months):
        total_days += days_per_month[index]
      
      return total_days
    

    @staticmethod
    def age_finder(begining_date:datetime.datetime, end_date:datetime.datetime):
      bd = Calculator.Time.date_converter(begining_date)
      ed = Calculator.Time.date_converter(end_date)

      age = Calculator.Time.to_seconds(ed[0], ed[1], ed[2], ed[3], ed[4]) - Calculator.Time.to_seconds(bd[0], bd[1], bd[2], bd[3], bd[4])

      return Calculator.Time.from_seconds(age)


    @staticmethod
    def date_converter(date:datetime.datetime, want_months:bool=False) -> tuple[int,int,int,int,int] | tuple[int,int,int,int,int,int]:
      '''Converts a date to a tuple formated as (years, days, hours, minutes, seconds), and optionally months inbetween years and days.'''
      str_date = str(date).split(".")[0].split(" ")

      years = int(str_date[0].split("-")[0])
      months = int(str_date[0].split("-")[1])
      days = int(str_date[0].split("-")[2])

      hours = int(str_date[1].split(":")[0])
      minutes = int(str_date[1].split(":")[1])
      seconds = int(str_date[1].split(":")[2])

      if want_months:
        return (years, months, days, hours, minutes, seconds)

      days += Calculator.Time.months_to_days(months)
      return (years, days, hours, minutes, seconds)