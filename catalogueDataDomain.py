import os
import re

dir = 'c:\\svn\\k2\\trunk\\Services'

for root, dirs, files in os.walk(dir):
    for file in files:
        if file == "DataTier.generated.cs":
            filename = os.path.join(root, file)
            file = open(filename)
            contents = file.read()
            file.close()
            
            m = re.findall('public\spartial\sclass\s\w+ResultSet', contents)
            if (m != None):
                for s in m:
                    projectRoot = root.replace(dir + '\\', '')
                    projectName = projectRoot[0:projectRoot.index('\\')]
                    print(projectName, '|', s.replace('public partial class ', '').replace('ResultSet', ''))
            
                
