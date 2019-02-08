import logging , time , re , random
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("path_to_source_log_file" , type=str ,help="insert path to source log file like './logs/action.log' .")
parser.add_argument("-t","--timestamp"  , help="this option to insert timestamp in new log file" , action="store_true")
parser.add_argument("--thread"  , help="this option to insert threadname in new log file" , action="store_true")
parser.add_argument("-l","--loglevel"  , help="this option to insert loglevel in new log file" , action="store_true")
parser.add_argument("-d","--destfile"  , help="this option to store new log file to your path" , default="./app.log")
args = parser.parse_args()
if args.timestamp and args.thread and args.loglevel:
    logging.basicConfig(filename=args.destfile, filemode='a', level=logging.DEBUG , format='%(asctime)s [%(threadName)s] [%(levelname)s]  %(message)s')
else:
    log_format = ''
    if args.timestamp: log_format += '%(asctime)s '
    if args.thread: log_format += '[%(threadName)s] '
    if args.loglevel: log_format += '[%(levelname)s]'
    log_format += '%(message)s'
    logging.basicConfig(filename=args.destfile, filemode='a', level=logging.DEBUG , format=log_format)
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
    tmp = formatting([re.findall(' - .*',t) for t in text])
    if not tmp: return formatting(text,abnormal=True)
    return tmp

def wr_log(logs_custom):
    while True:
        try:
            time.sleep(1)
            thislog = random.choice(logs_custom)
            print("[+] write log ["+ thislog + "].")
            logging.warning(thislog)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    lst_logms = insert_ms()
    custom_log = list(set(lst_logms))
    wr_log(custom_log)