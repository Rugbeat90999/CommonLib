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
  def uuid(self) -> "UUID":
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
  
  # def __format__(self, format_spec:str="string"):
  #   '''
  #   Options:\n
  #   \"string\": returns a string of the UUID\n
  #   \"alphabetic\": returns a string of the UUID in alphabetic form\n
  #   '''
  #   if format_spec == "string":
  #     return self.__uuid
  #   if format_spec == "alphabetic":
  #     return self.alphabetic_version

  def __eq__(self, other:"UUID") -> bool:
    if not isinstance(other, UUID):
      raise ValueError(f"UUID can only be compaired to UUID not {type(other)}")
    return self.__uuid == other.uuid
  
  def __ne__(self, other:"UUID") -> bool:
    if not isinstance(other, UUID):
      raise ValueError(f"UUID can only be compaired to UUID not {type(other)}")
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




class Path:
  def __init__(self, path:str):
    self.path = path
    self.__is_directory_valid = os.path.isdir(path)
    self.__is_file_valid = os.path.isfile(path)
    if not self.__is_directory_valid and not self.__is_file_valid:
      raise ValueError(f"Invalid path: {path}")


  @property
  def is_file(self) -> bool:
    return self.__is_file_valid

  @property
  def is_directory(self) -> bool:
    return self.__is_directory_valid

  @property
  def file_name(self) -> str:
    if self.is_directory:
      raise FileNotFoundError("this is a directory not a file")
    return os.path.basename(self.path)
  
  @property
  def base_file_name(self) -> str:
    if self.is_directory:
      raise FileNotFoundError("this is a directory not a file")
    base = os.path.basename(self.path).split(".")
    base.pop()
    return ".".join(base)

  @property
  def file_extension(self) -> str:
    if self.is_directory:
      raise FileNotFoundError("this is a directory not a file")
    return os.path.splitext(self.path)[1]

  @property
  def files_in_directory(self) -> list["Path"]:
    if self.is_file:
      raise NotADirectoryError("this is a file not a directory")
    paths = []
    for name in os.listdir(self.path):
      paths.append(Path(f"{self.path}/{name}"))
    return paths
  
  @property
  def directory(self) -> str:
    if self.is_file:
      raise NotADirectoryError("this is a file not a directory")
    return os.path.dirname(self.path)
  

  @property
  def file_name(self) -> str:
    if self.is_directory:
      raise FileNotFoundError("this is a directory not a file")
    return os.path.basename(self.path)
  
  @property
  def base_file_name(self) -> str:
    if self.is_directory:
      raise FileNotFoundError("this is a directory not a file")
    base = os.path.basename(self.path).split(".")
    base.pop()
    return ".".join(base)

  @property
  def file_extension(self) -> str:
    if self.is_directory:
      raise FileNotFoundError("this is a directory not a file")
    return os.path.splitext(self.path)[1]

  @property
  def files_in_directory(self) -> list["Path"]:
    if self.is_file:
      raise NotADirectoryError("this is a file not a directory")
    paths = []
    for name in os.listdir(self.path):
      paths.append(Path(f"{self.path}/{name}"))
    return paths
  
  @property
  def directory(self) -> str:
    if self.is_file:
      raise NotADirectoryError("this is a file not a directory")
    return os.path.dirname(self.path)
  

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
files_in_directroy:{os.listdir(self.path)}'''




class OutputColors:
  def __init__(self, font: str | int = "default", color: str | int = "default", background: str | int = "default"):
    match font:
      case "default" | 0:
        self.font = 0
      case "bold" | 1:
        self.font = 1
      case "faded" | 2:
        self.font = 2
      case "italic" | 3:
        self.font = 3
      case "underline" | 4:
        self.font = 4
      case "blink" | 5:
        self.font = 5
      case "negative" | 6:
        self.font = 6
      case "reverse" | 7:
        self.font = 7
      case "invisible" | 8:
        self.font = 8
      case "strike" | "strike_through" | 9:
        self.font = 9
      case _:
        raise ValueError(f"Invalid font: {font}")
    
    match color:
      case "dark_gray" | "dark" | "dark_grey" | 0:
        self.color = 30
      case "red" | 1:
        self.color = 31
      case "green" | 2:
        self.color = 32
      case "yellow" | 3:
        self.color = 33
      case "blue" | 4:
        self.color = 34
      case "magenta" | 5:
        self.color = 35
      case "cyan" | 6:
        self.color = 36
      case "white" | 7:
        self.color = 37
      case "default" | 9 | 8:
        self.color = 39
      case _:
        raise ValueError(f"Invalid color: {color}")
    
    match background:
      case "black" | 0:
        self.background = 40
      case "red" | 1:
        self.background = 41
      case "green" | 2:
        self.background = 42
      case "yellow" | 3:
        self.background = 43
      case "blue" | 4:
        self.background = 44
      case "magenta" | 5:
        self.background = 45
      case "cyan" | 6:
        self.background = 46
      case "white" | 7:
        self.background = 47
      case "default" | 9 | 8:
        self.background = 49
      case _:
        raise ValueError(f"Invalid background: {background}")
  
  def __str__(self):
    return f"\033[{self.font};{self.color};{self.background}m"
  
  def __format__(self, format_spec):
    return self.__str__()




class debase_float:
  def __init__(self, num: float):
    self.__num = num
    split_number = str(num).split(".")

    float_amount = "0"
    try:
      for _ in split_number[1]:
        float_amount += "0"
      float_amount = "1" + float_amount
    except:
      pass


    all_numerals = "".join(split_number)


    translated_number = ""
    for i in all_numerals:
      match i:
        case "0":
          translated_number = "" + translated_number
        case "1":
          translated_number = "" + translated_number
        case "2":
          translated_number = "" + translated_number
        case "3":
          translated_number = "" + translated_number
        case "4":
          translated_number = "" + translated_number
        case "5":
          translated_number = "" + translated_number
        case "6":
          translated_number = "" + translated_number
        case "7":
          translated_number = "" + translated_number
        case "8":
          translated_number = "" + translated_number
        case "9":
          translated_number = "" + translated_number
    
      
    self.__display = translated_number[1:]
    if float(float_amount) > 0:
      self.__display = translated_number[:1] + "" + self.__display

  def __str__(self) -> str:
    return f"{self.__display}"
  
  def __float__(self) -> float:
    return float(self.__num)
  
  def __add__(self, other: "debase_float") -> "debase_float":
    return debase_float(self.__num + float(other))
  
  def __sub__(self, other: "debase_float") -> "debase_float":
    return debase_float(self.__num - float(other))
  
  def __mul__(self, other: "debase_float") -> "debase_float":
    return debase_float(self.__num * float(other))
  
  def __truediv__(self, other: "debase_float") -> "debase_float":
    return self.__num / float(other)
  
  def __floordiv__(self, other: "debase_float") -> "debase_float":
    return debase_float(self.__num // float(other))



