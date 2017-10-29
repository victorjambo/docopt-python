"""
prints the command entered after dojo
Usage:
    dojo <commands>
    q
    Options:
    -h --help Show this screen.
    -v --version
"""
import cmd
from docopt import docopt, DocoptExit
from src.dojo import Dojo


def app_exec(func):
    """
    Decorator definition for the app.
    takes the commands passed to dojo
    it does this 'docopt(__doc__)'
    it works but am not sure why Hehehe
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            msg = "Invalid command! See help."
            print(msg)
            print(e)
            return

        except SystemExit:
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)

    return fn


class PrintDojo(cmd.Cmd):
    prompt = "~>"  # instead of printing '(Cmd)' it will print '~>'
    print(__doc__)  # this will print the comments from line 1 to 9 above
    dojo_instance = Dojo()  # creates an instance our our class Dojo()

    @app_exec  # same decorator defined above ~ line 15
    def do_dojo(self, arg):  # the method has to start with 'do_'
        """Prints the command
        Usage: dojo <commands>...
        """
        argument_entered = arg["<commands>"]  # command entered after dojo
        """Our instance of class Dojo() is calling method getText"""
        result = self.dojo_instance.getText(argument_entered)
        print(result)

    @app_exec
    def do_q(self, arg):
        """Exits the app.
        Usage: q
        """
        exit()


if __name__ == '__main__':
    """Main calls class PrintDojo() in a loop
    stops cli from exiting
    """
    PrintDojo().cmdloop()
