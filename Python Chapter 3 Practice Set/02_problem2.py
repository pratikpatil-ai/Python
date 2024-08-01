letter = ''' Dear <|Name|>,
            You are selected!  
            <|Date|> ''' 

print(letter.replace("<|Name|>","Pratik").replace("<|Date|", "13 August 2006"))
