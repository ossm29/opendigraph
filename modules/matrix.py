import random

def random_int_list(n, bound): #@param : n (int) : nb éléments | bound (int) : valeur max
  liste = []
  for i in range(0,n):
    liste.append(random.randint(0,bound))
  return liste #@return : int list
####################################################
def random_int_matrix(n, bound, null_diag=False):#@param : n (int) : nb éléments | bound (int) : valeur max | null_diag (boolean)
  liste = []
  for element in range(0,n):
    liste.append(random_int_list(n,bound))
  if null_diag:
    for i in range(0,n):
      liste[i][i] = 0
  return liste #@return : int list list
####################################################
def random_symetric_int_matrix(n, bound,null_diag=False):#@param : n (int) : nb éléments | bound (int) : valeur max | null_diag (boolean)
  liste = []
  for i in range(0, n):
    liste.append([0 for j in range(0, n)])
  for i in range(0, n):
    for j in range(0, i + 1):
      r = random.randint(0,bound)
      liste[i][j] = liste[j][i] = r
  if null_diag:
    for i in range(0,n):
      liste[i][i] = 0
  return liste #@return : int list list













