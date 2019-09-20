import os
import json

cache_dir = ".cache/"

def create_cache_file(filename):
     os_dir = os.path.dirname(filename)
     if not os.path.exists(os_dir):
          os.makedirs(os_dir)

     cache_file = open(filename, 'a+')
     cache_file.close()

def read_cachefile(filename):
     filename = cache_dir + filename
     create_cache_file(filename)

     with open(filename, 'r') as infile:
          try:
               return json.load(infile)
          except:
               return None

def write_cachefile(filename, data):
     filename = cache_dir + filename
     with open(filename, 'w') as outfile:
          json.dump(data, outfile)


def get_cached_powers():
     cached_data = read_cachefile('powers.json')
     if cached_data is None: 
          return []
     else:
          return cached_data['powers']


def save_cached_powers(powers):
     cache_data = {}
     cache_data['powers'] = powers
     write_cachefile('powers.json', cache_data)