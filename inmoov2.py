##################################################################################################  
#   .___           _____                     ________  
#   |   | ____    /     \   ____   _______  _\_____  \ 
#   |   |/    \  /  \ /  \ /  _ \ /  _ \  \/ //  ____/ 
#   |   |   |  \/    Y    (  <_> |  <_> )   //       \ 
#   |___|___|  /\____|__  /\____/ \____/ \_/ \_______ \
#            \/         \/                           \/
##################################################################################################

import logging


class InMoov2:
    def __init__(self, name, gateway):
        if not gateway:
            raise ValueError("gateway cannot be None")
        if not name:
            raise ValueError("name cannot be None")
        
        # internal references
        self._name = name

        # JVM specific - wouldn't be needed in native Python Services
        self._gateway = gateway
        self._runtime = gateway.getRuntime()
        
        # starting service and getting reference on jvm
        self._service = self._runtime.start(name, "InMoov2")
        
        self._logger = logging.getLogger(__name__)

    def print_value(self):
        print(self.value)


def main():
    # Configure logging settings (similar to the previous example)
    # logging.basicConfig(
    #     level=logging.INFO,
    #     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    #     filename='my_log.log',
    #     filemode='w'
    # )

    # Create an instance of MyClass
    my_instance = InMoov2(py4j)

    # Call a method that logs messages
    my_instance.some_method()


if __name__ == "__main__":
    main()