#Oussama Konate, Thomas Delépine, groupe 8

def remove_all(l, x):
  while x in l:
    l.remove(x)
  return l

def count_occurence(l, x):
	cpt = 0
	for e in l:
		if e == x:
			cpt = cpt + 1
	return cpt

