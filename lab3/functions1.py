#1st task
def gramm_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
grams = float(input())
ounces = gramm_to_ounces(grams)
print(ounces)
#2nd task
def  Fahrenheit_to_celsium(Fahrenheit):
    celsium=(5/9)*(Fahrenheit-32)
    return celsium
Fahrenheit = float(input())
celsium=Fahrenheit_to_celsium(Fahrenheit)
print(celsium)
#3rd task
legs = int(input())
heads = int(input())
def solution(heads,legs):
    r_heads = int(legs/2-heads)
    c_heads = int(heads - r_heads)
    print(f"Chickens{c_heads},and rbbits{r_heads}")

solution(heads,legs)