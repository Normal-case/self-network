import darknet

blocks = darknet.parse_cfg('yolov3.cfg')

print(darknet.create_modules(blocks))