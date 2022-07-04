import random
from sample5.new_db_manager import DbSeeder


times = 0


class Seeder:

    @staticmethod
    def seed_name():
        with open('name.txt', 'r') as f:
            mystring = f.readlines()[random.randrange(1, 20)]
            stg = mystring.replace("\n", "")
            return stg

    @staticmethod
    def seed_surname():
        with open('name.txt', 'r') as f:
            mystring = f.readlines()[random.randrange(1, 20)]
            string = mystring.replace("\n", "")
            return string

    @staticmethod
    def seed_groups():
        return random.randrange(1, 3)

    @staticmethod
    def seed_curator_id():
        return random.randrange(1, 3)

    @staticmethod
    def seed_faculty_id():
        return random.randrange(1, 3)

    @staticmethod
    def seed1_mark():
        return random.randrange(3, 6)

    @staticmethod
    def seed2_mark():
        return random.randrange(3, 6)

    @staticmethod
    def seed3_mark():
        return random.randrange(3, 6)


while times != 100:
    DbSeeder.post_marks(Seeder.seed1_mark(), Seeder.seed2_mark(), Seeder.seed3_mark())

    DbSeeder.post_student(Seeder.seed_name(), Seeder.seed_surname(), Seeder.seed_groups(), Seeder.seed_curator_id(), Seeder.seed_faculty_id())

    times += 1
