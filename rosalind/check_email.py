"""
Created on Fri Mar 11 20:41:06 2016

@author: Grigory Kovtun
"""
import re

def check_email(email):
    len_name = email.find('@')
    len_domen = len(email) - len_name - 1
    if len_name < 1 or len_name >128 or len_domen < 3 or len_domen > 256:
        return False
                
    sub_name = '("(\.?[_a-z0-9!,:-]*)*(\.?)")*'
    name = '^(' + sub_name + '\.?([_a-z0-9-]+' + sub_name + '))*(\.?)@'
    
    sub_domen = '(([a-z0-9_]+[a-z0-9_-]*[a-z0-9_]+)|([a-z0-9_]+))'
    domen = '(' + sub_domen + '(\.' + sub_domen + '+)*)$'
    
    p = re.compile(name + domen)
    if p.search(email) is None:
        return False
    return True
    
import unittest

class TestCheckEmail(unittest.TestCase):
    
    def test_availability_at(self):
        self.assertTrue(check_email("test@jmail.com"))
        self.assertFalse(check_email("test@jmail@com"))
        self.assertFalse(check_email("test@@jmail.com"))
        self.assertFalse(check_email("test.jmail.com"))
        
    def test_domen_len(self):
        self.assertTrue(check_email("test@" + "t"*256))
        self.assertFalse(check_email("test@" + "t"*257))
        self.assertTrue(check_email("test@" + "t"*3))
        self.assertFalse(check_email("test@" + "t"*2))
        self.assertFalse(check_email("test@"))
        
    def test_domen_composition(self):
        self.assertTrue(check_email("test@j-jmail.com"))
        self.assertTrue(check_email("test@0169jmail.com"))
        self.assertTrue(check_email("test@j.mai_l.com"))
        self.assertFalse(check_email("test@jмэйл.com"))
        self.assertFalse(check_email("test@jmail .com"))
        self.assertFalse(check_email("test@jmail+.com"))
        self.assertFalse(check_email("test@jmail-.com"))
        self.assertFalse(check_email("test@jmаil.com")) # Russian а
        self.assertFalse(check_email("test@jmAil.com"))
        self.assertFalse(check_email("test@jma/il.com"))
        self.assertFalse(check_email("test@jma,il.com"))
        self.assertFalse(check_email("test@jma!!il.com"))
        self.assertFalse(check_email("test@jma:il.com"))
        
    def test_domen_subdomens(self):
        self.assertTrue(check_email("test@jmail.cong.com"))
        self.assertFalse(check_email("test@.jmail.com"))
        #self.assertFalse(check_email("test@com")) # True or False???
        self.assertFalse(check_email("test@jmail.com."))
        self.assertFalse(check_email("test@jmail..com"))
        
    def test_domen_subdomens_start_end(self):
        self.assertTrue(check_email("test@j-m-a-i----l.c-o-m"))
        self.assertFalse(check_email("test@-jmail.cong.com"))
        self.assertFalse(check_email("test@jmail-.cong.com"))
        self.assertFalse(check_email("test@jmail.cong.com-"))
        self.assertFalse(check_email("test@jmail-.-cong.com"))
        self.assertFalse(check_email("test@jmail.--cong.com"))
        self.assertFalse(check_email("test@-jmail.cong.com"))
        
    def test_name_len(self):
        self.assertTrue(check_email("test@jmail.com"))
        self.assertTrue(check_email("t"*1+"@jmail.cong.com"))
        self.assertTrue(check_email("t"*128+"@jmail.cong.com"))
        self.assertFalse(check_email("t"*129+"@jmail.cong.com"))
        self.assertFalse(check_email("@jmail.cong.com"))
        
    def test_name_composition(self):
        self.assertTrue(check_email("-test.01_59@jmail.com"))
        self.assertTrue(check_email("te-st@jmail.com"))
        self.assertFalse(check_email("test;@jmail.com"))
        self.assertFalse(check_email("te'st.@jmail.com"))
        self.assertFalse(check_email("TESt@jmail.com"))
        self.assertFalse(check_email("Тест-t@jmail.com"))
        self.assertFalse(check_email("tеst@jmail.com")) #Russian e

        
        self.assertTrue(check_email("t.est@jmail.com"))
        self.assertTrue(check_email("t.es.t@jmail.com"))
        self.assertTrue(check_email(".t.es.t@jmail.com"))
        self.assertTrue(check_email("test.@jmail.com"))
        self.assertFalse(check_email("te..st@jmail.com"))
        self.assertFalse(check_email(".test...@jmail.com"))
        self.assertFalse(check_email("..test@jmail.com"))
        
        self.assertTrue(check_email('''te""st@jmail.com'''))
        self.assertTrue(check_email('''te""s"t"@jmail.com'''))
        self.assertTrue(check_email('''te"!,:"st@jmail.com'''))
        self.assertFalse(check_email('''te"st@jmail.com'''))
        self.assertFalse(check_email('''te!""st@jmail.com'''))
        self.assertFalse(check_email('''te!""?st@jmail.com'''))
        self.assertFalse(check_email('''te"?st@jmail.com'''))

        self.assertTrue(check_email('''te"!,:"st@jmail.com'''))
        self.assertFalse(check_email("te!st.@jmail.com"))  
        self.assertFalse(check_email("test:@jmail.com"))
        self.assertFalse(check_email("test,t@jmail.com"))
        
        # Interesting cases. I'm not sure!
        self.assertFalse(check_email('''test"",:!""t@jmail.com'''))
        self.assertTrue(check_email('''test",:!"",:!"t@jmail.com'''))
        self.assertFalse(check_email('''test",:!",:!""t@jmail.com'''))
        self.assertFalse(check_email('''test",:!",:!",:!"t@jmail.com'''))
        self.assertFalse(check_email('''test"",:!",:!"t@jmail.com'''))
        self.assertFalse(check_email('''t"est,:!",:!""t@jmail.com'''))
        
        
if __name__ == '__main__':
    unittest.main()    
