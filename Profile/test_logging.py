import logging
import profile

def fun():
    for i in range(10000):
        logging.debug("This is a debug log.")
        logging.info("This is a info log.")
        logging.warning("This is a warning log.")
        logging.error("This is a error log.")
        logging.critical("This is a critical log.")

if __name__ == '__main__':
    profile.run('fun()')