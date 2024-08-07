print(__name__)
print("Module #1 Name=", __name__)
Module #1 Name= __main__
def main():
    print("Module #1 Name=", __name__)

if __name__ == "__main__":
   print("Code is being run directly from Python.")

else:
   print("Code is being run indirectly from import.")

