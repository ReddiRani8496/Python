import os
if os.path.exists("rock.txt"):
  os.remove("rock.txt")
else:
  print("The file does not exist")