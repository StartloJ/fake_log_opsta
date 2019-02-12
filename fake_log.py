import logging , time , re , random
import argparse
DURATION = 1 # second

parser = argparse.ArgumentParser()

parser.add_argument("path_to_source_log_file" , type=str ,help="insert path to source log file like './logs/action.log' .")
parser.add_argument("-a","--all_default" , help="this option to use default log format is -[ asctime [threadName] levelname  message ]-" , action="store_true")
parser.add_argument("--text" , help="this option to insert sometext in new log file" , type=str)
parser.add_argument("-d","--destfile" , help="this option to store new log file to your path" , default="./app.log")
parser.add_argument("-f","--filter" , help="this option for edit regex filter source log to short messages such as '.*' ." , default="\s-\s.*")
parser.add_argument("--logformat" , help="this option for edit log-header format without message body to generate ." , default="%(asctime)s [%(threadName)s] %(levelname)s ")
parser.add_argument("--timeformat" , help="this option for edit timestamp format ref. in [http://strftime.org] ." , default="%Y-%m-%d %H:%M:%S ")

args = parser.parse_args()
if not args.all_default:
    log_format = ''
    log_format += args.logformat
    if args.text: log_format += args.text
    log_format += '%(message)s'
    logging.basicConfig(filename=args.destfile, filemode='a', level=logging.DEBUG , format=log_format,datefmt=args.timeformat)
else:
    logging.basicConfig(filename=args.destfile, filemode='a', level=logging.DEBUG , format="%(asctime)s [%(threadName)s] %(levelname)s  %(message)s",datefmt=args.timeformat)

#path = "./docushare/Monitor.log"

def is_somealpha(text):
    for chr in text:
        if chr.isalpha():
            return True
        else: pass
    return False

def formatting(logms,abnormal=False):
    tmp = list()
    if not abnormal:
        for log in logms:
            if log and is_somealpha(log[0]):
                tmp.append(log[0].replace("\r","").strip())
    else:
        for log in logms:
            tmp_log = log.replace("\r","").strip()
            tmp_log = tmp_log.split(',')
            tmp.append(",".join(tmp_log[1:]))
    return tmp

def insert_ms():
    with open(args.path_to_source_log_file , "r") as f:
        text = f.read().split("\n")
    tmp = formatting([re.findall(args.filter , t) for t in text])
    if not tmp: return formatting(text,abnormal=True)
    return tmp

def wr_log(logs_custom):
    while True:
        try:
            time.sleep(DURATION)
            thislog = random.choice(logs_custom)
            print("[+] write log ["+ thislog + "].")
            logging.warning(thislog)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    lst_logms = insert_ms()
    custom_log = list(set(lst_logms))
    wr_log(custom_log)