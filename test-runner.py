import unittest
import importlib
import pandas as pd
import sqlite3

class TestAssignmentTwo(unittest.TestCase):
    def test_01(self):
        result_01 = pd.read_sql(asgmt.answer_01, connection)
        self.assertEqual(result_01.shape, (5, 2))
    def test_02(self):
        result_02 = pd.read_sql(asgmt.answer_02, connection)
        self.assertEqual(result_02.shape, (22, 1))
        counties = result_02.iloc[:, 0].values.tolist()
        self.assertIn("臺北市", counties)
        self.assertIn("臺南市", counties)
        self.assertIn("臺東縣", counties)
        self.assertIn("臺中市", counties)
    def test_03(self):
        result_03 = pd.read_sql(asgmt.answer_03, connection)
        self.assertEqual(result_03.shape, (37, 1))
        towns = result_03.iloc[:, 0].values.tolist()
        self.assertIn("安平區", towns)
        self.assertIn("官田區", towns)
        self.assertIn("東區", towns)
        self.assertIn("關廟區", towns)
        self.assertIn("玉井區", towns)
        self.assertIn("鹽水區", towns)
    def test_04(self):
        result_04 = pd.read_sql(asgmt.answer_04, connection)
        self.assertEqual(result_04.shape, (16, 1))
        counties = result_04.iloc[:, 0].values.tolist()
        self.assertNotIn("臺北市", counties)
        self.assertNotIn("臺南市", counties)
        self.assertNotIn("新北市", counties)
        self.assertNotIn("桃園市", counties)
        self.assertNotIn("臺中市", counties)
        self.assertNotIn("高雄市", counties)
    def test_05(self):
        result_05 = pd.read_sql(asgmt.answer_05, connection)
        self.assertEqual(result_05.shape, (1, 1))
        ans = result_05.iloc[:, 0].values[0]
        self.assertEqual(ans, 17795)
    def test_06(self):
        result_06 = pd.read_sql(asgmt.answer_06, connection)
        self.assertEqual(result_06.shape, (1, 1))
        ans = result_06.iloc[:, 0].values[0]
        self.assertEqual(ans, 328)
    def test_07(self):
        result_07 = pd.read_sql(asgmt.answer_07, connection)
        self.assertEqual(result_07.shape, (16, 2))
    def test_08(self):
        result_08 = pd.read_sql(asgmt.answer_08, connection)
        self.assertEqual(result_08.shape, (1, 1))
        ans = result_08.iloc[:, 0].values[0]
        self.assertGreaterEqual(ans, 680000)
    def test_09(self):
        result_09 = pd.read_sql(asgmt.answer_09, connection)
        self.assertEqual(result_09.shape, (3, 3))
        party_ids = result_09.iloc[:, 0].values.tolist()
        self.assertIn(29, party_ids)
        self.assertIn(1, party_ids)
        self.assertIn(15, party_ids)
        parties = result_09.iloc[:, 1].values.tolist()
        self.assertIn("民主進步黨", parties)
        self.assertIn("中國國民黨", parties)
        self.assertIn("台灣民眾黨", parties)
    def test_10(self):
        result_10 = pd.read_sql(asgmt.answer_10, connection)
        self.assertEqual(result_10.shape, (3, 5))
        numbers = result_10.iloc[:, 0].values.tolist()
        self.assertIn(1, numbers)
        self.assertIn(2, numbers)
        self.assertIn(3, numbers)
        parties = result_10.iloc[:, 1].values.tolist()
        self.assertIn("民主進步黨", parties)
        self.assertIn("中國國民黨", parties)
        self.assertIn("台灣民眾黨", parties)
        candidates = result_10.iloc[:, 2].values.tolist()
        self.assertIn("柯文哲/吳欣盈", candidates)
        self.assertIn("賴清德/蕭美琴", candidates)
        self.assertIn("侯友宜/趙少康", candidates)
        sum_votes = result_10.iloc[:, 3].values.tolist()
        self.assertEqual(sum(sum_votes), 3690466 + 5586019 + 4671021)
        
connection = sqlite3.connect("taiwan_election_2024.db")
asgmt = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentTwo)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"You've got {number_of_successes} successes among {number_of_test_runs} questions.")