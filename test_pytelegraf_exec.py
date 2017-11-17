import pytelegraf_exec
import re

def test_output():
    '''
    Tests if the output function return the correct values.
    '''
    #expected = 'test,t2=t2,t1=t1 v1=1,v2=v2'

    out = pytelegraf_exec.TelegrafExec("test")
    out.add_tags({"t1":"t1", "t2":"t2"})
    out.add_values({"v1":"1", "v2":"v2"})

    assert re.match('test,(?:t[0-9]=t[0-9],?){2}\s(?:v[0-9]=[v0-9]+,?){2}', out.output())

def test_print_output(capsys):
    '''
    Tests if the print function outputs to stdout correctly.
    The line must end in a \n character.
    '''
    expected = "test,t2=t2,t1=t1 v1=1,v2=v2\n"

    out = pytelegraf_exec.TelegrafExec("test")
    out.add_tags({"t1":"t1", "t2":"t2"})
    out.add_values({"v1":"1", "v2":"v2"})
    out.print_output()

    stdout,_ = capsys.readouterr()
    assert re.match('test,(?:t[0-9]=t[0-9],?){2}\s(?:v[0-9]=[v0-9]+,?){2}\n', stdout)
