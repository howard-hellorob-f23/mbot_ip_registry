#!/usr/bin/env python3
import os
import json
import argparse
import datetime

LOG_FILE = "/var/log/mbot/mbot_pub_info.log"
IP_DIR = "/var/tmp/mbot_ip_registry/data"


def update_ip_file(hostname, ipaddr, cur_time, log_file=LOG_FILE):
    info = {
        "hostname": hostname,
        "ip": ipaddr,
        "last_update": cur_time.strftime('%d_%b_%Y_%I:%M:%S %p')
    }
    with open(log_file, 'a') as f:
        f.write(hostname)
        f.write("\n")
        f.write(ipaddr)
        f.write("\n")
        f.write(cur_time.strftime('%d_%b_%Y_%I:%M:%S %p'))
        f.write("\n")
    json_obj = json.dumps(info, indent=4)
    with open(os.path.join(IP_DIR, "{}.json".format(hostname)), "w") as outfile:
        outfile.write(json_obj)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-hostname", type=str, help="Hostname of this bot")
    parser.add_argument("-ip", type=str, help="IP of this bot")
    parser.add_argument("-log", type=str, help="Log file location", default=LOG_FILE)
    args = parser.parse_args()

    with open(args.log, 'a') as f:
        f.write("RUNNING...")
        f.write("\n")

    utctoday = datetime.datetime.utcnow() #UTC
    utc2est = datetime.timedelta(hours=5)
    today = utctoday - utc2est #EST
    update_ip_file(args.hostname, args.ip, today, log_file=args.log)
