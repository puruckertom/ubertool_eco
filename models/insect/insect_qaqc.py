"""
.. module:: insect_qaqc
   :synopsis: A useful module indeed.
"""

import insect_model
import logging
import os
import unittest
from StringIO import StringIO
import csv

logger = logging.getLogger('InsectQaqcPage')

data = csv.reader(open(os.path.join(os.environ['PROJECT_PATH'], 'models','insect','insect_qaqc.csv')))

chemical_name=[]
b_species=[]
m_species=[]
bw_quail=[]
bw_duck=[]
bwb_other=[]
bw_rat=[]
bwm_other=[]
avian_ld50=[]
mammalian_ld50=[]
sol = []
aw_bird=[]
mineau=[]
aw_mamm=[]
noaec_d=[]
noaec_q=[]
noaec_o=[]
noael=[]
Species_of_the_bird_NOAEC_CHOICES = []

######Pre-defined outputs########
fw_bird_out = []
fw_mamm_out = []
dose_bird_out = []
dose_mamm_out = []
at_bird_out = []
at_mamm_out = []
fi_bird_out = []
det_out = []
act_out = []
acute_bird_out = []
acuconb_out = []
acute_mamm_out = []
acuconm_out = []
chron_bird_out = []
chronconb_out = []
chron_mamm_out = []
chronconm_out = []


data.next()
for row in data:
    chemical_name.append(row[0])
    b_species.append(row[1])
    m_species.append(row[2])
    bw_quail.append(float(row[3]))
    bw_duck.append(float(row[4]))
    bwb_other.append(float(row[5])) 
    bw_rat.append(float(row[6]))
    bwm_other.append(float(row[7]))
    sol.append(float(row[8]))
    avian_ld50.append(float(row[9])) 
    mammalian_ld50.append(float(row[10]))
    aw_bird.append(float(row[11]))
    mineau.append(float(row[12]))
    aw_mamm.append(float(row[13]))
    noaec_d.append(float(row[14]))
    noaec_q.append(float(row[15]))
    noaec_o.append(float(row[16]))
    noael.append(float(row[17]))
    dose_bird_out.append(float(row[18]))
    dose_mamm_out.append(float(row[19])) 
    at_bird_out.append(float(row[20]))
    at_mamm_out.append(float(row[21]))
    det_out.append(float(row[22]))
    act_out.append(float(row[23]))
    acute_bird_out.append(float(row[24]))
    acuconb_out.append(str(row[25])) 
    acute_mamm_out.append(float(row[26]))
    acuconm_out.append(str(row[27]))
    chron_bird_out.append(float(row[28])) 
    chronconb_out.append(str(row[29]))
    chron_mamm_out.append(float(row[30]))
    chronconm_out.append(str(row[31]))
    Species_of_the_bird_NOAEC_CHOICES.append(str(row[32]))
    
out_fun_fw_bird = []
out_fun_fw_mamm = []
out_fun_dose_bird = []
out_fun_dose_mamm = []
out_fun_at_bird = []
out_fun_at_mamm = []
out_fun_fi_bird = []
out_fun_det = []
out_fun_act = []
out_fun_acute_bird = []
out_fun_acuconb = []
out_fun_acute_mamm = []
out_fun_acuconm = []
out_fun_chron_bird = []
out_fun_chronconb = []
out_fun_chron_mamm = []
out_fun_chronconm = []

def set_globals(**kwargs):
    for argname in kwargs:
        globals()['%s_in' % argname] = kwargs[argname]

