class ParseArguments:
         
    def __call__ (self, *args, **kwargs):
        """Pretty display of arguments"""
        return "("+ self.parseArgs(*args) + self.splitArgsKwargs(*args, **kwargs) + self.parseKwargs(**kwargs) +")"
    
    def parseArgs (self, *args):
        args_str = ""
        for value in args:
            args_str += repr(value) + ", "
        return args_str[:-2]
    
    def splitArgsKwargs (self, *args, **kwargs):
        spliter_str = ""
        if args and kwargs:
            spliter_str = ", "
        return spliter_str
    
    def parseKwargs (self, **kwargs):
        kwargs_str=""
        for name, value in kwargs.items():
            kwargs_str += name + "=" + repr(value) + ", "
        return kwargs_str[:-2]
        
parseArguments = ParseArguments()