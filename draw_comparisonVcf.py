'''
Created on 2021.3.30

@author: Zhi Zhang

@email: zhi.zhang@lns.etat.lu

draw picture for hap.py summary result
======================================

'''

#!/usr/bin/env python
import os
import re
import sys
import glob
import argparse
import shutil
from time import time, ctime
import datetime
import logging
import pandas as pd
import numpy as np
import seaborn as sns

__version__ = '0.1'
USAGE = '''
'''
def main0(args):
    print(args)
    summary_input=args.summary_input
    output_dir = os.path.dirname(summary_input)
    summary_data=pd.read_csv(summary_input)
    snp_all=pd.DataFrame(columns=["snp_all","Dijon", "Custom"], 
                  data=[["common",summary_data.iloc[2]['TRUTH.TP'],summary_data.iloc[2]['TRUTH.TP']],
                        ["uniqueDijon",summary_data.iloc[2]['TRUTH.FN'],0],
                        ["uniqueCustom",0,summary_data.iloc[2]['QUERY.FP']]])

    snp_pass= pd.DataFrame(columns=["snp_pass","Dijon", "Custom"], 
                  data=[["common",summary_data.iloc[3]['TRUTH.TP'],summary_data.iloc[3]['TRUTH.TP']],
                        ["uniqueDijon",summary_data.iloc[3]['TRUTH.FN'],0],
                        ["uniqueCustom",0,summary_data.iloc[3]['QUERY.FP']]])

    indel_all= pd.DataFrame(columns=["indel_all","Dijon", "Custom"], 
                  data=[["common",summary_data.iloc[0]['TRUTH.TP'],summary_data.iloc[0]['TRUTH.TP']],
                        ["uniqueDijon",summary_data.iloc[0]['TRUTH.FN'],0],
                        ["uniqueCustom",0,summary_data.iloc[0]['QUERY.FP']]])

    indel_pass= pd.DataFrame(columns=["indel_pass","Dijon", "Custom"], 
                  data=[["common",summary_data.iloc[1]['TRUTH.TP'],summary_data.iloc[1]['TRUTH.TP']],
                        ["uniqueDijon",summary_data.iloc[1]['TRUTH.FN'],0],
                        ["uniqueCustom",0,summary_data.iloc[1]['QUERY.FP']]])
    sns.set()
    snp_all_plot = snp_all.set_index('snp_all').T.plot(kind='bar', stacked=True, title = "snp_all", ylim=(0,80000), figsize=(12,9))
    snp_pass_plot = snp_pass.set_index('snp_pass').T.plot(kind='bar', stacked=True, title = "snp_pass", ylim=(0,80000), figsize=(12,9))
    indel_all_plot = indel_all.set_index('indel_all').T.plot(kind='bar', stacked=True, title = "indel_all", ylim=(0,8000), figsize=(12,9))
    indel_pass_plot = indel_pass.set_index('indel_pass').T.plot(kind='bar', stacked=True, title = "indel_pass", ylim=(0,8000), figsize=(12,9))

    snp_all_plot.figure.savefig(os.path.join(output_dir,"snp_all.png"))
    snp_pass_plot.figure.savefig(os.path.join(output_dir,"snp_pass.png"))
    indel_all_plot.figure.savefig(os.path.join(output_dir,"indel_all.png"))
    indel_pass_plot.figure.savefig(os.path.join(output_dir,"indel_pass.png"))

def main():
    parser = argparse.ArgumentParser(
        description='draw picture for hap.py summary result')
    subparsers = parser.add_subparsers(help='sub-command help')
    parser_0 = subparsers.add_parser('0', description='draw picture for hap.py summary result',
                                     help='draw picture for hap.py summary result', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser_0.add_argument('-i', '--summary_input',
                          type=str, help='the summary input from hap.py')
    parser_0.set_defaults(func=main0)

    args = parser.parse_args(sys.argv[1:])
    args.func(args)


if __name__ == '__main__':
    main()
