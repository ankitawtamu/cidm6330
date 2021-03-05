class RomantoIntegers:
  def Roman_to_integer(self, numeral):
      d = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
      out = 0
      n = len(numeral)
      for (i, c) in enumerate(numeral):
         if i < n - 1 and d[c] < d[numeral[i + 1]]:
            out -= d[c]
         else:
            out += d[c]
      return out