class TestCase_fw_bird_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testFW_bird_out_in(self):
        out_fun_fw_bird.append(self.insect_obj.fw_bird_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("fw_bird",self.insect_obj.fw_bird_out,fun)
        self.assertEqual(round(fun,3),round(self.fw_bird_out,3),testFailureMessage)

class TestCase_fw_mamm_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testFW_mamm_out_in(self):
        out_fun_fw_mamm.append(self.insect_obj.fw_mamm_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("fw_mamm",self.insect_obj.fw_mamm_out,fun)
        self.assertEqual(round(fun,3),round(self.fw_mamm_out,3),testFailureMessage)

class TestCase_dose_bird_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testdose_bird_out_in(self):
        out_fun_dose_bird.append(self.insect_obj.dose_bird_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("dose_bird",self.insect_obj.dose_bird_out,fun)
        self.assertEqual(round(fun,3),round(self.dose_bird_out,3),testFailureMessage)

class TestCase_dose_mamm_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testdose_mamm_out_in(self):
        out_fun_dose_mamm.append(self.insect_obj.dose_mamm_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("dose_mamm",self.insect_obj.dose_mamm_out,fun)
        self.assertEqual(round(fun,3),round(self.dose_mamm_out,3),testFailureMessage)

class TestCase_at_bird_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testat_bird_out_in(self):
        out_fun_at_bird.append(self.insect_obj.at_bird_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("at_bird",self.insect_obj.at_bird_out,fun)
        self.assertEqual(round(fun,3),round(self.at_bird_out,3),testFailureMessage)

class TestCase_at_mamm_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testat_mamm_out_in(self):
        out_fun_at_mamm.append(self.insect_obj.at_mamm_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("at_mamm",self.insect_obj.at_mamm_out,fun)
        self.assertEqual(round(fun,3),round(self.at_mamm_out,3),testFailureMessage)

class TestCase_fi_bird_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testfi_bird_out_in(self):
        out_fun_fi_bird.append(self.insect_obj.fi_bird_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("fi_bird",self.insect_obj.fi_bird_out,fun)
        self.assertEqual(round(fun,3),round(self.fi_bird_out,3),testFailureMessage)

class TestCase_det_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testdet_out_in(self):
        out_fun_det.append(self.insect_obj.det_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("det",self.insect_obj.det_out,fun)
        self.assertEqual(round(fun,3),round(self.det_out,3),testFailureMessage)

class TestCase_act_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testact_out_in(self):
        out_fun_act.append(self.insect_obj.act_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("act",self.insect_obj.act_out,fun)
        self.assertEqual(round(fun,3),round(self.act_out,3),testFailureMessage)

class TestCase_acute_bird_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testacute_bird_out_in(self):
        out_fun_acute_bird.append(self.insect_obj.acute_bird_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("acute_bird",self.insect_obj.acute_bird_out,fun)
        self.assertEqual(round(fun,3),round(self.acute_bird_out,3),testFailureMessage)

class TestCase_acuconb_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testacuconb_out_in(self):
        out_fun_acuconb.append(self.insect_obj.acuconb_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("acuconb",self.insect_obj.acuconb_out,fun)
        self.assertEqual(fun,self.acuconb_out,testFailureMessage)

class TestCase_acute_mamm_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testacute_mamm_out_in(self):
        out_fun_acute_mamm.append(self.insect_obj.acute_mamm_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("acute_mamm",self.insect_obj.acute_mamm_out,fun)
        self.assertEqual(round(fun,3),round(self.acute_mamm_out,3),testFailureMessage)

class TestCase_acuconm_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testacuconm_out_in(self):
        out_fun_acuconm.append(self.insect_obj.acuconm_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("acuconm",self.insect_obj.acuconm_out,fun)
        self.assertEqual(fun,self.acuconm_out,testFailureMessage)

class TestCase_chron_bird_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testchron_bird_out_in(self):
        out_fun_chron_bird.append(self.insect_obj.chron_bird_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("chron_bird",self.insect_obj.chron_bird_out,fun)
        self.assertEqual(round(fun,3),round(self.chron_bird_out,3),testFailureMessage)

class TestCase_chronconb_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testacuconb_out_in(self):
        out_fun_chronconb.append(self.insect_obj.chronconb_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("chronconb",self.insect_obj.chronconb_out,fun)
        self.assertEqual(fun,self.chronconb_out,testFailureMessage)

class TestCase_chron_mamm_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testchron_mamm_out_in(self):
        out_fun_chron_mamm.append(self.insect_obj.chron_mamm_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("chron_mamm",self.insect_obj.chron_mamm_out,fun)
        self.assertEqual(round(fun,3),round(self.chron_mamm_out,3),testFailureMessage)

class TestCase_chronconm_out(unittest.TestCase):
    def setUp(self):
        self.insect_obj = insect_object_in
    def testchronconm_out_in(self):
        out_fun_chronconm.append(self.insect_obj.chronconm_out)
        testFailureMessage = "Test of function name: %s expected: %s != calculated: %s" % ("chronconm",self.insect_obj.chronconm_out,fun)
        self.assertEqual(fun,self.chronconm_out,testFailureMessage)

def suite(TestCaseName, **kwargs):
    suite = unittest.TestSuite()
    set_globals(**kwargs)
    suite.addTest(unittest.makeSuite(TestCaseName))
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    result = runner.run(suite)
    stream.seek(0)
    test_out=stream.read()
    return test_out


insect_obj = insect_model.insect(True,True,'qaqc',chemical_name[0], b_species[0], m_species[0], bw_quail[0], bw_duck[0], bwb_other[0], bw_rat[0], bwm_other[0], sol[0], avian_ld50[0], mammalian_ld50[0], aw_bird[0], mineau[0], aw_mamm[0], noaec_d[0], noaec_q[0], noaec_o[0], Species_of_the_bird_NOAEC_CHOICES[0], noael[0])
insect_obj.set_unit_testing_variables()

insect_obj.chemical_name_expected = chemical_name[0]
insect_obj.dose_bird_out_expected = dose_bird_out[0]
insect_obj.dose_mamm_out_expected = dose_mamm_out[0]
insect_obj.at_bird_out_expected = at_bird_out[0]
insect_obj.at_mamm_out_expected = at_mamm_out[0]
insect_obj.det_out_expected = det_out[0]
insect_obj.act_out_expected = act_out[0]
insect_obj.acute_bird_out_expected = acute_bird_out[0]
insect_obj.acuconb_out_expected = acuconb_out[0]
insect_obj.acute_mamm_out_expected = acute_mamm_out[0]
insect_obj.acuconm_out_expected = acuconm_out[0]
insect_obj.chron_bird_out_expected = chron_bird_out[0]
insect_obj.chronconb_out_expected = chronconb_out[0]
insect_obj.chron_mamm_out_expected = chron_mamm_out[0]
insect_obj.chronconm_out_expected = chronconm_out[0]

test_suite_dose_bird_out = suite(TestCase_dose_bird_out, insect_obj=insect_obj)
test_suite_dose_mamm_out = suite(TestCase_dose_mamm_out, insect_obj=insect_obj)
test_suite_at_bird_out = suite(TestCase_at_bird_out, insect_obj=insect_obj)
test_suite_at_mamm_out = suite(TestCase_at_mamm_out, insect_obj=insect_obj)
test_suite_det_out = suite(TestCase_det_out, insect_obj=insect_obj)
test_suite_act_out = suite(TestCase_act_out, insect_obj=insect_obj)
test_suite_acute_bird_out = suite(TestCase_acute_bird_out, insect_obj=insect_obj)
test_suite_acuconb_out = suite(TestCase_acuconb_out, insect_obj=insect_obj)
test_suite_acute_mamm_out = suite(TestCase_acute_mamm_out, insect_obj=insect_obj)
test_suite_acuconm_out = suite(TestCase_acuconm_out, insect_obj=insect_obj)
test_suite_chron_bird_out = suite(TestCase_chron_bird_out, insect_obj=insect_obj)
test_suite_chronconb_out = suite(TestCase_chronconb_out, insect_obj=insect_obj)
test_suite_chron_mamm_out = suite(TestCase_chron_mamm_out, insect_obj=insect_obj)
test_suite_chronconm_out = suite(TestCase_chronconm_out, insect_obj=insect_obj)