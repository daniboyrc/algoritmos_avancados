while True:
  h1, m1, h2, m2 = map(int, raw_input().split())
  if [h1, h2, m1, m2] == [0, 0, 0, 0]: break
  
  if h1 < h2 or (h1 == h2 and m1 == m2) or (h1 == h2 and m1 < m2):
    print (h2 * 60 + m2) - (h1 * 60 + m1)
  else:
    print (60 * 24) - (60 * h1 + m1) + (60 * h2 + m2)
