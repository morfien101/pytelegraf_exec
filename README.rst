=====================================
Description
=====================================
pytelegraf_exec is used to create telegraf line text which and be passed in to the telegraf exec plugin.

=====
Usage
=====


| import pytelegraf_exec
| 
| # Create a new tracker
| out = pytelegraf_exec.TelegrafExec("test")
|
| # Add your tags that you want. Can be called multiple times
| out.add_tags({"t1":"t1", "t2":"t2"})
| 
| # Add your values that you want. Can be called multiple times
| out.add_values({"v1":"1", "v2":"v2"})
| 
| text = out.output()
| # You will get a returned line like so
| # 'test,t2=t2,t1=t1 v1=1,v2=v2'
| # Or print directly
| 
| out.print_output()
| # You will get something like this in stdout.
| # "test,t2=t2,t1=t1 v1=1,v2=v2\n"
