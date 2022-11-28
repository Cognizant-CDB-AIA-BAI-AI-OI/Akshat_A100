import subprocess
def config():
  try :
    import sys 
    subprocess.run('conda env create -f Akshat_A100/env/env_akshat.yml python=3.8',shell =True)
  
  except :
    
    
    f = open('outputs/a_test_dile.txt','w+')
    f.write(str(sys.exc_info()[0]))
    f.close()
  
  else :
  
    f = open('outputs/a_test_dile.txt','w+')
    f.write('Environment Created')
    f.close()
  
    #time.sleep(150)
    
    try :
      
      subprocess.run('conda run -n env_akshat python Akshat_A100/funci.py',shell =True)
    
    except :
      f = open('outputs/a_test_dile.txt','a+')
      f.write(str(sys.exc_info()[0]))
      f.close()
    
    try :
      
      subprocess.run('conda env remove -n env_akshat',shell =True)
    
    except :
      f = open('outputs/a_test_dile.txt','a+')
      f.write(str(sys.exc_info()[0]))
      f.close()
      
    else :
      f = open('outputs/a_test_dile.txt','a+')
      f.write('Environment Deleted')
      f.close()
  


    
    
