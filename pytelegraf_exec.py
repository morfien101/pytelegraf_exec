class TelegrafExec(object):
    '''
    TelegrafExec is a class that is used to output text in telegraf
    line format. This will make it easier to execute commands via the
    telegraf exec plugin.
    '''
    def __init__(self, name):
        '''
        init takes the name of the metric that you are working with.
        
        Args:
            name(string): Name of the metric as you want to see it in influxdb
        '''
        self.tags = {}
        self.values = {}
        self.name = name

    def add_tags(self, new_tags):
        '''
        add_tags is used to add tags to the current collection.
        It takes a dictionary.
        '''
        self.tags = self._merger(self.tags, new_tags)

    def add_values(self, new_values):
        '''
        add_values is used to add values to the current collection.
        It takes a dictionary.
        '''
        self.values = self._merger(self.values, new_values)

    def _merger(self, current_dict, merge_this):
        '''
        _merger takes the current dictionary and merges the passed in values.
        Args:
            current_dict(dict): An empty or prepopulated dictionary
            merge_this(dict): A prefferably non-empty dictionary
        '''
        for key, value in merge_this.items():
            current_dict[key] = value
        return current_dict

    def output(self):
        '''
        output will print the values and tags that have been collected
        in the correct influx line format which is consumed by telgraf
        exec plugin.
        '''
        # This is the format that we are looking for.
        #name,<tags> <values>
        #cpu,cpu=cpu0,host=foo,datacenter=us-east usage_idle=99,usage_busy=1
        name = self.name
        tags = self._mux_text(self.tags)
        values = self._mux_text(self.values)
        s_formated = '{0},{1} {2}'.format(name, tags, values)
        
        return s_formated

    def print_output(self):
        '''
        print_output will send the line output to the stdout.
        '''
        print(self.output())

    def _mux_text(self, dic):
        '''
        _mux_text will take a dict and change it into a string with an =
        between the key and value. It will also join all the key value pairs
        with a , then return the new string.
        '''
        text_list = []
        for key, value in dic.items():
            text_list.append("{0}={1}".format(key, value))
        return ','.join(text_list)
