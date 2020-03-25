# Demonstrate how to customize logging output

import logging


extData = {
    'user': 'albolea@example.com',
    'IP': '192.168.0.1'
}


# TODO: add another function to log from
def anotherFunction():
    logging.debug("This is a debug-level message", extra=extData)


def main():
    # set the output file and debug level, and
    format_str = "User-%(user) at IP-%(IP)s: %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    date_str = "%m/%d/%Y %I:%M:%S %p"

    # TODO: use a custom formatting specification
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        format=format_str,
                        datefmt=date_str)

    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)
    anotherFunction()

if __name__ == "__main__":
    main()
