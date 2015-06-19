places = ['thousand', 'million', 'billion', 'trillion', 'quadrillionth', 'quintillionth', 'sextillionth', 'septillionth']
nums = ['one', 'two', 'three', 'four', 'five', 'six','seven', 'eight', 'nine'] 
teens = ['eleven', 'twelve', 'thirteen','fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_places = ['ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

from string import zfill

def int_to_str(val):
    if val == 0:
        return 'zero'
        
    words = []
    place = 0
    while val > 0:
            
        part = zfill(str(val), 3)[-3:]
        
        if place > 0 and part != '000':
            words.append(places[place-1])
        
        first_two_digits = int(part[1:])
        
        if 10 < first_two_digits < 20:
            words.append(teens[int(first_two_digits)-11])
        else:
            if part[2] != '0':
                words.append(nums[int(part[2])-1])
            if part[1] != '0':
                words.append(tens_places[int(part[1])-1])
        
        if part[0] != '0':
            words.append('hundred')
            words.append(nums[int(part[0])-1])
        
        place += 1
        val = int(1.*val / 1000)
    
    words.reverse()
    return ' '.join(words)