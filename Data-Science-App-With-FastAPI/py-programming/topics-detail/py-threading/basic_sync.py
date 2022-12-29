import logging
import concurrent.futures
import threading
import time

# logging.getLogger().setLevel(logging.DEBUG)


class FakeDatabase:
    def __init__(self):
        self.value = 0

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)

        with self._lock:
            logging.debug("Thread %s has lock", name)

            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy

            logging.debug("Thread %s about to release lock", name)

        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.DEBUG,
                        datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing locked update. Starting value is %d.",
                 database.value)

    # with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for index in range(3):
            executor.submit(database.locked_update, index)

    logging.info("Testing locked update. Ending value is %d.", database.value)
