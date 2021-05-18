s1 = float(input('Digite um segmento: '))
s2 = float(input('Digite outro segmento: '))
s3 = float(input('Digite outro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo!')