# faker_log

Python generate log from source log file in single line only and flush rate 1 message / sec (you can change rate in DURATION line 3)

## Option in script
<pre>
usage: fake_log.py [-h] [-t] [--thread] [--text TEXT] [-l] [-d DESTFILE]
                   [-f FILTER] [--timeformat TIMEFORMAT]
                   path_to_source_log_file

positional arguments:
  path_to_source_log_file               insert path to source log file like './logs/action.log'

optional arguments:
  -h, --help                            show this help message and exit
  -a, --all_default                     this option to use default log format is [ asctime [threadName] levelname message ]
  --text TEXT                           this option to insert sometext in new log file
  -d DESTFILE, --destfile DESTFILE      this option to store new log file to your path
  -f FILTER, --filter FILTER            this option for edit regex filter source log to short messages such as '.*' .
  --logformat LOGFORMAT                 this option for edit log-header format without message body to generate .
  --timeformat TIMEFORMAT               this option for edit timestamp format ref. in [http://strftime.org] .
</pre>

## Explain log format to use in [--logformat]
* asctime => %(asctime)s : is datetime is python get from system.
* threadName => %(threadName)s : is python get from complier thread default is mainthread.
* levelname => %(levelname)s : is python logging generate from log level to flush.

## Default values for some parameter
-a , --all_default : True
-d , --destfile    : "./app.log"
-f , --filter      : "\s-\s.*"
--logformat        : "%(asctime)s [%(threadName)s] %(levelname)s "
--timeformat       : "%Y-%m-%d %H:%M:%S "

## Sample command
command to gen log

+ sample1.log with default format in parameter -a.\
`
    python fake_log.py path/to/file.log -a --timeformat "%d %b %Y %H:%M:%S "
`
+ sample.log with change log format in --logformat.\
`
    python fake_log.py path/to/file.log --logformat "%(asctime)s %(levelname)s [%(threadName)s]" --timeformat "%d %b %Y %H:%M:%S "
`
+ file.csv with filter by regex string.\
`
    python fake_log.py path/to/file.csv -f ',\w.*' --logformat "%(asctime)s" --timeformat "%a %b %d %H:%M:%S %Y ICT"
`

+ file.something with insert text between header and message.\
`
    python fake_log.py path/to/file.stdOut.4 --logformat "%(asctime)s " --timeformat "%d %b %Y %H:%M:%S " --text "- [Thread[Thread-64,5,main]] - 4891379771 [Thread-8] DEBUG mailagent  " --filter "“\s\s-\s.*”"
`