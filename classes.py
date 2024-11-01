import datetime
import random
import os




class Direction:
  Up = b"Up"
  Right = b"Right"
  Down = b"Down"
  Left = b"Left"
  Still = b"Still"
  Forward = b"Forward"
  Backward = b"Backward"




class UUIDError(BaseException):
  def __init__(self, message):
    print(f"UUIDError: {message}")


class NotUniqueUUIDError(UUIDError):
  def __init__(self, message):
    print(f"NotUniqueUUIDError: {message}")
  



class Coord():
  '''
  used to define x, y, and z coordinets.
  '''
  def __init__(self, x:int=0, y:int=0, z:int=None, coord_type:int=2):
    if coord_type >= 1:
      self.x = x
      self.pos = (x,)
    if coord_type >= 2:
      self.y = y
      self.pos = (x, y)
    if coord_type == 3:
      self.z = z
      self.pos = (x, y ,z)
    if 1 < coord_type > 3:
      raise ValueError(f"type must be 1, 2, or 3, not {coord_type}") 


  def __str__(self) -> str:
    return f"{self.pos}"
  
  def __repr__(self) -> str:
    return f"CordValue={self.pos}"




class UUID:
  compares = 0
  def __init__(self, uuid:str=None) -> None:
    self.__generated = False
    if uuid == None:
      self.__generated = True
      self.__uuid = ""
      for _ in range(8):
        self.__uuid += Base16.rand_digit_base_16()
      self.__uuid += "-"
      for _ in range(3):
        for _ in range(4):
          self.__uuid += Base16.rand_digit_base_16()
        self.__uuid += "-"
      for _ in range(12):
        self.__uuid += Base16.rand_digit_base_16()
    else:
      uuid = uuid.lower().split("-")
      if uuid.__len__() != 5:
        raise ValueError(f"Invalid UUID input string")
      if uuid[0].__len__() != 8:
        raise ValueError(f"Invalid UUID input string")
      if uuid[1].__len__() != 4:
        raise ValueError(f"Invalid UUID input string")
      if uuid[2].__len__() != 4:
        raise ValueError(f"Invalid UUID input string")
      if uuid[3].__len__() != 4:
        raise ValueError(f"Invalid UUID input string")
      if uuid[4].__len__() != 12:
        raise ValueError(f"Invalid UUID input string")
      for x in uuid:
        for (y) in x:
          if not str(y).isalnum():
            raise ValueError(f"Invalid UUID input string")
          if str(y).isalpha():
            try:
              Base16.from_base(y)
            except:
              raise ValueError(f"Invalid UUID input string")

      self.__uuid = "-".join(uuid)
  
  @property
  def generated(self) -> bool:
    return self.__generated

  @property
  def uuid(self) -> str:
    return self.__uuid
  
  @property
  def alphabetic_version(self) -> str:
    letters = ""
    for i in self.__uuid:
      i = str(i)
      match i:
        case "0":
          letters += "a"
        case "1":
          letters += "b"
        case "2":
          letters += "c"
        case "3":
          letters += "d"
        case "4":
          letters += "e"
        case "5":
          letters += "f"
        case "6":
          letters += "g"
        case "7":
          letters += "h"
        case "8":
          letters += "i"
        case "9":
          letters += "j"
        case "a":
          letters += "k"
        case "b":
          letters += "l"
        case "c":
          letters += "m"
        case "d":
          letters += "n"
        case "e":
          letters += "o"
        case "f":
          letters += "p"
        case "-":
          letters += "q"
        case _:
          letters += "z"
    return letters


  def __str__(self) -> str:
    return self.__uuid

  def __eq__(self, other:"UUID") -> bool:
    return self.__uuid == other.uuid
  
  def __ne__(self, other:"UUID") -> bool:
    return self.__uuid != other.uuid
  

  def compare(self, other:"UUID"):
    UUID.compares += 1
    if self == other:
      if self.generated and other.generated:
        raise NotUniqueUUIDError(f"this is litteral a {UUID.compares} in 340,282,370,000,000,000,000,000,000,000,000,000,000 chance of happening. Congradulations you are either the luckiest or unluckiest person in all of existance.")
      raise NotUniqueUUIDError("UUID is not unique")
  
  


  

class Base16:
  def to_base(digit:int):
    if digit > 9:
      match digit:
        case 10:
          num = "a"
        case 11:
          num = "b"
        case 12:
          num = "c"
        case 13:
          num = "d"
        case 14:
          num = "e"
        case 15:
          num = "f"
        case _:
          raise ValueError("Can only be from 0 - 15")
    else:
      num = f"{digit}"
    
    return num
  

  def from_base(digit:str):
    try:
      num = int(digit)
    except ValueError:
      match digit:
        case "a":
          num = 10
        case "b":
          num = 11
        case "c":
          num = 12
        case "d":
          num = 13
        case "e":
          num = 14
        case "f":
          num = 15
        case _:
          print(f"\n\n\n\n\n\n\n\n{digit}\n\n\n\n\n\n\n\n\n\n\n")
          raise ValueError("This digit is not base 16")

    return num


  def rand_digit_base_16():
    return Base16.to_base(random.randint(0,15))




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




class Path:
  def __init__(self, path:str):
    self.path = path
    self.__is_directory_valid = os.path.isdir(path)
    self.__is_file_valid = os.path.isfile(path)
    if not self.__is_directory_valid and not self.__is_file_valid:
      raise ValueError(f"Invalid path: {path}")
    if self.__is_file_valid:
      self.file_name = os.path.basename(path)
      self.file_extension = os.path.splitext(path)[1]
    if self.__is_directory_valid and not self.__is_file_valid:
      self.directory = os.path.dirname(path)
      self.files_in_directory = os.listdir(path)


  @property
  def is_file(self) -> bool:
    return self.__is_file_valid
  @property
  def is_directory(self) -> bool:
    return self.__is_directory_valid


  def __str__(self) -> str:
    if self.__is_file_valid:
      return f'''This path is a file
path:{self.path}
file_name:{self.file_name}
file_extension:{self.file_extension}'''
    else:
      return f'''This path is a directory
path:{self.path}
directory:{self.directory}
files_in_directroy:{self.files_in_directory}'''




class staticproperty:
  def __init__(self, func):
    self.func = func

  def __get__(self, instance, owner):
    return self.func(owner)


class staticstr(type):
  def __str__(cls):
    return cls.__str__()