import atexit,io,sys

buffer = io.BytesIO()
sys.stdout = buffer


# print via here
@atexit.register
def write():
    sys.__stdout__.write(str(buffer.getvalue()))

