"""
Django command to wait for the database to be available.
"""
import time

from psycopg import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

from django.db import connections

class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                #time.sleep(5)
                self.check(databases=['default'])
                conn = connections['default']
                c = conn.cursor()
                
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 0.1 second...')
                time.sleep(0.1)

        self.stdout.write(self.style.SUCCESS('Database available!'))