from CommonLib.classes import Path
import random
import json
import os




def common_ave(from_int:int, to_int:int, increase:int=1, print_list:bool=False) -> int:
  '''
  Returns an int betwean the two provided values, with it weighted to the center number.
  '''

  if from_int > to_int:
    raise ValueError("from_int must be smaller than to_int")
  
  base_list = []
  output_list = []
  cur_int = from_int
  while cur_int <= to_int:
    base_list.append(round(cur_int, 3))
    cur_int += 1
  
  middle = base_list.__len__()/2-1
  cur_ind = 0
  iteration = 0

  if iteration <= middle:
    output_list.append(base_list[cur_ind])
    cur_ind += 1
    iteration += 1


  while iteration <= middle:
    for _ in range(increase):
      output_list.append(base_list[cur_ind])
    cur_ind += 1
    increase += increase
    iteration += 1

  if base_list.__len__()%2 == 0:
    iteration -= 1
    increase = int(increase/2)

  while iteration >= 0:
    for _ in range(increase):
      output_list.append(base_list[cur_ind])
    cur_ind += 1
    increase = int(increase/2)
    iteration -= 1
  
  while output_list[output_list.__len__()-1] == output_list[output_list.__len__()-2]:
    output_list.pop()
  
  if print_list:
    print(output_list)
  
  return random.choice(output_list)




def hex_to_rgb(hex_code:str):
  return tuple(int(hex_code.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))




def rgb_to_hex(rgb:tuple[int,int,int]):
  return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])




def read_json(path:Path) -> dict:
  if not path.is_file:
    raise IsADirectoryError(f"{path.path} must be a file not a dirctory")
  if path.file_extension != '.json':
    raise ValueError(f"{path} must be a \".json\" file but instead got {path.file_extension}")
  with open(path.path, 'r') as file:
    return json.load(file)
  



def lines_cleaner(lines:list):
  for line in lines:
    lines[lines.index(line)] = line.rstrip("\n")
  return lines


def py_image(path:str):
  import pygame
  def do(path:str) -> pygame.Surface:
    if not os.path.isfile(path):
      raise FileNotFoundError("Requires a path to a file, but no file was found")
    return pygame.image.load(path).convert_alpha()
  return do(path)


def log(message: str):
  with open('log.txt', 'a') as file:
    file.write(f"{message}\n")
  print(message)