# -*- coding: utf-8 -*-

# Use this file to easily define all of your cron jobs.
#
# It's helpful to understand cron before proceeding.
# http://en.wikipedia.org/wiki/Cron
#
# Learn more: http://github.com/fengsp/plan

from plan import Plan

cron = Plan("commands")

cron.command('top', every='4.hour', output=dict(stdout='/tmp/top_stdout.log',
                                                stderr='/tmp/top_stderr.log'))
cron.command('yourcommand', every='sunday', at='hour.12 minute.0 minute.30')
# more commands here


if __name__ == "__main__":
    cron.run()
