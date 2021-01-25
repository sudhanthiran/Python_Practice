import logging
import logging.config

def main():
    #logging.basicConfig(filename='app.log',level=logging.INFO)
    logging.config.fileConfig('log_config.ini')
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    logging.critical('host %s unknown',hostname)
    logging.error("couldn't find item %r",item)
    logging.warning("dep")
    logging.info("Opening file %r, mode=%r",filename,mode)
    logging.debug("test")

if __name__ == '__main__':
    main()


