items = [("sword", 100),
          ("potion", 50),
            ("shield", 150),
              ("potion", 50),
                ("spear", 120),
                  ("shield", 150),
                    ("spear", 120), 
                    ("shield", 150)]



def my_items(items_to_show):
    my_dict = {}
   
    # check if item is my tuple
    for item in items_to_show:

        if item in my_dict.keys():
            my_dict[item] += 1
            
    
        # if add 1 to the item
       # if item in my_dict:
          #  my_dict[item] += 1
         
            # encontrar strings em keys no dicionario
          

            

        # else, make it only 1
        else:
            my_dict[item] = 1
        
    #print(my_dict)
        
#def add_item(item):


   
    #print(my_dict)




my_items(items)
 
