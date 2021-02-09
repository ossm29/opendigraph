import random

def random_int_list(n, bound):
  liste = []
  for i in range(0,n):
    liste.append(random.randint(0,bound))
  return liste

def random_int_matrix(n, bound):
  liste = []
  for i in range(0,n):
    liste.append(random_int_list(n,bound))
  return liste

def random_int_matrix(n, bound, null_diag=True):
  liste = []
  for element in range(0,n):
    liste.append(random_int_list(n,bound))
  for i in range(0,n):
    liste[i][i] = 0
  return liste

def random_symetric_int_matrix(n, bound,null_diag=True):
  liste = []
  for i in range(0,n):
    for j in range(0,i):
      r = random.randint(0,bound)
      liste[i][j] = liste[j][i] = r
    liste.append(random_int_list(n,bound))

  for i in range(0,n):
    liste[i][i] = 0
  return liste