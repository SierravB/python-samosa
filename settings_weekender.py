#Specify connections here, format is (id,backend,[kwargs])
CONNECTIONS = (
                 (
                    'doctor.hrothgar@gmail',
                    'pygooglevoice',
                    {'GV_USER':"doctor.hrothgar@gmail.com",'GV_PASSWORD':'obscurepgh'}
                 ),
                 (
                    'askory@andrew',
                    'pygooglevoice',    
                    {'GV_USER':"askory@andrew.cmu.edu",'GV_PASSWORD':'w33k3nd3r'},
                 ),
              )

#Set the interval to ping each connection for new Messages
#format is an integer in seconds, or a tuple specifying a range
#from which to wait a random number of seconds each time
CHECK_INTERVAL = (20, 40)

#Specify apps here, format is (app,[connection1,connection2...])
#if no connections are listed, all connections will be checked by default
APPS = (
            ('weekender'),
       )
