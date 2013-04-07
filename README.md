Whiskerboard-tools
==================

whiskerboard-tools contains a set of modules/tools I am using with our [api-based whiskerboard](http://github.com/sijis/whiskerboard/) setup.

Quick start guide
-----------------
    $ git clone git@github.com:sijis/whiskerboard-tools.git
    $ cd whiskerboard-tools
    $ sudo pip install -r requirements.txt (if any)
    $ add whiskerboard-tools to your python path

Quick Usage
-----------------
```
import whiskerboard

status = whiskerboard.WhiskerBoard(host='status.example.com', port='80')

# enter logic to determine the status of your services
# status.update_status(<status>, <mesassge>, <service-name>)

status.update_status('up', 'All services operational.', 'app1')
status.update_status('down', 'All services are down.', 'app1')
status.update_status('warning', 'Services are degraded.', 'app1')

```

