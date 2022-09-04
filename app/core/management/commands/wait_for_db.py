from django.db.utils import OperationalError
import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2OpError


class Command(BaseCommand):
    """Django commands"""

    def handle(self, *args, **options):
        self.stdout.write('wait for database...')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('database unvailable, waiting 1 second ...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('database available!'))
