import random

class PrimaryReplicaRouter:

    def __init__(self):
        self.replica_dbs = ['replica1', 'replica2']
        self.next_replica = 0

    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen replica.
        """
        db_to = self.replica_dbs[self.next_replica]
        self.next_replica = (self.next_replica + 1) % 2
        print('****'*20)
        print(db_to)
        return db_to 

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        return 'primary'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_set = {'primary', 'replica1', 'replica2'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True