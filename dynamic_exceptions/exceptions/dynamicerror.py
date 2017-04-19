from error import Error
from missingparametererror import MissingParamError

class DynamicError(Error):
    """
    Dynamic error class that will raise a different error given different
    parameters. The err_name attribute that you set will be the object type
    that you create for the error. Ex. err_name of FooError and err_msg of
    'Foo' will raise a dynamicerror.FooError presenting 'Foo' as the message
    """
    def __init__(self, err_name=None, err_msg=None):
        """
        Binds attributes to the object when instantiating this class. Errors
        are raised if either of the attributes are set to None
        """
        self.err_name = err_name
        self.err_msg = err_msg

        # Raise errors if attributes are not set
        if self.err_name == None:
            raise MissingParamError('You must assign err_name when instantiantiating this class')
        if self.err_msg == None:
            raise MissingParamError('You must assign err_msg when instantiating this class')

        else:
            # Call method to raise your custom error
            error = self.raise_error()


    def __str__(self):
        """
        Returns the string representation of the err_msg attribute
        """
        return str(self.err_msg)

    def raise_error(self):
        """
        Creates the custom error class that you want using the built-in
        function type
        """
        def __init__(self, err_msg):
            self.err_msg = err_msg

        # type built-in method can not only check the type of an object, but
        # also create metaclasses. For more information go to
        # https://docs.python.org/3/library/functions.html#type
        error = type(self.err_name, (Exception,), {'__init__': __init__,'__str__':self.__str__})

        # Raises an instance of the Exception inherited metaclass created
        raise error(self.err_msg)
