import os


images = os.listdir('./')
print(images)
for i in images:
  name = i
  if (name == '.DS_Store'):
      continue;
    
  os.rename(i, i.capitalize());
    
  