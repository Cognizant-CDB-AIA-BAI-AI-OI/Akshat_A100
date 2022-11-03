import subprocess
def config():
  try :
    import sys 
    subprocess.run('conda env create -f Akshat_A100/env/env_akshat.yml python=3.8',shell =True)
    subprocess.run('conda run -n env_akshat python Akshat_A100/funci.py',shell =True)
    subprocess.run('conda env remove -n env_akshat',shell =True)
  except :
    print("Something went wrong..!!")

    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
