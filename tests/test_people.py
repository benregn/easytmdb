# -*- coding: utf-8 -*-
import unittest

from easytmdb.people import People, Credits, Jobs


class TestPeople(unittest.TestCase):
    def test_info(self):
        id = 287
        name = 'Brad Pitt'
        person = People(id)
        person.info()
        self.assertEqual(person.name, name)

    def test_movie_credits(self):
        id = 287
        person = People(id)
        person.movie_credits()
        self.assertTrue(hasattr(person, 'cast'))

    def test_TV_credits(self):
        id = 287
        person = People(id)
        person.tv_credits()
        self.assertTrue(hasattr(person, 'cast'))

    def test_combined_credits(self):
        id = 287
        person = People(id)
        person.combined_credits()
        self.assertTrue(hasattr(person, 'cast'))

    def test_images(self):
        id = 287
        person = People(id)
        person.images()
        self.assertTrue(hasattr(person, 'profiles'))

    def test_changes(self):
        id = 287
        person = People(id)
        person.changes()
        self.assertTrue(hasattr(person, 'changes'))

    def test_popular(self):
        person = People()
        person.popular()
        self.assertTrue(hasattr(person, 'results'))

    def test_latest(self):
        person = People()
        person.latest()
        self.assertTrue(hasattr(person, 'birthday'))


class TestCredits(unittest.TestCase):
    def test_info(self):
        id = '52542282760ee313280017f9'
        department = 'Actors'
        credit = Credits(id)
        credit.info()
        self.assertEqual(credit.department, department)


class TestJobs(unittest.TestCase):
    def test_list(self):
        lst = Jobs()
        lst.list()
        self.assertTrue(hasattr(lst, 'jobs'))
