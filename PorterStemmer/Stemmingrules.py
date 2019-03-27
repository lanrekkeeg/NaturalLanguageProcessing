import re

class rules:
    def __init__(self):
        self.count_step1 = 0
        self.count_step2 = 0
        self.count_step3 = 0
        self.count_step4 = 0
        self.count_step5 = 0
    # m
    def step_res(self, step):
        if step == 'st-1':
            return self.count_step1
        if step == 'st-2':
            return self.count_step2
        if step == 'st-3':
            return self.count_step3
        if step == 'st-4':
            return self.count_step4
        if step == 'st-5':
            return self.count_step5

    def measurement(self, word, suffix):
        temp = self.replace(suffix, word, '')
        return len(re.findall("([aeiouAEIOU][^aeiouAEIOU])", temp))

    def replace(self, suffix, stem, replwith):
        return re.sub (suffix+'$', replwith, stem)

    # words end specific substring
    def endswith(self, word, suffix):
        
        return (len(re.findall(suffix+'$', word))) > 0  and 1 or 0

    # *v*
    def containvowel(self, word, suffix):
        temp = self.replace(suffix, word, '')
        return len(re.findall('[aeiouAEIOU]+', temp)) > 0 and 1 or 0

    # *d
    def endwithdoubleconsonent(self, word):
        return len(re.findall ('([^aeiouAEIOU][^aeiouAEIOU])$',  word)) > 0 and 1 or 0
    # CVC    
    def endswithCVCformat(self, word):
        
        return len(re.findall ('([^aeiouAEIOU][aeiouAEIOU][^aeiouAEIOUwxyWXY])$',  word)) > 0 and 1 or 0

    # *s,*t,*f ...
    def endswithgivenchar(self, char, word):
        return len(re.findall(char + '$', word)) > 0 and 1 or 0

    def step1a(self, word):
        if self.endswith(word, 'sses'):
            word = self.replace('sses', word, 'ss')
            self.count_step1 += 1
        elif self.endswith(word, 'ies'):
            word = self.replace('ies', word, 'i')
            self.count_step1 += 1
        elif self.endswith(word, 'ss'):
            word = self.replace('ss', word,'ss')
            self.count_step1 += 1
        elif self.endswith(word, 's'):
            word = self.replace('s', word, '')
            self.count_step1 += 1
        else:
            pass
        return word

    def step1b(self, word):

        check_rule = False
        if self.endswith(word, 'eed'):
            if self.measurement(word, 'eed') > 0:
                word = self.replace('eed', word, 'ee')
                self.count_step1 += 1
        elif self.endswith(word, 'ed'):
            if self.containvowel(word, 'ed'):
                word = self.replace('ed', word, '')
                self.count_step1 += 1
                # clean up part for condition 1b-2
                check_rule = True
                
        elif self.endswith(word, 'ing'):
            if self.containvowel(word, 'ing'):
                word = self.replace('ing', word, '')
                # clean up part for condition 1b-3
                self.count_step1 += 1
                check_rule = True
                
        if check_rule:
            if self.endswith(word, 'at'):
                    word = self.replace('at', word, 'ate')
                    self.count_step1 += 1
            elif self.endswith(word, 'bl'):
                    word = self.replace('bl', word, 'ble')
                    self.count_step1 += 1
            elif self.endswith(word, 'iz'):   
                    word = self.replace('iz', word, 'ize')
                    self.count_step1 += 1
            elif (self.endwithdoubleconsonent(word) and not((self.endswith(word, 'l')) or 
                (self.endswith(word, 's')) or (self.endswith(word, 'z')))):
                    suffix = word[len(word)-1] + word[len(word)-1]
                    word = self.replace(suffix, word, word[len(word)-1])
                    self.count_step1 += 1
            elif self.measurement(word, '') == 1 and self.endswithCVCformat(word):
                self.count_step1 += 1
                word += 'e'

        return word

    def step1c(self, word):
        if self.endswith(word, 'y'):
            if self.containvowel(word, 'y'):
                word = self.replace('y', word, 'i')
                self.count_step1 += 1
            
        return word

    def step2(self, word):
         
        if self.endswith(word, 'ational'):
            if self.measurement(word, 'ational') > 0:
                word = self.replace('ational', word, 'ate')
                self.count_step2 += 1
        elif self.endswith(word, 'tional'):
            if self.measurement(word, 'tional')> 0:
                word  = self.replace('tional', word, 'tion')
                self.count_step2 += 1
        elif self.endswith(word, 'enci'):
            if self.measurement(word, 'enci')> 0:
                word  = self.replace('enci', word, 'ence')
                self.count_step2 += 1
        elif self.endswith(word, 'anci'):
            if self.measurement(word, 'anci') > 0:
                word  = self.replace('anci', word, 'ance')
                self.count_step2 += 1
        elif self.endswith(word, 'izer'):
            if self.measurement(word, 'izer') > 0:
                word  = self.replace('izer', word, 'ize')
                self.count_step2 += 1
        elif self.endswith(word, 'abli'):
            if self.measurement(word, 'abli')> 0:
                word  = self.replace('abli', word, 'able')
                self.count_step2 += 1
        elif self.endswith(word, 'alli'):
            if self.measurement(word, 'alli') > 0:
                word  = self.replace('alli', word, 'al')
                self.count_step2 += 1
            
        elif self.endswith(word, 'entli'):
            if self.measurement(word, 'entli') > 0:
                word  = self.replace('entli', word, 'ent')
                self.count_step2 += 1
        elif self.endswith(word, 'eli'):
            if self.measurement(word, 'eli') > 0:
                word  = self.replace('eli', word, 'e')
                self.count_step2 += 1
        elif self.endswith(word, 'ousli'):
            if self.measurement(word, 'ousli') > 0:
                word  = self.replace('ousli', word, 'ous')
                self.count_step2 += 1
        elif self.endswith(word, 'ization'):
            if self.measurement(word, 'ization') > 0:
                word  = self.replace('ization', word, 'ize')
                self.count_step2 += 1
        elif self.endswith(word, 'ation'):
            if self.measurement(word, 'ation') > 0:
                word  = self.replace('ation', word, 'ate')
                self.count_step2 += 1
        elif self.endswith(word, 'ator'):
            if self.measurement(word, 'ator') > 0:
                word  = self.replace('ator', word, 'ate')
                self.count_step2 += 1
        elif self.endswith(word, 'alism'):
            if self.measurement(word, 'alism') > 0:
                word  = self.replace('alism', word, 'al')
                self.count_step2 += 1
        elif self.endswith(word, 'iveness'):
            if self.measurement(word, 'iveness') > 0:
                word  = self.replace('iveness', word, 'ive')
                self.count_step2 += 1
        elif self.endswith(word, 'fulness'):
            if self.measurement(word, 'fulness') > 0:
                word  = self.replace('fulness', word, 'ful')
                self.count_step2 += 1
        elif self.endswith(word, 'ousness'):
            if self.measurement(word,'ousness') > 0:
                word  = self.replace('ousness', word, 'ous')
                self.count_step2 += 1
        elif self.endswith(word, 'aliti'):
            if self.measurement(word, 'aliti') > 0:
                word  = self.replace('aliti', word, 'al')
                self.count_step2 += 1
        elif self.endswith(word, 'iviti'):
            if self.measurement(word, 'iviti') > 0:
                word  = self.replace('iviti', word, 'ive')
                self.count_step2 += 1
        elif self.endswith(word, 'biliti'):
            if self.measurement(word, 'biliti') > 0:
                word  = self.replace('biliti', word, 'ble')
                self.count_step2 += 1
        return word

    def step3(self, word):
        if self.endswith(word, 'icate'):
            word = self.replace('icate', word, 'ic')
            self.count_step3 += 1
        elif self.endswith(word, 'ative'):
            word = self.replace( 'ative', word, '')
            self.count_step3 += 1
        elif self.endswith(word, 'alize'):
            word = self.replace( 'alize', word, 'al')
            self.count_step3 += 1
        elif self.endswith(word, 'iciti'):
            word = self.replace('iciti', word, 'ic')
            self.count_step3 += 1
        elif self.endswith(word, 'ful'):
            word = self.replace('ful', word, '')
            self.count_step3 += 1
        elif self.endswith(word, 'ical'):
            word = self.replace('ical', word, 'ic')
            self.count_step3 += 1
        elif self.endswith(word, 'ness'):
            word = self.replace('ness', word, '')
            self.count_step3 += 1
        return word

    def step4(self, word):
       
        if self.endswith(word, 'al'):
            if self.measurement(word, 'al') > 1:
                word = self.replace('al', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'ance'):
            if self.measurement(word, 'ance') > 1:
                word = self.replace('ance', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'ence'):
            if self.measurement(word, 'ence') > 1:
                word = self.replace('ence', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'er'):
            if self.measurement(word, 'er') > 1:
                word = self.replace('er', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'ic'):
            if self.measurement(word, 'ic') > 1:
                word = self.replace('ic', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'able'):
            if self.measurement(word, 'able') > 1:
                word = self.replace('able', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'ible'):
            if self.measurement(word, 'ible') > 1:
                word = self.replace('ible', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'ant'):
            if self.measurement(word, 'ant') > 1:
                word = self.replace('ant', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'ement'):
            if self.measurement(word, 'ement') > 1:
                word = self.replace('ement', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'ment'):
            if self.measurement(word, 'ment') > 1:
                word = self.replace('ment', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'ent'):
            if self.measurement(word, 'ent') > 1:
                word = self.replace('ent', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'ou'):
            if self.measurement(word, 'ou') > 1:
                word = self.replace('ou', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'ism'):
            if self.measurement(word, 'ism') > 1:
                word = self.replace('ism', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'ate'):
            if self.measurement(word, 'ate') > 1:
                word = self.replace('ate', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'iti'):
            if self.measurement(word, 'iti') > 1:
                word = self.replace('iti', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'ous'):
            if self.measurement(word, 'ous') > 1:
                word = self.replace('ous', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'ive'):
            if self.measurement(word, 'ive') > 1:
                word = self.replace('ive', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'ize'):
            if self.measurement(word,'ize') > 1:
                word = self.replace('ize', word, '')
                self.count_step4 += 1
        elif self.endswith(word, 'ion'):
           
            if self.measurement(word, 'ion') > 1:
                temp = self.replace('ion', word, '')
                if ((self.endswith(temp, 's') or self.endswith(temp, 't'))):
                    word = self.replace('ion', word, '')
                    self.count_step4 += 1
        return word

    def step5a(self, word):
        if self.endswith(word, 'e'):
            if self.measurement( word, 'e') > 1:
                word = self.replace('e', word, '')
                self.count_step5 += 1
            elif self.measurement( word, 'e') == 1 and not (self.endswithCVCformat(word)):
                word = self.replace('e', word, '')
                self.count_step5 += 1
            
        return word

    def step5b(self, word):
        if (self.measurement(word, '') > 1 and self.endwithdoubleconsonent(word) and
        self.endswith(word, word[len(word)-1])):
            word = self.replace(word[len(word)-1], word, '')
            self.count_step5 += 1

        return word