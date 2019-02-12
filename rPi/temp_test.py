"""
20160518 - Created by stillborn86 (c)

This sketch will deliver multiple temperature readings from your rPi, one from
the beginning (at idle) and five more after running your process at maximum
stress for two minutes.
"""

vcgencmd measure_temp
sysbench --test=cpu --cpi-max-prime=2000 --num-threads=4 run >/dev/null 2>&1
vcgencmd measure_temp
sysbench --test=cpu --cpi-max-prime=2000 --num-threads=4 run >/dev/null 2>&1
vcgencmd measure_temp
sysbench --test=cpu --cpi-max-prime=2000 --num-threads=4 run >/dev/null 2>&1
vcgencmd measure_temp
sysbench --test=cpu --cpi-max-prime=2000 --num-threads=4 run >/dev/null 2>&1
vcgencmd measure_temp
sysbench --test=cpu --cpi-max-prime=2000 --num-threads=4 run >/dev/null 2>&1
vcgencmd measure_temp
