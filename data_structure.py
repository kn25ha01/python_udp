import ctypes

max_bbox = 1

class BoundingBox(ctypes.BigEndianStructure):
  _fields_ = [
    ('class_no', ctypes.c_uint32),
    ('midpoint_x', ctypes.c_float),
    ('midpoint_y', ctypes.c_float),
    ('width', ctypes.c_float),
    ('height', ctypes.c_float),
    ('probability', ctypes.c_float)
  ]

class Payload(ctypes.BigEndianStructure):
  _fields_ = [
    ('seq_no', ctypes.c_uint32),
    ('unixtime', ctypes.c_double),
    ('bbox', BoundingBox * max_bbox)
  ]

def print_payload(payload):
  print(f'sequencial no : {payload.seq_no}')
  print(f'unixtime      : {payload.unixtime}')
  for i in range(max_bbox):
    print(f'bbox:{i}')
    print(f'  - class           : {payload.bbox[i].class_no}')
    print(f'  - probability     : {payload.bbox[i].probability}')
    print(f'  - (mid x, mid y)  : ({payload.bbox[i].midpoint_x}, {payload.bbox[i].midpoint_y})')
    print(f'  - (width, height) : ({payload.bbox[i].width}, {payload.bbox[i].height})')
    print('')

if __name__ == "__main__":
  bbox = BoundingBox()
  print(ctypes.sizeof(bbox))
  payload = Payload()
  print(ctypes.sizeof(payload))

  import time
  payload.unixtime = time.time()
  print_payload(payload)
