import pprint

import googletrans

trans = googletrans.Translator()
str1 = '질량은 물리학에서 물질이 가지고 있는 고유한 양을 일컫는 말이다. 질량의 SI 단위는 킬로그램(kg)이다. 질량의 개념은 고대 그리스의 여러 철학자들의 물질이나 물질관에 대한 토론으로부터 비롯되었다. 질량은 일반적으로 다음 세 가지 방법으로 정의된다.'
str2 = 'Have a nice day'

#pprint.pprint(googletrans.LANGUAGES) #googletrans.LANGUAGES는 번역 언어 ticker들을 불러온다. pprint는 말 그대로 ~예쁘게 프린트하기~다. 한 줄로 된 결과를 알아서 줄 바꿔서 출력해 준다.

result1 = trans.translate(str1, dest='en')
result2 = trans.translate(str2, dest='ja')
result3 = trans.translate(str2, dest='ko')

#print(result1.text)
print(f"번역 결과 1: {result1.text} 입니다") #f string은 자바의 EL과 비슷하다. 굉장히 유용!
print(f"번역 결과 2: {result2.text} 입니다")
print(f"번역 결과 3: {result3.text} 입니다")





